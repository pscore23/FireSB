# -*- coding: utf-8 -*-

import random
import string


def argument_type(enum):
    return {
        1: "menu",
        2: "block",
        3: "note",
        8: "direction",
        9: "color",
        10: "text",
        11: "broadcast",
        12: "variable",
        13: "list"
    }.get(enum, "number")


def generate_random_string(nos: int, los: int) -> list[str]:
    return ["".join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for j in range(los)) for i in range(nos)]
