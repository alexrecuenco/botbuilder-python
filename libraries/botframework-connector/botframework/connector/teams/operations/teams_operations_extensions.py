# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import TurnContext
from botframework.connector.aio import ConnectorClient
from botframework.connector.teams import TeamsConnectorClient
from botbuilder.schema.teams import ConversationList, TeamDetails, MeetingInfo, TeamsMeetingParticipant
from botbuilder.schema.teams.meeting_notification_response import MeetingNotificationResponse
from botbuilder.schema.teams.meeting_notification_base import  MeetingNotificationBase
from botframework.connector.teams.operations._iteams_operations import ITeamsOperations
from botbuilder.schema.iactivity import IActivity
from botbuilder.schema.teams.team_member import TeamMember
from botbuilder.schema.teams.batch_operation_state import BatchOperationState
from botbuilder.schema.teams.batch_failed_entries_response import BatchFailedEntriesResponse
from botframework.connector.teams.operations.teams_operations import TeamsOperations
from typing import List
import asyncio

class TeamsOperationsExtensions:

    @staticmethod
    async def fetch_channel_list(operations: ITeamsOperations, team_id: str, cancellation_token=None) -> ConversationList:
        result = await operations.fetch_channel_list_with_http_messages_async(team_id, cancellation_token=cancellation_token)
        return result.body

    @staticmethod
    async def fetch_team_details(operations: ITeamsOperations, team_id: str, cancellation_token=None) -> TeamDetails:
        result = await operations.fetch_team_details_with_http_messages_async(team_id, cancellation_token=cancellation_token)
        return result.body

    @staticmethod
    async def fetch_meeting_info(operations: ITeamsOperations, meeting_id: str, cancellation_token=None) -> MeetingInfo:
        if isinstance(operations,TeamsOperations):
            result = await operations.fetch_meeting_info_with_http_messages_async(meeting_id, cancellation_token=cancellation_token)
            return result.body
        else:
             raise Exception("TeamsOperations with GetParticipantWithHttpMessagesAsync is required for FetchParticipantAsync.")


    @staticmethod
    async def fetch_participant_async(operations, meeting_id, participant_id, tenant_id, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.fetch_participant_with_http_messages_async(meeting_id, participant_id, tenant_id, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with FetchParticipantWithHttpMessagesAsync is required for FetchParticipantAsync.")


    async def send_meeting_notification_async(operations, meeting_id, notification, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.send_meeting_notification_message_async(meeting_id, notification, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with SendMeetingNotificationMessageAsync is required for SendMeetingNotificationAsync.")


    @staticmethod
    async def send_message_to_list_of_users_async(operations, activity, teams_members, tenant_id, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.send_message_to_list_of_users_async(activity, teams_members, tenant_id, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with SendMessageToListOfUsersAsync is required for SendMessageToListOfUsersAsync.")

    @staticmethod
    async def send_message_to_all_users_in_tenant_async(operations, activity, tenant_id, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.send_message_to_all_users_in_tenant_async(activity, tenant_id, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with SendMessageToAllUsersInTenantAsync is required for SendMessageToAllUsersInTenantAsync.")
    @staticmethod
    async def send_message_to_all_users_in_team_async(operations, activity, team_id, tenant_id, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.send_message_to_all_users_in_team_async(activity, team_id, tenant_id, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with SendMessageToAllUsersInTeamAsync is required for SendMessageToAllUsersInTeamAsync.")

    @staticmethod
    async def send_message_to_list_of_channels_async(operations, activity, channels_members, tenant_id, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.send_message_to_list_of_channels_async(activity, channels_members, tenant_id, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with SendMessageToListOfChannelsAsync is required for SendMessageToListOfChannelsAsync.")

    @staticmethod
    async def get_operation_state_async(operations, operation_id, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.get_operation_state_async(operation_id, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with GetOperationStateAsync is required for GetOperationStateAsync.")

    @staticmethod
    async def get_paged_failed_entries_async(operations, operation_id, continuation_token=None, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            result = await operations.get_paged_failed_entries_async(operation_id, continuation_token=continuation_token, cancellationToken=cancellationToken)
            return result.body
        else:
            raise ValueError("TeamsOperations with GetPagedFailedEntriesAsync is required for GetPagedFailedEntriesAsync.")


    @staticmethod
    async def cancel_operation_async(operations, operation_id, cancellationToken=None):
        if isinstance(operations, TeamsOperations):
            await operations.cancel_operation_async(operation_id, cancellationToken=cancellationToken)
        else:
            raise ValueError("TeamsOperations with CancelOperationAsync is required for CancelOperationAsync.")
