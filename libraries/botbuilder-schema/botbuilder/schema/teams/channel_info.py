import json

class ChannelInfo:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        self.custom_init()

    def custom_init(self):
        # Custom initialization logic can be placed here
        pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
