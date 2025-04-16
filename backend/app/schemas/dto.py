from typing import Generic, Optional, TypeVar

from pydantic.generics import GenericModel

T = TypeVar("T")


class BaseResponse(GenericModel, Generic[T]):
    status: bool
    message: Optional[str] = None


class SuccessResponse(BaseResponse[T], Generic[T]):
    data: T


class FailedResponse(SuccessResponse):
    pass
