# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List, Dict
from botbuilder.schema.teams._models_py3 import ConversationList, TeamDetails
import asyncio

class ITeamsOperations:
    """
    Interface for TeamsOperations operations.
    """

    async def fetch_channel_list_with_http_messages_async(self, team_id: str, custom_headers: Dict[str, List[str]] = None, cancellationToken: asyncio.Event = None) -> ConversationList:
        """
        Fetches channel list for a given team.

        :param team_id: Team Id.
        :param custom_headers: The headers that will be added to request.
        :param cancellationToken: The cancellation token.
        :raises HttpOperationException: Thrown when the operation returned an invalid status code.
        :raises SerializationException: Thrown when unable to deserialize the response.
        :raises ValidationException: Thrown when a required parameter is null.
        :return: The channel list for a given team.
        """
        raise NotImplementedError()

    async def fetch_team_details_with_http_messages_async(self, team_id: str, custom_headers: Dict[str, List[str]] = None, cancellationToken: asyncio.Event = None) -> TeamDetails:
        """
        Fetches details related to a team.

        :param team_id: Team Id.
        :param custom_headers: The headers that will be added to request.
        :param cancellationToken: The cancellation token.
        :raises HttpOperationException: Thrown when the operation returned an invalid status code.
        :raises SerializationException: Thrown when unable to deserialize the response.
        :raises ValidationException: Thrown when a required parameter is null.
        :return: The details related to a team.
        """
        raise NotImplementedError()
