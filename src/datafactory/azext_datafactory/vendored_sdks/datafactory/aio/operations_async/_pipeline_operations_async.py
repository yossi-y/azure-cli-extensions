# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PipelineOperations:
    """PipelineOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datafactory.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        **kwargs
    ) -> "models.PipelineListResponse":
        """Lists pipelines.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineListResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.PipelineListResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PipelineListResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-06-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_factory.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PipelineListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_factory.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines'}

    async def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        pipeline_name: str,
        if_match: Optional[str] = None,
        description: Optional[str] = None,
        activities: Optional[List["Activity"]] = None,
        parameters: Optional[Dict[str, "ParameterSpecification"]] = None,
        variables: Optional[Dict[str, "VariableSpecification"]] = None,
        concurrency: Optional[int] = None,
        annotations: Optional[List[str]] = None,
        run_dimensions: Optional[Dict[str, object]] = None,
        folder: Optional["models.PipelineFolder"] = None,
        **kwargs
    ) -> "models.PipelineResource":
        """Creates or updates a pipeline.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :param if_match: ETag of the pipeline entity.  Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update.
        :type if_match: str
        :param description: The description of the pipeline.
        :type description: str
        :param activities: List of activities in pipeline.
        :type activities: list[~azure.mgmt.datafactory.models.Activity]
        :param parameters: List of parameters for pipeline.
        :type parameters: dict[str, ~azure.mgmt.datafactory.models.ParameterSpecification]
        :param variables: List of variables for pipeline.
        :type variables: dict[str, ~azure.mgmt.datafactory.models.VariableSpecification]
        :param concurrency: The max number of concurrent runs for the pipeline.
        :type concurrency: int
        :param annotations: List of tags that can be used for describing the Pipeline.
        :type annotations: list[str]
        :param run_dimensions: Dimensions emitted by Pipeline.
        :type run_dimensions: dict[str, object]
        :param folder: The folder that this Pipeline is in. If not specified, Pipeline will appear at
         the root level.
        :type folder: ~azure.mgmt.datafactory.models.PipelineFolder
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.PipelineResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PipelineResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _pipeline = models.PipelineResource(description=description, activities=activities, parameters=parameters, variables=variables, concurrency=concurrency, annotations=annotations, run_dimensions=run_dimensions, folder=folder)
        api_version = "2018-06-01"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_pipeline, 'PipelineResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PipelineResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName}'}

    async def get(
        self,
        resource_group_name: str,
        factory_name: str,
        pipeline_name: str,
        if_none_match: Optional[str] = None,
        **kwargs
    ) -> "models.PipelineResource":
        """Gets a pipeline.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :param if_none_match: ETag of the pipeline entity. Should only be specified for get. If the
         ETag matches the existing entity tag, or if * was provided, then no content will be returned.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.PipelineResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PipelineResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-06-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PipelineResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName}'}

    async def delete(
        self,
        resource_group_name: str,
        factory_name: str,
        pipeline_name: str,
        **kwargs
    ) -> None:
        """Deletes a pipeline.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-06-01"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName}'}

    async def create_run(
        self,
        resource_group_name: str,
        factory_name: str,
        pipeline_name: str,
        reference_pipeline_run_id: Optional[str] = None,
        is_recovery: Optional[bool] = None,
        start_activity_name: Optional[str] = None,
        start_from_failure: Optional[bool] = None,
        parameters: Optional[Dict[str, object]] = None,
        **kwargs
    ) -> "models.CreateRunResponse":
        """Creates a run of a pipeline.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :param reference_pipeline_run_id: The pipeline run identifier. If run ID is specified the
         parameters of the specified run will be used to create a new run.
        :type reference_pipeline_run_id: str
        :param is_recovery: Recovery mode flag. If recovery mode is set to true, the specified
         referenced pipeline run and the new run will be grouped under the same groupId.
        :type is_recovery: bool
        :param start_activity_name: In recovery mode, the rerun will start from this activity. If not
         specified, all activities will run.
        :type start_activity_name: str
        :param start_from_failure: In recovery mode, if set to true, the rerun will start from failed
         activities. The property will be used only if startActivityName is not specified.
        :type start_from_failure: bool
        :param parameters: Parameters of the pipeline run. These parameters will be used only if the
         runId is not specified.
        :type parameters: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CreateRunResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.CreateRunResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CreateRunResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-06-01"

        # Construct URL
        url = self.create_run.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if reference_pipeline_run_id is not None:
            query_parameters['referencePipelineRunId'] = self._serialize.query("reference_pipeline_run_id", reference_pipeline_run_id, 'str')
        if is_recovery is not None:
            query_parameters['isRecovery'] = self._serialize.query("is_recovery", is_recovery, 'bool')
        if start_activity_name is not None:
            query_parameters['startActivityName'] = self._serialize.query("start_activity_name", start_activity_name, 'str')
        if start_from_failure is not None:
            query_parameters['startFromFailure'] = self._serialize.query("start_from_failure", start_from_failure, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if parameters is not None:
            body_content = self._serialize.body(parameters, '{object}')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CreateRunResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_run.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName}/createRun'}
