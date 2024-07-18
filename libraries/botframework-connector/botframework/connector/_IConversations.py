from typing import List, Dict, Optional
import asyncio
from msrest.serialization import Deserializer
from msrest.exceptions import HttpOperationError

from botbuilder.schema._models_py3 import ConversationParameters

from .models import ConversationsResult, ConversationResourceResponse, ResourceResponse, ChannelAccount, PagedMembersResult, Activity, Transcript, AttachmentData
#from .parameters import ConversationParameters

class IConversations:
    async def get_conversations_with_http_messages_async(self, continuation_token: Optional[str] = None, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[ConversationsResult]:
        pass

    async def create_conversation_with_http_messages_async(self, parameters: ConversationParameters, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[ConversationResourceResponse]:
        pass

    async def send_to_conversation_with_http_messages_async(self, conversation_id: str, activity: Activity, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[ResourceResponse]:
        pass

    async def send_conversation_history_with_http_messages_async(self, conversation_id: str, transcript: Transcript, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[ResourceResponse]:
        pass

    async def update_activity_with_http_messages_async(self, conversation_id: str, activity_id: str, activity: Activity, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[ResourceResponse]:
        pass

    async def reply_to_activity_with_http_messages_async(self, conversation_id: str, activity_id: str, activity: Activity, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[ResourceResponse]:
        pass

    async def delete_activity_with_http_messages_async(self, conversation_id: str, activity_id: str, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[None]:
        pass

    async def get_conversation_members_with_http_messages_async(self, conversation_id: str, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[List[ChannelAccount]]:
        pass

    async def get_conversation_paged_members_with_http_messages_async(self, conversation_id: str, page_size: Optional[int] = None, continuation_token: Optional[str] = None, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[PagedMembersResult]:
        pass

    async def delete_conversation_member_with_http_messages_async(self, conversation_id: str, member_id: str, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[None]:
        pass

    async def get_activity_members_with_http_messages_async(self, conversation_id: str, activity_id: str, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[List[ChannelAccount]]:
        pass

    async def upload_attachment_with_http_messages_async(self, conversation_id: str, attachment_upload: AttachmentData, custom_headers: Optional[Dict[str, List[str]]] = None, cancellationToken: Optional[asyncio.CancelToken] = None) -> Deserializer[ResourceResponse]:
        pass
