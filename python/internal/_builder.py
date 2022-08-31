import json

from static import _generic

block_definitation = _generic._define("block_definitation")


class BaseBuilder(_generic.GenericData):
    menu, block = None, None
    number = 0
    color, text, broadcast_id, broadcast_name = "", "", "", ""

    def __init__(self, **kwargs):
        super().__init__(kwargs)

        self.iter_num = 0
