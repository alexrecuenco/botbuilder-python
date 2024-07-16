# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List
from dataclasses import dataclass
from botbuilder.schema.teams.meeting_notification_recipient_failureInfo import MeetingNotificationRecipientFailureInfo

@dataclass
class MeetingNotificationResponse:
    """
    Specifies Bot meeting notification response.
    Contains list of MeetingNotificationRecipientFailureInfo.
    """

    recipients_failure_info: List[MeetingNotificationRecipientFailureInfo] = None

    def __init__(self, recipients_failure_info: List[MeetingNotificationRecipientFailureInfo] = None):
        self.recipients_failure_info = recipients_failure_info or []
