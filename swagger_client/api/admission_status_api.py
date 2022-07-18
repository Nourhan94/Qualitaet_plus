# coding: utf-8

"""
    Student-Management-System-API

    The Student-Management-System-API. <a href='http://147.172.178.30:8080/stmgmt/api-json'>JSON</a>  # noqa: E501

    OpenAPI spec version: 2.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AdmissionStatusApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_admission_status_of_participant(self, course_id, user_id, **kwargs):  # noqa: E501
        """Get admission status.  # noqa: E501

        Returns the admission status of all participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admission_status_of_participant(course_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param str user_id: (required)
        :return: AdmissionStatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admission_status_of_participant_with_http_info(course_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admission_status_of_participant_with_http_info(course_id, user_id, **kwargs)  # noqa: E501
            return data

    def get_admission_status_of_participant_with_http_info(self, course_id, user_id, **kwargs):  # noqa: E501
        """Get admission status.  # noqa: E501

        Returns the admission status of all participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admission_status_of_participant_with_http_info(course_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param str user_id: (required)
        :return: AdmissionStatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admission_status_of_participant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_admission_status_of_participant`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_admission_status_of_participant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/courses/{courseId}/admission-status/{userId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdmissionStatusDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admission_status_of_participants(self, course_id, **kwargs):  # noqa: E501
        """Get admission status.  # noqa: E501

        Returns the admission status of all participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admission_status_of_participants(course_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :return: list[AdmissionStatusDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admission_status_of_participants_with_http_info(course_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admission_status_of_participants_with_http_info(course_id, **kwargs)  # noqa: E501
            return data

    def get_admission_status_of_participants_with_http_info(self, course_id, **kwargs):  # noqa: E501
        """Get admission status.  # noqa: E501

        Returns the admission status of all participants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admission_status_of_participants_with_http_info(course_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :return: list[AdmissionStatusDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admission_status_of_participants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_admission_status_of_participants`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/courses/{courseId}/admission-status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AdmissionStatusDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_points_overview(self, course_id, **kwargs):  # noqa: E501
        """Get points overview.  # noqa: E501

        Returns an overview of the achieved points of all students mapped the assignments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_points_overview(course_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :return: PointsOverviewDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_points_overview_with_http_info(course_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_points_overview_with_http_info(course_id, **kwargs)  # noqa: E501
            return data

    def get_points_overview_with_http_info(self, course_id, **kwargs):  # noqa: E501
        """Get points overview.  # noqa: E501

        Returns an overview of the achieved points of all students mapped the assignments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_points_overview_with_http_info(course_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :return: PointsOverviewDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_points_overview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_points_overview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/courses/{courseId}/admission-status/overview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PointsOverviewDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_points_overview_of_student(self, course_id, user_id, **kwargs):  # noqa: E501
        """Get points overview of student.  # noqa: E501

        Returns an overview of the achieved points of a student mapped the assignments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_points_overview_of_student(course_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param str user_id: (required)
        :return: PointsOverviewDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_points_overview_of_student_with_http_info(course_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_points_overview_of_student_with_http_info(course_id, user_id, **kwargs)  # noqa: E501
            return data

    def get_points_overview_of_student_with_http_info(self, course_id, user_id, **kwargs):  # noqa: E501
        """Get points overview of student.  # noqa: E501

        Returns an overview of the achieved points of a student mapped the assignments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_points_overview_of_student_with_http_info(course_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param str user_id: (required)
        :return: PointsOverviewDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_points_overview_of_student" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_points_overview_of_student`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_points_overview_of_student`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/courses/{courseId}/admission-status/overview/{userId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PointsOverviewDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
