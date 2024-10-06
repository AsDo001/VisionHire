from json import JSONEncoder
from datetime import datetime
from enum import Enum


class JSONCustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Enum):
            return obj.value
        
        return super().default(obj)