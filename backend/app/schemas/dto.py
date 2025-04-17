from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    status: bool
    message: Optional[str] = None


class SuccessResponse(BaseResponse[T], Generic[T]):
    data: T


class FailedResponse(SuccessResponse):
    pass
