# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 54.3.2-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from ..models import *

class PluginsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_plugin(self, **kwargs):
        """
        Delete a plugin
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_plugin(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID of the plugin (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_plugin_with_http_info(**kwargs)
        else:
            (data) = self.delete_plugin_with_http_info(**kwargs)
            return data

    def delete_plugin_with_http_info(self, **kwargs):
        """
        Delete a plugin
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_plugin_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID of the plugin (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_plugin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_plugin`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/plugins/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StatusMessageBase',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_file(self, **kwargs):
        """
        Get a plugin file
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file(id=id_value, file_name=file_name_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID of the plugin (required)
        :param str file_name: The name of the file from the plugin (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_file_with_http_info(**kwargs)
        else:
            (data) = self.get_file_with_http_info(**kwargs)
            return data

    def get_file_with_http_info(self, **kwargs):
        """
        Get a plugin file
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_with_http_info(id=id_value, file_name=file_name_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID of the plugin (required)
        :param str file_name: The name of the file from the plugin (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        all_params = ['id', 'file_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_file`")
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params) or (params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `get_file`")

        if 'file_name' in params and not re.search('.+', params['file_name']):
            raise ValueError("Invalid value for parameter `file_name` when calling `get_file`, must conform to the pattern `/.+/`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/plugins/{id}/files/{fileName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_plugins(self, **kwargs):
        """
        Get a collection of plugins
        Pagination is enabled for this query
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_plugins(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name_search: Search text by which to filter plugins' names.
        :param str identifier_search: Search text by which to filter plugins' identifiers.
        :param str category_search: Search text by which to filter plugins' categories.
        :param str sort_order: A field by which to order the plugins followed by a space and 'asc' or 'desc'. Field name can be one of: name, identifier, category
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :return: PluginOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PluginOutputListV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_plugins_with_http_info(**kwargs)
        else:
            (data) = self.get_plugins_with_http_info(**kwargs)
            return data

    def get_plugins_with_http_info(self, **kwargs):
        """
        Get a collection of plugins
        Pagination is enabled for this query
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_plugins_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name_search: Search text by which to filter plugins' names.
        :param str identifier_search: Search text by which to filter plugins' identifiers.
        :param str category_search: Search text by which to filter plugins' categories.
        :param str sort_order: A field by which to order the plugins followed by a space and 'asc' or 'desc'. Field name can be one of: name, identifier, category
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :return: PluginOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PluginOutputListV1
        """

        all_params = ['name_search', 'identifier_search', 'category_search', 'sort_order', 'offset', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plugins" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name_search' in params:
            query_params.append(('nameSearch', params['name_search']))
        if 'identifier_search' in params:
            query_params.append(('identifierSearch', params['identifier_search']))
        if 'category_search' in params:
            query_params.append(('categorySearch', params['category_search']))
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/plugins', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PluginOutputListV1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_sdk(self, **kwargs):
        """
        Get an SDK file
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sdk(file_name=file_name_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_name: The name of the file from the plugin (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sdk_with_http_info(**kwargs)
        else:
            (data) = self.get_sdk_with_http_info(**kwargs)
            return data

    def get_sdk_with_http_info(self, **kwargs):
        """
        Get an SDK file
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sdk_with_http_info(file_name=file_name_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_name: The name of the file from the plugin (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        all_params = ['file_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sdk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params) or (params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `get_sdk`")

        if 'file_name' in params and not re.search('.+', params['file_name']):
            raise ValueError("Invalid value for parameter `file_name` when calling `get_sdk`, must conform to the pattern `/.+/`")

        collection_formats = {}

        path_params = {}
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/plugins/sdk/{fileName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def upload_plugin(self, **kwargs):
        """
        Upload a plugin
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_plugin(file=file_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: Plugin to upload (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.upload_plugin_with_http_info(**kwargs)
        else:
            (data) = self.upload_plugin_with_http_info(**kwargs)
            return data

    def upload_plugin_with_http_info(self, **kwargs):
        """
        Upload a plugin
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_plugin_with_http_info(file=file_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: Plugin to upload (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
        """

        all_params = ['file']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_plugin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `upload_plugin`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/plugins', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StatusMessageBase',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
