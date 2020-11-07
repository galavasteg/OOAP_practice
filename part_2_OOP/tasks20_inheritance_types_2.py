"""
----------------------- TASK 20 -----------------------

    Приведите примеры кода, реализующие:
    1. наследование вариаций (functional/type variation inheritance),
    2. наследование с конкретизацией (reification inheritance)
    3. и структурное наследование (structure inheritance).

"""
from http import HTTPStatus
from pathlib import Path
from typing import overload, Union, TypedDict


# 3. Structure inheritance
class SimpleResponse(TypedDict):
    content: bytes
    content_length: int
    status: HTTPStatus


class BaseAPI:
    def __init__(self, url: str):
        self.url = self.validate(url)

    def upload_content(self, content: bytes) -> SimpleResponse:
        response = ...
        return response

    def validate(self, url: str) -> str:
        raise NotImplementedError


class BaseView:
    ...

    def has_view_permission(self, request, user=None) -> bool:
        return True


class SecretView(BaseView):
    ...

    # 1.1. Functional variation inheritance
    def has_view_permission(self, request, user=None) -> bool:
        if user and user.is_admin:
            return True
        else:
            return False


class FileAPI(BaseAPI):
    # 1.2. Type variation inheritance
    @overload
    def upload_content(self, content: Union[str, Path]) -> SimpleResponse: ...

    def upload_content(self, content) -> SimpleResponse:
        with open(str(content), mode='rb') as file_obj:
            content = file_obj.read()
        response = super().upload_content(content)
        return response

    # 2. Reification inheritance
    def validate(self, url: str) -> str:
        valid_url = ...
        return valid_url
