# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import http
import pytest
import aiohttp
from aiohttp.skills.skill_http_client import SkillHttpClient
import aiounittest
from aiohttp import web
from aiohttp.web import middleware

from botbuilder.core.adapters.test_adapter import TestAdapter
from botbuilder.core.bot_framework_adapter import BotFrameworkAdapter
from botframework.connector import Channels

from aiohttp import ClientSession, ClientResponse
from unittest.mock import AsyncMock, MagicMock, Mock

from botbuilder.core import TurnContext, MessageFactory
from botbuilder.core.teams import TeamsInfo, TeamsActivityHandler
from botbuilder.schema import (
    Activity,
    ChannelAccount,
    ConversationAccount,
)
from botframework.connector._IConnector_client import IConnectorClient
from botframework.connector.auth.microsoft_app_credentials import MicrosoftAppCredentials
from botframework.connector.connector_client import ConnectorClient
from simple_adapter_with_create_conversation import SimpleAdapterWithCreateConversation
from tests.simple_adapter import SimpleAdapter

ACTIVITY = Activity(
    id="1234",
    type="message",
    text="test",
    from_property=ChannelAccount(id="user", name="User Name"),
    recipient=ChannelAccount(id="bot", name="Bot Name"),
    conversation=ConversationAccount(id="convo", name="Convo Name"),
    channel_data={"channelData": {}},
    channel_id="UnitTest",
    locale="en-us",
    service_url="https://example.org",
)


