# -*- coding: utf-8 -*-

import json
from typing import Any
from urllib import request

from python.internal.static import _exceptions

headers = {
    "x-csrftoken": "a",
    "x-requested-with": "XMLHttpRequest",
    "Cookie": "scratchcsrftoken=a;scratchlanguage=en;",
    "referer": "https://scratch.mit.edu",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.101 Safari/537.36 "
}


class Require:
    @staticmethod
    def get_project_data(project_url: str) -> Any:
        if project_url.lower().startswith("https"):
            req = request.Request(project_url, headers=headers)

            try:
                with request.urlopen(req) as res:  # nosec
                    return json.dumps(json.loads(res.read().decode(
                        "utf-8")), ensure_ascii=False, indent=4, sort_keys=False, separators=(",", ": "))

            except UnicodeEncodeError:
                raise _exceptions.InputError("URL に使用できない文字が含まれています")

        else:
            raise _exceptions.InputError("\"https://\" から始まる URL を入力してください")
