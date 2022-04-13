from flask import Flask,abort, current_app, url_for,jsonify,make_response
from werkzeug.exceptions import HTTPException, InternalServerError
from flask_restful import Resource,request, Api,reqparse
from flask_jwt_extended import create_access_token,JWTManager,decode_token,jwt_required
from datetime import datetime
from functools import wraps
from lib.printer import Printer
import threading
import sys
import time
import uuid
import os
from merakitools.main import run
from os import getenv
from multiprocessing import Array,Manager,Value

tasks = {}

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = uuid.uuid4().hex
app.config['JWT_QUERY_STRING_NAME'] = "Meraki_Tools"
api = Api(app)
jwt = JWTManager(app)
jwt.init_app(app)
sync_parser = reqparse.RequestParser()
sync_parser.add_argument('network_name',type=str,location="json",help="network or list of networks to sync")
sync_parser.add_argument('network_tags',type=str,location="json",help="additional meraki netowkr sync key pairs")
sync_parser.add_argument('MERAKI_DASHBOARD_API_KEY',type=str,location="json",help="replacement meraki dashbaord key")
def initialize():
    global data
    global tasks
    data = {}
    data['master_pid'] = os.getpid()
    data['global_data'] = "This is global data"
    data['multiprocess_value'] = Value('d', 0.0)
    data['multiprocess_array'] = Array('i', range(5))
    manager_dict = Manager().dict()
    manager_dict['manager_key'] = 'manager_value'
    data['multiprocess_manager'] = manager_dict
 


def create_first_token(app):
    
    test_client = app.test_client()
    with app.test_request_context():
        token = create_access_token(uuid.uuid4().node)
        idenity = decode_token(token)
        print(f"Token Idenity: {idenity}")
        print(f"Current Access Token is: {token}")
        
        
@app.before_first_request
def before_first_request():
    """Start a background thread that cleans up old tasks."""
    def clean_old_tasks():
        """
        This function cleans up old tasks from our in-memory data structure.
        """
        global tasks
        while True:
            # Only keep tasks that are running or that finished less than 5
            # minutes ago.
            five_min_ago = datetime.timestamp(datetime.utcnow()) - 5 * 60
            tasks = {task_id: task for task_id, task in tasks.items()
                     if 'completion_timestamp' not in task or task['completion_timestamp'] > five_min_ago}
            time.sleep(60)

    if not current_app.config['TESTING']:
        thread = threading.Thread(target=clean_old_tasks)
        thread.start()


def async_api(wrapped_function):
    global tasks
    
    @wraps(wrapped_function)
    def new_function(*args, **kwargs):
        def task_call(flask_app, environ):
           
            # Create a request context similar to that of the original request
            # so that the task can have access to flask.g, flask.request, etc.
            with flask_app.request_context(environ):
                try:
                    #values = sync_parser.parse_args()
                    #request_data = Request(environ)
                    tasks[task_id]['return_value'] = wrapped_function(*args, **kwargs)
                except HTTPException as e:
                    tasks[task_id]['return_value'] = current_app.handle_http_exception(e)
                except Exception as e:
                    # The function raised an exception, so we set a 500 error
                    tasks[task_id]['return_value'] = InternalServerError()
                    if current_app.debug:
                        # We want to find out if something happened so reraise
                        raise
                finally:
                    # We record the time of the response, to help in garbage
                    # collecting old tasks
                    tasks[task_id]['completion_timestamp'] = datetime.timestamp(datetime.utcnow())

                    # close the database session (if any)

        # Assign an id to the asynchronous task
        task_id = uuid.uuid4().hex

        # Record the task, and then launch it
        tasks[task_id] = {'task_thread': threading.Thread(
            target=task_call, args=(current_app._get_current_object(),
                               request.environ))}
        tasks[task_id]['task_thread'].start()

        # Return a 202 response, with a link that the client can use to
        # obtain task status
        print(url_for('gettaskstatus', task_id=task_id))
        #return jsonify()f"ccepted location {url_for('gettaskstatus', task_id=task_id)}", 202, {'Location': url_for('gettaskstatus', task_id=task_id)}
        return make_response(jsonify({"message": "Proccess Accepted",
                                      "status": 202,
                                      "status url": url_for('gettaskstatus', task_id=task_id)}),
                             202,
                             {'Location': url_for('gettaskstatus', task_id=task_id)})
    return new_function


class GetTaskStatus(Resource):
    global tasks
    @jwt_required()
    def get(self, task_id):
        """
        Return status about an asynchronous task. If this request returns a 202
        status code, it means that task hasn't finished yet. Else, the response
        from the task is returned.
        """
        task = tasks.get(task_id)
        if task is None:
            abort(404)
        if 'return_value' not in task:
            #return "Sync Still Running", 202, {'Location': url_for('gettaskstatus', task_id=task_id)}
            return make_response(jsonify({"message" : "Sync Still Running",
                                          "status" : 202,
                                          "status url": url_for(
                                              'gettaskstatus',
                                              task_id=task_id)}),
                                 202,
                                 {'Location': url_for('gettaskstatus',
                                                      task_id=task_id)})
        return make_response(jsonify({"message" : task["return_value"],
                                          "status" : 200}),
                                 202)


class CatchAll(Resource):
    @jwt_required()
    @async_api
    def get(self, path=''):
        # perform some intensive processing
        print("starting processing task, path: '%s'" % path)
        time.sleep(10)
        print("completed processing task, path: '%s'" % path)
        return f'The answer is: {path}'

class Sync(Resource):
    def __init__(self):
        self.values = sync_parser.parse_args()
        self.config_coverride = {
                                    'network_tags': self.values["network_tags"],
	                                'MERAKI_DASHBOARD_API_KEY': self.values["MERAKI_DASHBOARD_API_KEY"]
                               }

    @jwt_required()
    @async_api
    def post(self):
        # perform some intensive processing
        config_file = getenv("MERAKI_TOOLS_CONFIG", None)
        config_overide ={}
        if config_file is None:
            return "No Config Filed Defined"
        finish = run(config_file,task='sync',network_name=self.values["network_name"],config_overide=self.config_coverride)
        #run(config_file, task='sync')
        print("starting processing task")
        time.sleep(10)
        print("completed processing task")
        return finish

api.add_resource(CatchAll, '/<path:path>', '/')
api.add_resource(GetTaskStatus, '/status/<task_id>')
api.add_resource(Sync,'/sync')
create_first_token(app)

if __name__ == '__main__':
    app.run(debug=True)