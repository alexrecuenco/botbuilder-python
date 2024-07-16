from typing import Optional

class AttachmentView:
    def __init__(self, view_id: Optional[str] = None, size: Optional[int] = None):
        self.view_id = view_id
        self.size = size
        self.custom_init()

    def custom_init(self):
        # Add custom initialization code here if needed
        pass

    @property
    def view_id(self) -> Optional[str]:
        return self._view_id

    @view_id.setter
    def view_id(self, value: Optional[str]):
        self._view_id = value

    @property
    def size(self) -> Optional[int]:
        return self._size

    @size.setter
    def size(self, value: Optional[int]):
        self._size = value
