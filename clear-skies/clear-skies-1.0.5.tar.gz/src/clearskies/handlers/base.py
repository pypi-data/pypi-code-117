from abc import ABC, abstractmethod
from .exceptions import ClientError, InputError
from collections import OrderedDict
import inspect
import re
from ..autodoc.schema import Integer as AutoDocInteger
from ..autodoc.schema import String as AutoDocString
from ..autodoc.schema import Object as AutoDocObject
from ..autodoc.response import Response as AutoDocResponse
from ..functional import string
from typing import List, Dict
class Base(ABC):
    _configuration = None
    _configuration_defaults = {}
    _global_configuration_defaults = {
        'base_url': '',
        'response_headers': None,
        'authentication': None,
        'authorization': None,
        'output_map': None,
        'column_overrides': None,
        'id_column_name': None,
        'doc_description': '',
        'internal_casing': '',
        'external_casing': '',
    }
    _di = None
    _configuration = None

    def __init__(self, di):
        self._di = di
        self._configuration = None

    @abstractmethod
    def handle(self):
        pass

    def configure(self, configuration):
        for key in configuration.keys():
            if key not in self._configuration_defaults and key not in self._global_configuration_defaults:
                class_name = self.__class__.__name__
                raise KeyError(f"Attempt to set unknown configuration setting '{key}' for handler '{class_name}'")

        self._check_configuration(configuration)
        self._configuration = self._finalize_configuration(self.apply_default_configuation(configuration))

    def _check_configuration(self, configuration):
        if not 'authentication' in configuration:
            raise KeyError(
                f"You must provide authentication in the configuration for handler '{self.__class__.__name__}'"
            )
        if configuration.get('authorization', None):
            if not callable(configuration['authorization']) and not isinstance(configuration['authorization'], dict):
                raise ValueError("'authorization' should be a callable or a dictionary with subclaims to enforce")
        if configuration.get('output_map') is not None:
            if not callable(configuration['output_map']):
                raise ValueError("'output_map' should be a callable")
            signature = inspect.getfullargspec(configuration['output_map'])
            if signature.defaults and len(signature.defaults):
                raise ValueError(
                    "'output_map' should be a callable that accepts one parameter: the model. " + \
                    "However, the provided one accepts kwargs"
                )
            if len(signature.args) != 1:
                raise ValueError(
                    "'output_map' should be a callable that accepts one parameter: the model. " + \
                    f"However, the provided one accepts {len(signature.args)}"
                )
        number_casings = 0
        internal_casing = configuration.get('internal_casing')
        if internal_casing and internal_casing not in string.casings:
            raise ValueError(
                f"Invalid internal_casing config for handler '{self.__class__.__name__}': expected one of " + \
                "'" + ", '".join(string.casings) + f"' but found '{internal_casing}'"
            )
            number_casings += 1
        external_casing = configuration.get('external_casing')
        if external_casing and external_casing not in string.casings:
            raise ValueError(
                f"Invalid external_casing config for handler '{self.__class__.__name__}': expected one of " + \
                "'" + ", '".join(string.casings) + f"' but found '{external_casing}'"
            )
            number_casings += 1
        if number_casings == 1:
            raise ValueError(
                f"Configuration error for handler '{self.__class__.__name__}': external_casing and internal_casing" + \
                " must be specified together, but only one was found"
            )

    def apply_default_configuation(self, configuration):
        return {
            **self._global_configuration_defaults,
            **self._configuration_defaults,
            **configuration,
        }

    def configuration(self, key):
        if self._configuration is None:
            raise ValueError("Cannot fetch configuration values before setting the configuration")
        if key not in self._configuration:
            class_name = self.__class__.__name__
            raise KeyError(f"Configuration key '{key}' does not exist for handler '{class_name}'")
        return self._configuration[key]

    def _finalize_configuration(self, configuration):
        configuration['authentication'] = self._di.build(configuration['authentication'])
        return configuration

    def __call__(self, input_output):
        if self._configuration is None:
            raise ValueError("Must configure handler before calling")
        authentication = self._configuration.get('authentication')
        if authentication:
            try:
                if not authentication.authenticate(input_output):
                    return self.error(input_output, 'Not Authenticated', 401)
            except ClientError as client_error:
                return self.error(input_output, str(client_error), 401)
            authorization = self._configuration.get('authorization')
            if authorization:
                try:
                    if not authentication.authorize(authorization):
                        return self.error(input_output, 'Not Authorized', 403)
                except ClientError as client_error:
                    return self.error(input_output, str(client_error), 403)

        try:
            response = self.handle(input_output)
        except ClientError as client_error:
            return self.error(input_output, str(client_error), 400)
        except InputError as input_error:
            return self.input_errors(input_output, input_error.errors)

        return response

    def input_errors(self, input_output, errors, status_code=200):
        return self.respond(input_output, {'status': 'input_errors', 'input_errors': errors}, status_code)

    def error(self, input_output, message, status_code):
        return self.respond(input_output, {'status': 'client_error', 'error': message}, status_code)

    def success(self, input_output, data, number_results=None, limit=None, next_page=None):
        response_data = {'status': 'success', 'data': data, 'pagination': {}}

        if number_results is not None:
            for value in [number_results, limit]:
                if value is not None and type(value) != int:
                    raise ValueError("number_results and limit must all be integers")

            response_data['pagination'] = {
                'number_results': number_results,
                'limit': limit,
                'next_page': next_page,
            }

        return self.respond(input_output, response_data, 200)

    def respond(self, input_output, response_data, status_code):
        response_headers = self.configuration('response_headers')
        if response_headers:
            input_output.set_headers(response_headers)
        return input_output.respond(self._normalize_response(response_data), status_code)

    def _normalize_response(self, response_data):
        if not 'status' in response_data:
            raise ValueError("Huh, status got left out somehow")
        return {
            self.auto_case_internal_column_name('status'):
            self.auto_case_internal_column_name(response_data['status']),
            self.auto_case_internal_column_name('error'):
            response_data.get('error', ''),
            self.auto_case_internal_column_name('data'):
            response_data.get('data', []),
            self.auto_case_internal_column_name('pagination'):
            self._normalize_pagination(response_data.get('pagination', {})),
            self.auto_case_internal_column_name('input_errors'):
            response_data.get('input_errors', {})
        }

    def _normalize_pagination(self, pagination):
        # pagination isn't always relevant so if it is completely empty then leave it that way
        if not pagination:
            return pagination
        return {
            self.auto_case_internal_column_name('number_results'): pagination.get('number_results', 0),
            self.auto_case_internal_column_name('limit'): pagination.get('limit', 0),
            self.auto_case_internal_column_name('next_page'): {
                self.auto_case_internal_column_name(key): value
                for (key, value) in pagination.get('next_page', {}).items()
            },
        }

    def _model_as_json(self, model):
        if self.configuration('output_map'):
            return self.configuration('output_map')(model)

        model_id = getattr(model, self.id_column_name)
        json = OrderedDict()
        json[self.auto_case_internal_column_name('id')] = model_id
        for column in self._get_readable_columns().values():
            json[self.auto_case_column_name(column.name, True)] = column.to_json(model)
        return json

    def auto_case_internal_column_name(self, column_name):
        if self._configuration['external_casing']:
            return string.swap_casing(column_name, 'snake_case', self._configuration['external_casing'])
        return column_name

    def auto_case_to_internal_column_name(self, column_name):
        if self._configuration['external_casing']:
            return string.swap_casing(column_name, self._configuration['external_casing'], 'snake_case')
        return column_name

    def auto_case_column_name(self, column_name, internal_to_external):
        if not self._configuration['internal_casing']:
            return column_name
        if internal_to_external:
            return string.swap_casing(
                column_name,
                self._configuration['internal_casing'],
                self._configuration['external_casing'],
            )
        return string.swap_casing(
            column_name,
            self._configuration['external_casing'],
            self._configuration['internal_casing'],
        )

    @property
    def id_column_name(self) -> str:
        """
        This returns the name of the id column to use for requests

        There are three ways to determine the id column:

         1. It may be defined in the handler configuration.
         2. It may be overridden in the model class
         3. It defaults to 'id'

        The first happens if the developer wants to expose a different "id" column to the client.
        The second happens if the developer wants to use a different id column internally.
        The third is the clearskies default.

        The first is easy to detect because the dev will set `id_column_name` in the handler config.
        The second happens if the model class defines a different `id_column_name` property in the model class.
        However, this is tricky because there is nothing in this base case that allows us to pull up the model.
        In fact, not all handlers use a model, or they may use multiple models, etc...  Still, it's pretty
        common for the handler to have a configuration named `model_class` or `model`, so let's check for that and assume
        the handler will only ask for the id_column_name() if the handler has a `self.configuration('model_class')`
        """
        id_column_name = self.configuration('id_column_name')
        if id_column_name is not None:
            return id_column_name
        if not self._configuration.get('model_class', False) and not self._configuration.get('model', False):
            raise KeyError(
                "To properly use handler.id_column_name, the handler must have a 'model_class' or 'model' configuration key"
            )
        if self._configuration.get('model_class', False):
            return self._configuration.get('model_class').id_column_name
        return self._configuration.get('model').id_column_name

    def documentation(self):
        return []

    def documentation_models(self):
        return {}

    def documentation_pagination_response(self, include_pagination=True):
        if not include_pagination:
            return AutoDocObject(self.auto_case_internal_column_name('pagination'), [], value={})
        return AutoDocObject(
            self.auto_case_internal_column_name('pagination'),
            [
                AutoDocInteger(self.auto_case_internal_column_name('number_results'), example=10),
                AutoDocInteger(self.auto_case_internal_column_name('limit'), example=100),
                AutoDocObject(
                    self.auto_case_internal_column_name('next_page'),
                    self._model.documentation_pagination_next_page_response(self.auto_case_internal_column_name),
                    self._model.documentation_pagination_next_page_example(self.auto_case_internal_column_name),
                )
            ],
        )

    def documentation_success_response(self, data_schema, description='', include_pagination=False):
        return AutoDocResponse(
            200,
            AutoDocObject(
                'body', [
                    AutoDocString(self.auto_case_internal_column_name('status'), value='success'),
                    data_schema,
                    self.documentation_pagination_response(include_pagination=include_pagination),
                    AutoDocString(self.auto_case_internal_column_name('error'), value=''),
                    AutoDocObject(self.auto_case_internal_column_name('input_errors'), [], value={}),
                ]
            ),
            description=description,
        )

    def documentation_generic_error_response(self, description='Invalid Call', status=400):
        return AutoDocResponse(
            status,
            AutoDocObject(
                'body', [
                    AutoDocString(self.auto_case_internal_column_name('status'), value='error'),
                    AutoDocObject(self.auto_case_internal_column_name('data'), [], value={}),
                    self.documentation_pagination_response(include_pagination=False),
                    AutoDocString(self.auto_case_internal_column_name('error'), example='User readable error message'),
                    AutoDocObject(self.auto_case_internal_column_name('input_errors'), [], value={}),
                ]
            ),
            description=description
        )

    def documentation_input_error_response(self, description='Invalid client-side input'):
        email_example = self.auto_case_internal_column_name('email')
        return AutoDocResponse(
            200,
            AutoDocObject(
                'body', [
                    AutoDocString(self.auto_case_internal_column_name('status'), value='input_errors'),
                    AutoDocObject(self.auto_case_internal_column_name('data'), [], value={}),
                    self.documentation_pagination_response(include_pagination=False),
                    AutoDocString(self.auto_case_internal_column_name('error'), value=''),
                    AutoDocObject(
                        self.auto_case_internal_column_name('input_errors'),
                        [AutoDocString('[COLUMN_NAME]', example='User friendly error message')],
                        example={email_example: f'{email_example} was not a valid email address'}
                    ),
                ]
            ),
            description=description
        )

    def documentation_access_denied_response(self):
        return self.documentation_generic_error_response(description='Access Denied', status=401)

    def documentation_unauthorized_response(self):
        return self.documentation_generic_error_response(description='Unauthorized', status=403)

    def documentation_not_found(self):
        return self.documentation_generic_error_response(description='Not Found', status=404)

    def documentation_data_schema(self):
        id_column_name = self.id_column_name
        properties = [
            self._columns[id_column_name].documentation(name=self.auto_case_internal_column_name('id'))
            if id_column_name in self._columns else AutoDocString(self.auto_case_internal_column_name('id'))
        ]

        for column in self._get_readable_columns().values():
            column_doc = column.documentation()
            column_doc.name = self.auto_case_internal_column_name(column_doc.name)
            properties.append(column_doc)

        return properties
