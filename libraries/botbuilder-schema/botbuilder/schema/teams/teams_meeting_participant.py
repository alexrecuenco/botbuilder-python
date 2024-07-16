from pydantic import BaseModel, Field
from typing import Optional

class TeamsChannelAccount(BaseModel):
    # Add properties of TeamsChannelAccount here
    # Example:
    id: Optional[str] = None
    name: Optional[str] = None

class ConversationAccount(BaseModel):
    # Add properties of ConversationAccount here
    # Example:
    id: Optional[str] = None
    name: Optional[str] = None

class MeetingParticipantInfo(BaseModel):
    # Add properties of MeetingParticipantInfo here
    # Example:
    role: Optional[str] = None

class TeamsMeetingParticipant(BaseModel):
    user: TeamsChannelAccount = Field(...)
    meeting: Optional[MeetingParticipantInfo] = None
    conversation: Optional[ConversationAccount] = None

    class Config:
        arbitrary_types_allowed = True

