from typing import List
from dataclasses import dataclass
from botbuilder.schema.teams.channel_info import ChannelInfo

@dataclass
class ConversationList:
    conversations: List[ChannelInfo]

    def __init__(self, conversations: List[ChannelInfo] = None):
        if conversations is None:
            conversations = []
        self.conversations = conversations
