import json
from typing import Dict

class BatchOperationState:
    def __init__(self):
        self.state = None  # Initializes operation state
        self.status_map = {}  # Initializes status map
        self.retry_after = None  # Initializes retry datetime
        self.total_entries_count = 0  # Initializes total entries count
