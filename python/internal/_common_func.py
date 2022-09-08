# -*- coding: utf-8 -*-

import random
import string


def generate_random_string(nos: int, los: int) -> list[str]:
    return ["".join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for j in range(los)) for i in range(nos)]
