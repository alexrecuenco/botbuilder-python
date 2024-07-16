import json

class TeamDetails:
    def __init__(self, id=None, name=None, aad_group_id=None):
        self.id = id
        self.name = name
        self.aad_group_id = aad_group_id
        self.channel_count = 0  # Default value for channel count
        self.member_count = 0   # Default value for member count
        self.type = None        # Default value for team type
        self.custom_init()

    def custom_init(self):
        # Custom initialization logic can be placed here
        pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
