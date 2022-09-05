from typing import Any
import json

from static import _generic

block_definitation = _generic._define("block_definitation")
_input: type = _generic._define("input")
_field: type = _generic._define("field")


class BlockBuilder(_generic.GenericData):
    menu, block = None, None
    number = 0
    color, text, broadcast_id, broadcast_name = "", "", "", ""

    def __init__(self, **kwargs):
        super().__init__(kwargs)

        self.iter_count: int = 0

    def __repr__(self):
        return f"<BlockBuilder {self.id}>"

    def __iter__(self):
        return self

    def __next__(self):
        self_ = self

        for _ in range(self.iter_count):
            if getattr(self_, "next", None):
                self_ = self_.next

            else:
                self.iter_count += 1

                raise StopIteration

        self.iter_count += 1

        return self_

    def __eq__(self, other: Any):
        return self.id == other.id

    @property
    def isolated(self):
        return getattr(self, "first_block", False) and not getattr(self, "next", None)
