from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session

router = APIRouter()


@router.post(
    "/",
    # response_model=,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
)
async def create_new_donation(
    # donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return 123
