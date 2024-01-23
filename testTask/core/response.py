from typing import Union, Any


def create_response(data: Union[Any, dict] = None, code: int = None, description: str = None, message: str = None):
    _response = {"code": 200 if code is None else code,
                 "description": description,
                 "data": data,
                 "message": message}

    return _response
