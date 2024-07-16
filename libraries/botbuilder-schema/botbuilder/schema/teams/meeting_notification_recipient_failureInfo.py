# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from dataclasses import dataclass
from typing import Optional
import json

@dataclass
class MeetingNotificationRecipientFailureInfo:
    """
    Information regarding failure to notify a recipient of a meeting notification.
    """

    recipient_mri: Optional[str] = None
    error_code: Optional[str] = None
    failure_reason: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def from_json(data: str):
        json_data = json.loads(data)
        return MeetingNotificationRecipientFailureInfo(**json_data)
