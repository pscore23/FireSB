from typing import Any
import json

from python.internal.static import _generic

block_def = _generic._define("block_def")
input_ = _generic._define("input")
field_ = _generic._define("field")


class BlockBuilder(_generic.GenericData):
    menu, block = None, None
    number = 0
    color, text, broadcast_id, broadcast_name = "", "", "", ""

    def __init__(self, **kwargs):
        super().__init__(kwargs)

        self._iter_count = 0

    def __repr__(self):
        return f"<BlockBuilder {self.id}>"

    def __iter__(self):
        return self

    def __next__(self):
        self_ = self

        for _ in range(self._iter_count):
            if getattr(self_, "next", None):
                self_ = self_.next

            else:
                self._iter_count += 1

                raise StopIteration

        self._iter_count += 1

        return self_

    def __eq__(self, other: Any):
        return self.id == other.id

    @property
    def isolated(self):
        return getattr(self, "first_block", False) and not getattr(self, "next", None)

    @property
    def proc_define(self):
        if self._mutation:
            return block_def(
                name=self.id,
                code=self._mutation["proccode"],
                arg_ids=json.loads(self._mutation["argumentids"]),
                arg_names=json.loads(self._mutation["argumentnames"]),
                arg_defaults=json.loads(self._mutation["argumentdefaults"]),
                without_refresh=self._mutation.get("warp", False)
            )

    @property
    def selectables(self):
        return self.inputs + self.fields
