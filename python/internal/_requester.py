# -*- coding: utf-8 -*-

import json
import re
from typing import Any
from urllib import error, request

from python.internal.static import _exceptions

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.101 Safari/537.36 "
}


class Require:
    @staticmethod
    def get_project_data(query: str) -> Any:
        if query.lower().startswith("https"):
            req = request.Request(re.compile(r"<[^>]*?>").sub("", query), headers=HEADERS)

            try:
                with request.urlopen(req) as res:  # nosec
                    return json.dumps(json.loads(res.read().decode(
                        "utf-8")), ensure_ascii=False, indent=4, sort_keys=False, separators=(",", ": "))

            except UnicodeEncodeError:
                raise _exceptions.InputError("URL に使用できない文字が含まれています")

            except error.HTTPError as e:
                if e.code >= 400:
                    raise _exceptions.RequestError(e.reason)

                else:
                    raise _exceptions.UnknownError("不明なエラーが発生しました")

        else:
            raise _exceptions.ProtocolError("\"https://\" から始まる URL を指定してください")
