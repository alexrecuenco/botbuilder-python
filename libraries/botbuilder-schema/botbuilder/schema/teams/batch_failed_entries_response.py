import json
from typing import List

class BatchFailedEntriesResponse:
    def __init__(self):
        self.continuation_token = None  # Initializes continuation token
        self.failed_entries = []  # Initializes list of failed entries

    @property
    def continuation_token(self) -> str:
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, value: str):
        self._continuation_token = value

    @property
    def failed_entries(self) -> List['BatchFailedEntry']:
        return self._failed_entries

    @failed_entries.setter
    def failed_entries(self, value: List['BatchFailedEntry']):
        self._failed_entries = value

class BatchFailedEntry:
    def __init__(self, id: str, error_message: str):
        self.id = id
        self.error_message = error_message
