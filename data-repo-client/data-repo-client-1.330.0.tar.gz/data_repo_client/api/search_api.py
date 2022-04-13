# coding: utf-8

"""
    Data Repository API

    <details><summary>This document defines the REST API for the Terra Data Repository.</summary> <p> **Status: design in progress** There are a few top-level endpoints (besides some used by swagger):  * / - generated by swagger: swagger API page that provides this documentation and a live UI for submitting REST requests  * /status - provides the operational status of the service  * /configuration - provides the basic configuration and information about the service  * /api - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The API endpoints are organized by interface. Each interface is separately versioned. <p> **Notes on Naming** <p> All of the reference items are suffixed with \\\"Model\\\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. </details>   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from data_repo_client.api_client import ApiClient
from data_repo_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_search_index(self, id, search_index_request, **kwargs):  # noqa: E501
        """create_search_index  # noqa: E501

        Create a new search index for a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_search_index(id, search_index_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param SearchIndexRequest search_index_request: Index to create from SQL (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SearchIndexModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_search_index_with_http_info(id, search_index_request, **kwargs)  # noqa: E501

    def create_search_index_with_http_info(self, id, search_index_request, **kwargs):  # noqa: E501
        """create_search_index  # noqa: E501

        Create a new search index for a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_search_index_with_http_info(id, search_index_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param SearchIndexRequest search_index_request: Index to create from SQL (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SearchIndexModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'search_index_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_search_index" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `create_search_index`")  # noqa: E501
        # verify the required parameter 'search_index_request' is set
        if self.api_client.client_side_validation and ('search_index_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['search_index_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `search_index_request` when calling `create_search_index`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_index_request' in local_var_params:
            body_params = local_var_params['search_index_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['googleoauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/repository/v1/search/{id}/index', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchIndexModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_search_metadata(self, id, **kwargs):  # noqa: E501
        """delete_search_metadata  # noqa: E501

        Delete search metadata for a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_search_metadata(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_search_metadata_with_http_info(id, **kwargs)  # noqa: E501

    def delete_search_metadata_with_http_info(self, id, **kwargs):  # noqa: E501
        """delete_search_metadata  # noqa: E501

        Delete search metadata for a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_search_metadata_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_search_metadata" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_search_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['googleoauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/repository/v1/search/{id}/metadata', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enumerate_snapshot_search(self, **kwargs):  # noqa: E501
        """enumerate_snapshot_search  # noqa: E501

        Returns metadata for all snapshots a user has access to   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enumerate_snapshot_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SearchMetadataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.enumerate_snapshot_search_with_http_info(**kwargs)  # noqa: E501

    def enumerate_snapshot_search_with_http_info(self, **kwargs):  # noqa: E501
        """enumerate_snapshot_search  # noqa: E501

        Returns metadata for all snapshots a user has access to   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enumerate_snapshot_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SearchMetadataResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enumerate_snapshot_search" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['googleoauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/repository/v1/search/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchMetadataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lookup_snapshot_preview_by_id(self, id, table, **kwargs):  # noqa: E501
        """lookup_snapshot_preview_by_id  # noqa: E501

        Retrieve data for a table in a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_snapshot_preview_by_id(id, table, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param str table: Name of table to get data from (required)
        :param int offset: The number of rows to skip when retrieving the next page
        :param int limit: The number of rows to return for the data
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SnapshotPreviewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.lookup_snapshot_preview_by_id_with_http_info(id, table, **kwargs)  # noqa: E501

    def lookup_snapshot_preview_by_id_with_http_info(self, id, table, **kwargs):  # noqa: E501
        """lookup_snapshot_preview_by_id  # noqa: E501

        Retrieve data for a table in a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_snapshot_preview_by_id_with_http_info(id, table, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param str table: Name of table to get data from (required)
        :param int offset: The number of rows to skip when retrieving the next page
        :param int limit: The number of rows to return for the data
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SnapshotPreviewModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'table',
            'offset',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lookup_snapshot_preview_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `lookup_snapshot_preview_by_id`")  # noqa: E501
        # verify the required parameter 'table' is set
        if self.api_client.client_side_validation and ('table' not in local_var_params or  # noqa: E501
                                                        local_var_params['table'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `table` when calling `lookup_snapshot_preview_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `lookup_snapshot_preview_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `lookup_snapshot_preview_by_id`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `lookup_snapshot_preview_by_id`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'table' in local_var_params:
            path_params['table'] = local_var_params['table']  # noqa: E501

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['googleoauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/repository/v1/snapshots/{id}/data/{table}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotPreviewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_search_indices(self, search_query_request, **kwargs):  # noqa: E501
        """query_search_indices  # noqa: E501

        Run a query on the metadata of one or more snapshots  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_search_indices(search_query_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SearchQueryRequest search_query_request: Search query to run against one or more snapshots (required)
        :param int offset: The number of results to skip before retrieving the next page
        :param int limit: The number of search results to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SearchQueryResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.query_search_indices_with_http_info(search_query_request, **kwargs)  # noqa: E501

    def query_search_indices_with_http_info(self, search_query_request, **kwargs):  # noqa: E501
        """query_search_indices  # noqa: E501

        Run a query on the metadata of one or more snapshots  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_search_indices_with_http_info(search_query_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SearchQueryRequest search_query_request: Search query to run against one or more snapshots (required)
        :param int offset: The number of results to skip before retrieving the next page
        :param int limit: The number of search results to return
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SearchQueryResultModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'search_query_request',
            'offset',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_search_indices" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'search_query_request' is set
        if self.api_client.client_side_validation and ('search_query_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['search_query_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `search_query_request` when calling `query_search_indices`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_query_request' in local_var_params:
            body_params = local_var_params['search_query_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['googleoauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/repository/v1/search/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchQueryResultModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_search_metadata(self, id, body, **kwargs):  # noqa: E501
        """upsert_search_metadata  # noqa: E501

        Insert or update search metadata for a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_search_metadata(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param str body: Search metadata to upsert on a snapshot (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SearchMetadataModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_search_metadata_with_http_info(id, body, **kwargs)  # noqa: E501

    def upsert_search_metadata_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """upsert_search_metadata  # noqa: E501

        Insert or update search metadata for a snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_search_metadata_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A UUID to used to identify an object in the repository (required)
        :param str body: Search metadata to upsert on a snapshot (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SearchMetadataModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_search_metadata" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `upsert_search_metadata`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `upsert_search_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['googleoauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/repository/v1/search/{id}/metadata', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchMetadataModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
