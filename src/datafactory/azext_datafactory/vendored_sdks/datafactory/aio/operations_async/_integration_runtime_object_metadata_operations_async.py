# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class IntegrationRuntimeObjectMetadataOperations:
    """IntegrationRuntimeObjectMetadataOperations async operations.

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

    async def _refresh_initial(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        **kwargs
    ) -> "models.SsisObjectMetadataStatusResponse":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SsisObjectMetadataStatusResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-06-01"

        # Construct URL
        url = self._refresh_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'integrationRuntimeName': self._serialize.url("integration_runtime_name", integration_runtime_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SsisObjectMetadataStatusResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _refresh_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/refreshObjectMetadata'}

    async def refresh(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        **kwargs
    ) -> "models.SsisObjectMetadataStatusResponse":
        """Refresh a SSIS integration runtime object metadata.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name.
        :type integration_runtime_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns SsisObjectMetadataStatusResponse
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.datafactory.models.SsisObjectMetadataStatusResponse]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SsisObjectMetadataStatusResponse"]
        raw_result = await self._refresh_initial(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            integration_runtime_name=integration_runtime_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('SsisObjectMetadataStatusResponse', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    refresh.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/refreshObjectMetadata'}

    async def get(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        metadata_path: Optional[str] = None,
        **kwargs
    ) -> "models.SsisObjectMetadataListResponse":
        """Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name.
        :type integration_runtime_name: str
        :param metadata_path: Metadata path.
        :type metadata_path: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SsisObjectMetadataListResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SsisObjectMetadataListResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SsisObjectMetadataListResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _get_metadata_request = models.GetSsisObjectMetadataRequest(metadata_path=metadata_path)
        api_version = "2018-06-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'integrationRuntimeName': self._serialize.url("integration_runtime_name", integration_runtime_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if _get_metadata_request is not None:
            body_content = self._serialize.body(_get_metadata_request, 'GetSsisObjectMetadataRequest')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SsisObjectMetadataListResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getObjectMetadata'}
