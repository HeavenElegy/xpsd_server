import json
from datetime import date

from apps.workAssistant.entities.base import BaseResponse


class CustomJsonEncoder(json.JSONEncoder):

    def default(self, o):
        pass

    def encode(self, o):
        if isinstance(o, dict):
            pass
        else:
            o = o.__dict__
        return super().encode(o)
