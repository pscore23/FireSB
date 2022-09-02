import json

from static import _generic

block_definitation = _generic._define("block_definitation")
_input = _generic._define("input")
_field = _generic._define("field")


class BlockBuilder(_generic.GenericData):
    menu, block = None, None
    number = 0
    color, text, broadcast_id, broadcast_name = "", "", "", ""

    def __init__(self, **kwargs):
        super().__init__(kwargs)

        self.iter_count = 0

    def __repr__(self):
        return f"<BlockBuilder {self.id}>"

    def __iter__(self):
        return self
