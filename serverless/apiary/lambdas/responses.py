import decimal
import json
from typing import Optional


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def _HTTP_Json_Response(body: dict, headers: Optional[dict] = None, status_code: int = 200) -> dict:
    headers = headers or {}
    headers = {
        **headers,
        "Content-Type": "application/json",
    }

    return {
        "headers": headers,
        "statusCode": status_code,
        "body": json.dumps(body, cls=DecimalEncoder)
    }


def HTTP_200_OK(body: dict, headers: Optional[dict] = None) -> dict:
    return _HTTP_Json_Response(body, headers, 200)


def HTTP_400_BAD_REQUEST(body: dict, headers: Optional[dict] = None) -> dict:
    return _HTTP_Json_Response(body, headers, 400)


def HTTP_404_NOT_FOUND(body: Optional[dict] = None, headers: Optional[dict] = None) -> dict:
    body = body or {"detail": "Resource not found!"}
    return _HTTP_Json_Response(body, headers, 404)
