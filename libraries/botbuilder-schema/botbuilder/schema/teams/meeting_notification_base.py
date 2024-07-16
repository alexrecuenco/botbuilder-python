# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from dataclasses import dataclass
from typing import Optional
import json

@dataclass
class MeetingNotificationBase:
    """
    Specifies Bot meeting notification base including channel data and type.
    """

    type: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def from_json(data: str):
        json_data = json.loads(data)
        return MeetingNotificationBase(**json_data)
