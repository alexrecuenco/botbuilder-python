from typing import List, Union
from datetime import datetime, timezone
from dataclasses import dataclass

@dataclass
class ChannelAccount:
    id: str

@dataclass
class ConversationAccount:
    id: str

@dataclass
class Entity:
    # Define Entity properties as needed
    pass

@dataclass
class IActivity:
    Type: str
    Id: str
    ServiceUrl: str
    Timestamp: Union[datetime, None]
    LocalTimestamp: Union[datetime, None]
    ChannelId: str
    From: ChannelAccount
    Conversation: ConversationAccount
    Recipient: ChannelAccount
    ReplyToId: str
    Entities: List[Entity]
    ChannelData: dict

    def GetChannelData(self, TypeT):
        # Implementation for getting channel data as strongly typed object
        pass

    def TryGetChannelData(self, TypeT) -> bool:
        # Implementation for trying to get channel data as strongly typed object
        pass

    def AsMessageActivity(self):
        # Implementation specific to IMessageActivity interface
        pass

    def AsContactRelationUpdateActivity(self):
        # Implementation specific to IContactRelationUpdateActivity interface
        pass

    def AsInstallationUpdateActivity(self):
        # Implementation specific to IInstallationUpdateActivity interface
        pass

    def AsConversationUpdateActivity(self):
        # Implementation specific to IConversationUpdateActivity interface
        pass

    def AsTypingActivity(self):
        # Implementation specific to ITypingActivity interface
        pass

    def AsEndOfConversationActivity(self):
        # Implementation specific to IEndOfConversationActivity interface
        pass

    def AsEventActivity(self):
        # Implementation specific to IEventActivity interface
        pass

    def AsInvokeActivity(self):
        # Implementation specific to IInvokeActivity interface
        pass

    def AsMessageUpdateActivity(self):
        # Implementation specific to IMessageUpdateActivity interface
        pass

    def AsMessageDeleteActivity(self):
        # Implementation specific to IMessageDeleteActivity interface
        pass

    def AsMessageReactionActivity(self):
        # Implementation specific to IMessageReactionActivity interface
        pass

    def AsSuggestionActivity(self):
        # Implementation specific to ISuggestionActivity interface
        pass

    def GetConversationReference(self):
        # Implementation specific to getting a conversation reference
        pass

    def ApplyConversationReference(self, reference, isIncoming=False):
        # Implementation specific to applying conversation reference
        pass
