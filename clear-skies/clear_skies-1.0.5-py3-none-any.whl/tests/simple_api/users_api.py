import clearskies
from . import models

users_api = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        'authentication':
        clearskies.authentication.public(),
        'routes': [
            {
                'path': 'users',
                'handler_class': clearskies.handlers.RestfulAPI,
                'handler_config': {
                    'model_class': models.User,
                    'readable_columns': ['status_id', 'name', 'email', 'created', 'updated'],
                    'writeable_columns': ['status_id', 'name', 'email'],
                    'searchable_columns': ['status_id', 'name', 'email'],
                    'default_sort_column': 'name',
                },
            },
            {
                'path': 'statuses',
                'handler_class': clearskies.handlers.RestfulAPI,
                'handler_config': {
                    'model_class': models.Status,
                    'read_only': True,
                    'readable_columns': ['name', 'users'],
                    'searchable_columns': ['name', 'users'],
                    'default_sort_column': 'name',
                },
            },
        ],
    },
)
