from typing import List

from botbuilder.schema._attachment_view import AttachmentView

class AttachmentInfo:
    def __init__(self, name: str = None, type: str = None, views: List['AttachmentView'] = None):
        self.name = name
        self.type = type
        self.views = views if views is not None else []
        self.custom_init()

    def custom_init(self):
        # Add custom initialization code here if needed
        pass

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def views(self) -> List['AttachmentView']:
        return self._views

    @views.setter
    def views(self, value: List['AttachmentView']):
        self._views = value if value is not None else []

