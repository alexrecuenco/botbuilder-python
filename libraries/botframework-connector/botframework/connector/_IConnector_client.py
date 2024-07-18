import json
from typing import Optional
from urllib.parse import urlparse

from botbuilder.schema._models_py3 import Attachment, ConversationsResult

class IConnectorClient:
    def __init__(self, base_uri: Optional[str] = None):
        self._base_uri = urlparse(base_uri) if base_uri else None
        self._serialization_settings = JsonSerializerSettings()
        self._deserialization_settings = JsonSerializerSettings()
        self._credentials = ServiceClientCredentials()

    @property
    def base_uri(self):
        return self._base_uri

    @base_uri.setter
    def base_uri(self, value):
        self._base_uri = urlparse(value) if value else None

    @property
    def serialization_settings(self):
        return self._serialization_settings

    @property
    def deserialization_settings(self):
        return self._deserialization_settings

    @property
    def credentials(self):
        return self._credentials

    @property
    def attachments(self):
        return Attachment()

    @property
    def conversations(self):
        return ConversationsResult()

class JsonSerializerSettings:
    pass

class ServiceClientCredentials:
    pass

# class IAttachments:
#     pass

# class IConversations:
#     pass
