# @Time : 10/7/23 2:05 PM
# @Author : HanyuLiu/Rainman
# @Email : rainman@ref.finance
# @File : exceptions.py
from fastapi.requests import Request
from starlette.responses import JSONResponse


class SettingNotFound(Exception):
    pass


class APIException(Exception):
    """

    """
    def __init__(self,
                 error_code: int = 000,
                 status_code: int = 500,
                 detail="",
                 message="",
                 *args,
                 **kwargs
                 ):
        Exception.__init__(self, *args, **kwargs)

        self.error_code = error_code
        self.message = message
        self.detail = detail
        self.status_code = status_code

    def __str__(self):
        return f"APIException(status_code={self.status_code}, detail={self.message})"


async def on_api_exception(
    request: Request,
    exception: APIException
) -> JSONResponse:
    content = {"error": {"error_code": exception.error_code}}

    if exception.message:
        content['error']['message'] = exception.message

    if exception.detail:
        content['error']['detail'] = exception.detail

    return JSONResponse(content=content, status_code=exception.status_code)