class TestTeamsInfo(aiounittest.AsyncTestCase):
    async def test_send_message_to_teams_channels_without_activity(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        activity = Activity()
        turn_context = TurnContext(adapter, activity)

        try:
            await TeamsInfo.send_message_to_teams_channel(
                turn_context, None, "channelId123"
            )
        except ValueError:
            pass
        else:
            assert False, "should have raise ValueError"

    async def test_send_message_to_teams(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        turn_context = TurnContext(adapter, ACTIVITY)
        handler = TestTeamsActivityHandler()
        await handler.on_turn(turn_context)

    async def test_send_message_to_teams_channels_without_turn_context(self):
        try:
            await TeamsInfo.send_message_to_teams_channel(
                None, ACTIVITY, "channelId123"
            )
        except ValueError:
            pass
        else:
            assert False, "should have raise ValueError"

    async def test_send_message_to_teams_channels_without_teams_channel_id(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        turn_context = TurnContext(adapter, ACTIVITY)

        try:
            await TeamsInfo.send_message_to_teams_channel(turn_context, ACTIVITY, "")
        except ValueError:
            pass
        else:
            assert False, "should have raise ValueError"

    async def test_send_message_to_teams_channel_works(self):
        adapter = SimpleAdapterWithCreateConversation()

        turn_context = TurnContext(adapter, ACTIVITY)
        result = await TeamsInfo.send_message_to_teams_channel(
            turn_context, ACTIVITY, "teamId123"
        )
        assert result[0].activity_id == "new_conversation_id"
        assert result[1] == "reference123"

    async def test_get_team_details_works_without_team_id(self):
        adapter = SimpleAdapterWithCreateConversation()
        ACTIVITY.channel_data = {}
        turn_context = TurnContext(adapter, ACTIVITY)
        result = TeamsInfo.get_team_id(turn_context)

        assert result == ""

    async def test_get_team_details_works_with_team_id(self):
        adapter = SimpleAdapterWithCreateConversation()
        team_id = "teamId123"
        ACTIVITY.channel_data = {"team": {"id": team_id}}
        turn_context = TurnContext(adapter, ACTIVITY)
        result = TeamsInfo.get_team_id(turn_context)

        assert result == team_id

    async def test_get_team_details_without_team_id(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        turn_context = TurnContext(adapter, ACTIVITY)

        try:
            await TeamsInfo.get_team_details(turn_context)
        except TypeError:
            pass
        else:
            assert False, "should have raise TypeError"

    async def test_get_team_channels_without_team_id(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        turn_context = TurnContext(adapter, ACTIVITY)

        try:
            await TeamsInfo.get_team_channels(turn_context)
        except TypeError:
            pass
        else:
            assert False, "should have raise TypeError"

    async def test_get_paged_team_members_without_team_id(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        turn_context = TurnContext(adapter, ACTIVITY)

        try:
            await TeamsInfo.get_paged_team_members(turn_context)
        except TypeError:
            pass
        else:
            assert False, "should have raise TypeError"

    async def test_get_team_members_without_team_id(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        turn_context = TurnContext(adapter, ACTIVITY)

        try:
            await TeamsInfo.get_team_member(turn_context)
        except TypeError:
            pass
        else:
            assert False, "should have raise TypeError"

    async def test_get_team_members_without_member_id(self):
        def create_conversation():
            pass

        adapter = SimpleAdapterWithCreateConversation(
            call_create_conversation=create_conversation
        )

        turn_context = TurnContext(adapter, ACTIVITY)

        try:
            await TeamsInfo.get_team_member(turn_context, "teamId123")
        except TypeError:
            pass
        else:
            assert False, "should have raise TypeError"

    async def test_get_participant(self):
        adapter = SimpleAdapterWithCreateConversation()

        activity = Activity(
            type="message",
            text="Test-get_participant",
            channel_id=Channels.ms_teams,
            from_property=ChannelAccount(aad_object_id="participantId-1"),
            channel_data={
                "meeting": {"id": "meetingId-1"},
                "tenant": {"id": "tenantId-1"},
            },
            service_url="https://test.coffee",
        )

        turn_context = TurnContext(adapter, activity)
        handler = TeamsActivityHandler()
        await handler.on_turn(turn_context)

    async def test_get_meeting_info(self):
        adapter = SimpleAdapterWithCreateConversation()

        activity = Activity(
            type="message",
            text="Test-get_meeting_info",
            channel_id=Channels.ms_teams,
            from_property=ChannelAccount(aad_object_id="participantId-1"),
            channel_data={"meeting": {"id": "meetingId-1"}},
            service_url="https://test.coffee",
        )

        turn_context = TurnContext(adapter, activity)
        handler = TeamsActivityHandler()
        await handler.on_turn(turn_context)

    async def test_send_message_to_list_of_users_async(status_code):
        base_uri = "https://test.coffee"
        
        # Mock HTTP client
        async def mock_send(request):
            response = ClientResponse('GET', request.url)
            response.status = int(status_code)
            response._body = b''  # Mocked response body
            return response

        # Create a mock client session
        mock_session = AsyncMock(spec=ClientSession)
        mock_session._request = mock_send

        # Mock connector client and activity
        connector_client = ConnectorClient(base_uri, MicrosoftAppCredentials("", ""), client_session=mock_session)

        activity = {
            "type": "message",
            "text": "Test-SendMessageToListOfUsersAsync",
            "channelId": Channels.MSTEAMS,
            "serviceUrl": "https://test.coffee",
            "from": {
                "id": "id-1",
                "name": status_code  # Pass expected status code
            },
            "conversation": {"id": "conversation-id"}
        }

        turn_context = TurnContext(SimpleAdapter(), activity)
        turn_context.turn_state["connector_client"] = connector_client

        handler = TestTeamsActivityHandler()
        await handler.on_turn(turn_context)

    async def test_send_message_to_all_users_in_tenant_async(status_code):
        base_uri = "https://test.coffee"
        
        # Mock HTTP client
        async def mock_send(request):
            response = ClientResponse('GET', request.url)
            response.status = int(status_code)
            response._body = b''  # Mocked response body
            return response

        # Create a mock client session
        mock_session = AsyncMock(spec=ClientSession)
        mock_session._request = mock_send

        # Mock connector client and activity
        connector_client = ConnectorClient(base_uri, MicrosoftAppCredentials("", ""), client_session=mock_session)

        activity = {
            "type": "message",
            "text": "Test-SendMessageToAllUsersInTenantAsync",
            "channelId": Channels.MSTEAMS,
            "serviceUrl": "https://test.coffee",
            "from": {
                "id": "id-1",
                "name": status_code  # Pass expected status code
            },
            "conversation": {"id": "conversation-id"}
        }

        turn_context = TurnContext(SimpleAdapter(), activity)
        turn_context.turn_state["connector_client"] = connector_client

        handler = TestTeamsActivityHandler()
        await handler.on_turn(turn_context)


    @pytest.mark.parametrize("status_code", ["201", "400", "403", "404", "429"])
    async def test_send_message_to_all_users_in_team(status_code):
        base_uri = "https://test.coffee"
        roster_handler = RosterHttpMessageHandler()
        custom_http_client = roster_handler.session

        app_credentials = Mock()  # Substitute with your actual app credentials if needed
        connector_client = SkillHttpClient(app_credentials, custom_http_client, base_uri)
        
        activity = Activity(
            type="message",
            text="Test-SendMessageToAllUsersInTeamAsync",
            channel_id=Channels.ms_teams,
            service_url="https://test.coffee",
            from_property=ChannelAccount(id="id-1", name=status_code),
            conversation=ConversationAccount(id="conversation-id")
        )

        turn_context = TurnContext(SimpleAdapter(), activity)
        turn_context.turn_state[IConnectorClient] = connector_client
        handler = TestTeamsActivityHandler()
        
        await handler.on_turn(turn_context)

        

class TestTeamsActivityHandler(TeamsActivityHandler):
    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        if turn_context.activity.text == "test_send_message_to_teams_channel":
            await self.call_send_message_to_teams(turn_context)

    async def call_send_message_to_teams(self, turn_context: TurnContext):
        msg = MessageFactory.text("call_send_message_to_teams")
        channel_id = "teams_channel_123"
        reference = await TeamsInfo.send_message_to_teams_channel(
            turn_context, msg, channel_id
        )

        assert reference[0].activity_id == "new_conversation_id"
        assert reference[1] == "reference123"



class RosterHttpMessageHandler(aiohttp.web.BaseBaseHandler):
    async def handle(self, request: aiohttp.web.Request) -> aiohttp.web.StreamResponse:
        response = web.Response()
        
        # GetTeamDetails
        if request.path.endswith("team-id"):
            content = {
                "id": "team-id",
                "name": "team-name",
                "aadGroupId": "team-aadgroupid"
            }
            response = web.json_response(content)
        
        # SendMessageToThreadInTeams
        elif request.path.endswith("v3/conversations"):
            content = {
                "id": "id123",
                "serviceUrl": "https://serviceUrl/",
                "activityId": "activityId123"
            }
            response = web.json_response(content)
        
        # GetChannels
        elif request.path.endswith("team-id/conversations"):
            content = {
                "conversations": [
                    {"id": "channel-id-1"},
                    {"id": "channel-id-2", "name": "channel-name-2"},
                    {"id": "channel-id-3", "name": "channel-name-3"}
                ]
            }
            response = web.json_response(content)
        
        # GetMembers (Team)
        elif request.path.endswith("team-id/members"):
            content = [
                {
                    "id": "id-1",
                    "objectId": "objectId-1",
                    "name": "name-1",
                    "givenName": "givenName-1",
                    "surname": "surname-1",
                    "email": "email-1",
                    "userPrincipalName": "userPrincipalName-1",
                    "tenantId": "tenantId-1"
                },
                {
                    "id": "id-2",
                    "objectId": "objectId-2",
                    "name": "name-2",
                    "givenName": "givenName-2",
                    "surname": "surname-2",
                    "email": "email-2",
                    "userPrincipalName": "userPrincipalName-2",
                    "tenantId": "tenantId-2"
                }
            ]
            response = web.json_response(content)
        
        # GetMembers (Group Chat)
        elif request.path.endswith("conversation-id/members"):
            content = [
                {
                    "id": "id-3",
                    "objectId": "objectId-3",
                    "name": "name-3",
                    "givenName": "givenName-3",
                    "surname": "surname-3",
                    "email": "email-3",
                    "userPrincipalName": "userPrincipalName-3",
                    "tenantId": "tenantId-3"
                },
                {
                    "id": "id-4",
                    "objectId": "objectId-4",
                    "name": "name-4",
                    "givenName": "givenName-4",
                    "surname": "surname-4",
                    "email": "email-4",
                    "userPrincipalName": "userPrincipalName-4",
                    "tenantId": "tenantId-4"
                }
            ]
            response = web.json_response(content)
        
        # Get Member
        elif request.path.endswith("team-id/members/id-1") or request.path.endswith("conversation-id/members/id-1"):
            content = {
                "id": "id-1",
                "objectId": "objectId-1",
                "name": "name-1",
                "givenName": "givenName-1",
                "surname": "surname-1",
                "email": "email-1",
                "userPrincipalName": "userPrincipalName-1",
                "tenantId": "tenantId-1"
            }
            response = web.json_response(content)
        
        # Get participant
        elif request.path.endswith("v1/meetings/meetingId-1/participants/participantId-1"):
            if request.query.get("tenantId") == "tenantId-1":
                content = {
                    "user": {"userPrincipalName": "userPrincipalName-1"},
                    "meeting": {"role": "Organizer"},
                    "conversation": {"Id": "meetigConversationId-1"}
                }
                response = web.json_response(content)
        
        # Get meeting details
        elif request.path.endswith("v1/meetings/meeting-id"):
            content = {
                "details": {"id": "meeting-id"},
                "organizer": {"id": "organizer-id"},
                "conversation": {"id": "meetingConversationId-1"}
            }
            response = web.json_response(content)
        
        # Post meeting notification
        elif request.path.endswith("v1/meetings/meeting-id/notification"):
            request_body = await request.json()
            notification = request_body.get("notification")
            obo = notification["ChannelData"]["OnBehalfOfList"][0]
            display_name = obo["DisplayName"]
            
            if display_name == "207":
                failure_info = {"RecipientMri": notification["Value"]["Recipients"][0]}
                infos = {"RecipientsFailureInfo": [failure_info]}
                response = web.json_response(infos, status=207)
            elif display_name == "403":
                response = web.json_response({"error": {"code": "BotNotInConversationRoster"}}, status=403)
            elif display_name == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            else:
                response = web.Response(status=202)
        
        # SendMessageToListOfUsers
        elif request.path.endswith("v3/batch/conversation/users/"):
            request_body = await request.json()
            request_activity = request_body["Activity"]
            from_name = request_activity["from"]["name"]
            
            if from_name == "201":
                response = web.Response(text="operation-1", status=201)
            elif from_name == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            elif from_name == "403":
                response = web.json_response({"error": {"code": "Forbidden"}}, status=403)
            elif from_name == "429":
                response = web.json_response({"error": {"code": "TooManyRequests"}}, status=429)
            else:
                response = web.Response(status=202)
        
        # SendMessageToAllUsersInTenant
        elif request.path.endswith("v3/batch/conversation/tenant/"):
            request_body = await request.json()
            request_activity = request_body["Activity"]
            from_name = request_activity["from"]["name"]
            
            if from_name == "201":
                response = web.Response(text="operation-1", status=201)
            elif from_name == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            elif from_name == "403":
                response = web.json_response({"error": {"code": "Forbidden"}}, status=403)
            elif from_name == "429":
                response = web.json_response({"error": {"code": "TooManyRequests"}}, status=429)
            else:
                response = web.Response(status=202)
        
        # SendMessageToAllUsersInTeam
        elif request.path.endswith("v3/batch/conversation/team/"):
            request_body = await request.json()
            request_activity = request_body["Activity"]
            from_name = request_activity["from"]["name"]
            
            if from_name == "201":
                response = web.Response(text="operation-1", status=201)
            elif from_name == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            elif from_name == "403":
                response = web.json_response({"error": {"code": "Forbidden"}}, status=403)
            elif from_name == "404":
                response = web.json_response({"error": {"code": "NotFound"}}, status=404)
            elif from_name == "429":
                response = web.json_response({"error": {"code": "TooManyRequests"}}, status=429)
            else:
                response = web.Response(status=202)
        
        # SendMessageToListOfChannels
        elif request.path.endswith("v3/batch/conversation/channels/"):
            request_body = await request.json()
            request_activity = request_body["Activity"]
            from_name = request_activity["from"]["name"]
            
            if from_name == "201":
                response = web.Response(text="operation-1", status=201)
            elif from_name == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            elif from_name == "403":
                response = web.json_response({"error": {"code": "Forbidden"}}, status=403)
            elif from_name == "429":
                response = web.json_response({"error": {"code": "TooManyRequests"}}, status=429)
            else:
                response = web.Response(status=202)
        
        # GetOperationState
        elif "v3/batch/conversation/operation-id" in request.path and request.method == "GET":
            status = request.path.split("%2A")[-1]
            
            if status == "200":
                content = {
                    "state": "state-1",
                    "response": {"statusMap": {"statusMap-1": 1}},
                    "totalEntriesCount": 1
                }
                response = web.json_response(content)
            elif status == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            elif status == "429":
                response = web.json_response({"error": {"code": "TooManyRequests"}}, status=429)
            else:
                response = web.Response(status=202)
        
        # GetPagedFailedEntries
        elif "v3/batch/conversation/failedentries/operation-id" in request.path:
            status = request.path.split("%2A")[-1]
            
            if status == "200":
                content = {
                    "continuationToken": "token-1",
                    "failedEntries": [{"id": "entry-1", "error": "400 user not found"}]
                }
                response = web.json_response(content)
            elif status == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            elif status == "429":
                response = web.json_response({"error": {"code": "TooManyRequests"}}, status=429)
            else:
                response = web.Response(status=202)
        
        # CancelOperation
        elif "v3/batch/conversation/operation-id" in request.path and request.method == "DELETE":
            status = request.path.split("%2A")[-1]
            
            if status == "200":
                response = web.Response(status=200)
            elif status == "400":
                response = web.json_response({"error": {"code": "BadSyntax"}}, status=400)
            elif status == "429":
                response = web.json_response({"error": {"code": "TooManyRequests"}}, status=429)
            else:
                response = web.Response(status=202)
        
        return response

    async def init_app():
        app = web.Application()
        app.router.add_route("*", "/{tail:.*}", RosterHttpMessageHandler())
        return app

    if __name__ == "__main__":
        web.run_app(init_app())

