# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import asyncio
import json
import uuid
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
import requests

import aiohttp
from typing import Dict, List, Any, Optional
import urllib.parse

from botbuilder.core.inspection import trace_activity
from botbuilder.schema.iactivity import IActivity
from botbuilder.schema.teams._models_py3 import MeetingInfo, TeamsMeetingParticipant
from botbuilder.schema.teams.team_member import TeamMember
from botframework.connector import retry_action
from botframework.connector.auth._throttle_exception import ThrottleException

from ... import models


class TeamsOperations(object):
    """TeamsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_teams_channels(
        self, team_id, custom_headers=None, raw=False, **operation_config
    ):
        """Fetches channel list for a given team.

        Fetch the channel list.

        :param team_id: Team Id
        :type team_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ConversationList or ClientRawResponse if raw=true
        :rtype: ~botframework.connector.teams.models.ConversationList or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_teams_channels.metadata["url"]
        path_format_arguments = {
            "teamId": self._serialize.url("team_id", team_id, "str")
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("ConversationList", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_teams_channels.metadata = {"url": "/v3/teams/{teamId}/conversations"}

    def get_team_details(
        self, team_id, custom_headers=None, raw=False, **operation_config
    ):
        """Fetches details related to a team.

        Fetch details for a team.

        :param team_id: Team Id
        :type team_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TeamDetails or ClientRawResponse if raw=true
        :rtype: ~botframework.connector.teams.models.TeamDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_team_details.metadata["url"]
        path_format_arguments = {
            "teamId": self._serialize.url("team_id", team_id, "str")
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("TeamDetails", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_team_details.metadata = {"url": "/v3/teams/{teamId}"}

    def fetch_participant(
        self,
        meeting_id: str,
        participant_id: str,
        tenant_id: str,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """Fetches Teams meeting participant details.

        :param meeting_id: Teams meeting id
        :type meeting_id: str
        :param participant_id: Teams meeting participant id
        :type participant_id: str
        :param tenant_id: Teams meeting tenant id
        :type tenant_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TeamsMeetingParticipant or ClientRawResponse if raw=true
        :rtype: ~botframework.connector.teams.models.TeamsParticipantChannelAccount or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """

        # Construct URL
        url = self.fetch_participant.metadata["url"]
        path_format_arguments = {
            "meetingId": self._serialize.url("meeting_id", meeting_id, "str"),
            "participantId": self._serialize.url(
                "participant_id", participant_id, "str"
            ),
            "tenantId": self._serialize.url("tenant_id", tenant_id, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("TeamsMeetingParticipant", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    fetch_participant.metadata = {
        "url": "/v1/meetings/{meetingId}/participants/{participantId}?tenantId={tenantId}"
    }

    def fetch_meeting(
        self, meeting_id: str, custom_headers=None, raw=False, **operation_config
    ):
        """Fetch meeting information.

        :param meeting_id: Meeting Id, encoded as a BASE64 string.
        :type meeting_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: MeetingInfo or ClientRawResponse if raw=true
        :rtype: ~botframework.connector.teams.models.MeetingInfo or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """

        # Construct URL
        url = self.fetch_participant.metadata["url"]
        path_format_arguments = {
            "meetingId": self._serialize.url("meeting_id", meeting_id, "str")
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("MeetingInfo", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    fetch_participant.metadata = {"url": "/v1/meetings/{meetingId}"}

    async def fetch_participant_with_http_messages_async(
    meeting_id: str, 
    participant_id: str, 
    tenant_id: str, 
    custom_headers: Dict[str, List[str]] = None, 
    cancellation_token: Any = None
    ) -> TeamsMeetingParticipant:
        if meeting_id is None:
            raise Exception("meeting_id cannot be null")
        if participant_id is None:
            raise Exception("participant_id cannot be null")
        if tenant_id is None:
            raise Exception("tenant_id cannot be null")

        content = {
            "meeting_id": meeting_id,
            "participant_id": participant_id,
            "tenant_id": tenant_id,
        }

        invocation_id = "some_invocation_id"  # Simulating TraceActivity, define this as needed.

        # Construct URL
        url = f"v1/meetings/{urllib.parse.quote(meeting_id)}/participants/{urllib.parse.quote(participant_id)}?tenantId={urllib.parse.quote(tenant_id)}"

        headers = custom_headers if custom_headers else {}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    response.raise_for_status()
                result = await response.json()
                # Assuming TeamsMeetingParticipant can be initialized with a dictionary.
                return TeamsMeetingParticipant(**result)


    class HttpOperationException(Exception):
        def __init__(self, message, request=None, response=None):
            super().__init__(message)
            self.request = request
            self.response = response

    class SerializationException(Exception):
        def __init__(self, message, content, original_exception):
            super().__init__(message)
            self.content = content
            self.original_exception = original_exception


    async def send_message_to_list_of_users_async(activity: IActivity, teams_members: List[TeamMember], tenant_id: str, custom_headers: Dict[str, List[str]] = None, cancellation_token: Any = None) -> str:
        if activity is None:
            raise ValidationException("activity cannot be null")
        
        if len(teams_members) == 0:
            raise Exception("teams_members cannot be empty")
        
        if not tenant_id:
            raise Exception("tenant_id cannot be null or empty")
        
        content = {
            "Members": [member.dict() for member in teams_members],
            "Activity": activity.dict(),
            "TenantId": tenant_id,
        }
    
        invocation_id = trace_activity("SendMessageToListOfUsers", content, cancellation_token)
        api_url = "v3/batch/conversation/users/"
        
        result = await retry_action(
            task=lambda: TeamsOperations.get_response_async(api_url, "POST", invocation_id, content=content, custom_headers=custom_headers, cancellation_token=cancellation_token),
            retry_exception_handler=TeamsOperations.handle_throttling_exception
        )
    
        return result
    
    async def get_response_async(api_url: str, http_method: str, invocation_id: Optional[str], content: Any = None, custom_headers: Optional[Dict[str, List[str]]] = None, continuation_token: Optional[str] = None, cancellation_token: Optional[Any] = None):
        should_trace = invocation_id is not None
        base_url = "https://your-base-url.com/"  # Replace with your base URL
        url = f"{base_url.rstrip('/')}/{api_url.lstrip('/')}"

        if continuation_token:
            url += f"?continuationToken={requests.utils.quote(continuation_token)}"

        headers = custom_headers if custom_headers else {}
        headers['Content-Type'] = 'application/json; charset=utf-8'

        request_content = None
        if content:
            request_content = json.dumps(content)

        try:
            response = None
            if http_method == "POST":
                response = requests.post(url, headers=headers, data=request_content)
            else:
                raise NotImplementedError("Only POST method is implemented")
            
            response.raise_for_status()
            if response.status_code in [200, 201]:
                if response.content:
                    response_content = response.text
                    try:
                        result_body = json.loads(response_content)
                        return result_body
                    except json.JSONDecodeError as ex:
                        raise TeamsOperations.SerializationException("Unable to deserialize the response.", response_content, ex)
            elif response.status_code == 429:
                raise TeamsOperations.ThrottleException()
            else:
                raise TeamsOperations.HttpOperationException(f"Operation returned an invalid status code '{response.status_code}'", request=request_content, response=response.text)

        except requests.HTTPError as http_err:
            raise TeamsOperations.HttpOperationException(f"HTTP error occurred: {http_err}", request=request_content, response=response.text if response else None)
        except Exception as err:
            raise TeamsOperations.HttpOperationException(f"Other error occurred: {err}", request=request_content, response=response.text if response else None)

    async def get_response_async(url: str, http_method: str, invocation_id: str, content: Any = None, custom_headers: Dict[str, List[str]] = None, cancellation_token: asyncio.CancelledError = None) -> MeetingInfo:
        async with aiohttp.ClientSession() as session:
            headers = custom_headers or {}
            async with session.request(http_method, url, json=content, headers=headers) as response:
                if response.status == 200:
                    response_content = await response.json()
                    return MeetingInfo(**response_content)
                else:
                    raise Exception(f"Request failed with status code {response.status}")

    async def fetch_meeting_info_with_http_messages_async(meeting_id: str, custom_headers: Dict[str, List[str]] = None, cancellation_token: asyncio.CancelledError = None) -> MeetingInfo:
        if meeting_id is None:
            raise ValidationException("meetingId cannot be null")

        invocation_id = await trace_activity("FetchMeetingInfo", {"meetingId": meeting_id}, cancellation_token)

        # Construct URL
        url = f"v1/meetings/{meeting_id}"

        return await TeamsOperations.get_response_async(url, "GET", invocation_id, custom_headers=custom_headers, cancellation_token=cancellation_token)

    def handle_throttling_exception(exception: Exception, current_retry_count: int) -> retry_action.RetryParams:
        if isinstance(exception, ThrottleException):
            return exception.retry_params or retry_action.RetryParams.default_back_off(current_retry_count)
        else:
            return retry_action.RetryParams.stop_retrying()


    async def send_meeting_notification_message_async(meeting_id, notification, custom_headers=None, cancellationToken=None):
        if meeting_id is None:
            raise ValueError("Meeting ID cannot be null.")

        invocation_id = await TeamsOperations.trace_activity("SendMeetingNotification", {"meetingId": meeting_id}, cancellationToken)

        # Construct URL
        url = f"v1/meetings/{meeting_id}/notification"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=notification, headers=custom_headers, ssl=False, raise_for_status=True) as response:
                response_body = await response.json()
                return response_body
            
    def trace_activity(operation_name, content, cancellationToken):
        should_trace = True 
        invocation_id = None

        if should_trace:
            tracing_parameters = {}
            for key, value in content.items():
                tracing_parameters[key] = value

            tracing_parameters['cancellationToken'] = cancellationToken

            invocation_id = str(uuid.uuid4())  # Generate a unique invocation ID
            print(f"Entering trace for operation '{operation_name}' with parameters: {tracing_parameters}")

        return invocation_id
    
    async def send_message_to_all_users_in_tenant_async(activity, tenant_id, custom_headers=None, cancellationToken=None):
        if activity is None:
            raise ValueError("Activity cannot be null.")

        if not tenant_id:
            raise ValueError("Tenant ID cannot be null or empty.")

        content = {
            "Activity": activity,
            "TenantId": tenant_id
        }

        invocation_id = await trace_activity("SendMessageToAllUsersInTenant", content, cancellationToken)

        api_url = "v3/batch/conversation/tenant/"

        result = await retry_action.run_async(
            lambda: TeamsOperations.get_response_async(api_url, "POST", invocation_id, content=content, custom_headers=custom_headers, cancellationToken=cancellationToken),
            lambda ex, ct: TeamsOperations.handle_throttling_exception(ex, ct)
        )

        return result
    

    async def send_message_to_all_users_in_team_async(activity, team_id, tenant_id, custom_headers=None, cancellationToken=None):
        if activity is None:
            raise ValueError("Activity cannot be null.")

        if not team_id:
            raise ValueError("Team ID cannot be null or empty.")

        if not tenant_id:
            raise ValueError("Tenant ID cannot be null or empty.")

        content = {
            "Activity": activity,
            "TeamId": team_id,
            "TenantId": tenant_id
        }
      
        invocation_id = await trace_activity("SendMessageToAllUsersInTeam", content, cancellationToken)

        api_url = "v3/batch/conversation/team/"

        result = await retry_action.run_async(
            lambda: TeamsOperations.get_response_async(api_url, "POST", invocation_id, content=content, custom_headers=custom_headers, cancellationToken=cancellationToken),
            lambda ex, ct: TeamsOperations.handle_throttling_exception(ex, ct)
        )

        return result
    
    async def send_message_to_list_of_channels_async(activity, channels_members, tenant_id, custom_headers=None, cancellationToken=None):
        if activity is None:
            raise ValueError("Activity cannot be null.")

        if not channels_members:
            raise ValueError("Channels members list cannot be empty.")

        if not tenant_id:
            raise ValueError("Tenant ID cannot be null or empty.")

        content = {
            "Members": channels_members,
            "Activity": activity,
            "TenantId": tenant_id
        }

        invocation_id = await trace_activity("SendMessageToListOfChannels", content, cancellationToken)

        api_url = "v3/batch/conversation/channels/"

        result = await retry_action.run_async(
            lambda: TeamsOperations.get_response_async(api_url, "POST", invocation_id, content=content, custom_headers=custom_headers, cancellationToken=cancellationToken),
            lambda ex, ct: TeamsOperations.handle_throttling_exception(ex, ct)
        )

        return result
    
    async def get_operation_state_async(operation_id, custom_headers=None, cancellationToken=None):
        if not operation_id:
            raise ValueError("Operation ID cannot be null or empty.")

        invocation_id = await trace_activity("GetOperationState", {"OperationId": operation_id}, cancellationToken)

        api_url = f"v3/batch/conversation/{urllib.parse.quote(operation_id)}"

        result = await retry_action.run_async(
            lambda: TeamsOperations.get_response_async(api_url, "GET", invocation_id, custom_headers=custom_headers, cancellationToken=cancellationToken),
            lambda ex, ct: TeamsOperations.handle_throttling_exception(ex, ct)
        )

        return result
    
    async def get_paged_failed_entries_async(operation_id, custom_headers=None, continuation_token=None, cancellationToken=None):
        if not operation_id:
            raise ValueError("Operation ID cannot be null or empty.")

        invocation_id = await trace_activity("GetPagedFailedEntries", {"OperationId": operation_id}, cancellationToken)

        api_url = f"v3/batch/conversation/failedentries/{urllib.parse.quote(operation_id)}"

        result = await retry_action.run_async(
            lambda: TeamsOperations.get_response_async(api_url, "GET", invocation_id, continuation_token=continuation_token, custom_headers=custom_headers, cancellationToken=cancellationToken),
            lambda ex, ct: TeamsOperations.handle_throttling_exception(ex, ct)
        )

        return result
    
    async def cancel_operation_async(operation_id, custom_headers=None, cancellationToken=None):
        if not operation_id:
            raise ValueError("Operation ID cannot be null or empty.")

        invocation_id = await trace_activity("CancelOperation", {"OperationId": operation_id}, cancellationToken)

        api_url = f"v3/batch/conversation/{urllib.parse.quote(operation_id)}"

        result = await retry_action.run_async(
            lambda: TeamsOperations.get_response_async(api_url, "DELETE", invocation_id, custom_headers=custom_headers, cancellationToken=cancellationToken),
            lambda ex, ct: TeamsOperations.handle_throttling_exception(ex, ct)
        )
        return result