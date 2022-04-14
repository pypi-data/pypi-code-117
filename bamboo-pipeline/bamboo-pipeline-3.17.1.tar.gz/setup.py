# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pipeline',
 'pipeline.builder',
 'pipeline.builder.flow',
 'pipeline.celery',
 'pipeline.component_framework',
 'pipeline.component_framework.components',
 'pipeline.component_framework.components.collections',
 'pipeline.component_framework.management',
 'pipeline.component_framework.management.commands',
 'pipeline.component_framework.migrations',
 'pipeline.components',
 'pipeline.components.collections',
 'pipeline.conf',
 'pipeline.contrib',
 'pipeline.contrib.external_plugins',
 'pipeline.contrib.external_plugins.migrations',
 'pipeline.contrib.external_plugins.models',
 'pipeline.contrib.external_plugins.utils',
 'pipeline.contrib.external_plugins.utils.importer',
 'pipeline.contrib.periodic_task',
 'pipeline.contrib.periodic_task.djcelery',
 'pipeline.contrib.periodic_task.migrations',
 'pipeline.contrib.periodic_task.signals',
 'pipeline.contrib.statistics',
 'pipeline.contrib.statistics.migrations',
 'pipeline.contrib.statistics.signals',
 'pipeline.core',
 'pipeline.core.data',
 'pipeline.core.flow',
 'pipeline.core.flow.activity',
 'pipeline.core.signals',
 'pipeline.django_signal_valve',
 'pipeline.django_signal_valve.migrations',
 'pipeline.engine',
 'pipeline.engine.conf',
 'pipeline.engine.core',
 'pipeline.engine.core.data',
 'pipeline.engine.core.handlers',
 'pipeline.engine.core.handlers.endevent',
 'pipeline.engine.health',
 'pipeline.engine.health.zombie',
 'pipeline.engine.migrations',
 'pipeline.engine.models',
 'pipeline.engine.signals',
 'pipeline.eri',
 'pipeline.eri.celery',
 'pipeline.eri.imp',
 'pipeline.eri.migrations',
 'pipeline.log',
 'pipeline.log.migrations',
 'pipeline.management',
 'pipeline.management.commands',
 'pipeline.migrations',
 'pipeline.parser',
 'pipeline.service',
 'pipeline.service.pipeline_engine_adapter',
 'pipeline.signals',
 'pipeline.templates',
 'pipeline.templates.create_plugins_app',
 'pipeline.utils',
 'pipeline.utils.boolrule',
 'pipeline.utils.mako_utils',
 'pipeline.validators',
 'pipeline.variable_framework',
 'pipeline.variable_framework.management',
 'pipeline.variable_framework.management.commands',
 'pipeline.variable_framework.migrations',
 'pipeline.variable_framework.signals']

package_data = \
{'': ['*']}

install_requires = \
['Django>=2.2,<4.0',
 'Mako>=1.1.4,<2.0.0',
 'Werkzeug>=1.0.0,<2.0.0',
 'bamboo-engine==2.2.1',
 'boto3>=1.9.130,<2.0.0',
 'celery>=4.4.0,<5.0.0',
 'django-celery-beat>=2.1.0,<3.0.0',
 'django-timezone-field>=4.0,<5.0',
 'jsonschema>=2.5.1,<3.0.0',
 'prometheus-client>=0.9.0,<0.10.0',
 'pyparsing>=2.2.0,<3.0.0',
 'pytz==2019.3',
 'redis-py-cluster==2.1.0',
 'redis>=3.2.0,<4.0.0',
 'requests>=2.22.0,<3.0.0',
 'ujson>=4.1.0,<4.2.0']

setup_kwargs = {
    'name': 'bamboo-pipeline',
    'version': '3.17.1',
    'description': 'runtime for bamboo-engine base on Django and Celery',
    'long_description': None,
    'author': 'homholueng',
    'author_email': 'homholueng@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.8',
}


setup(**setup_kwargs)
