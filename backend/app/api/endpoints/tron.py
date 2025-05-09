from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from tronpy import Tron
from tronpy.providers.http import HTTPProvider
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.config import settings
from app.crud.tron import tron_crud
from app.schemas.dto import FailedResponse, SuccessResponse
from app.schemas.tron import TronAddressRequest, TronRequestSchema

router = APIRouter()


@router.post(
    "/",
    response_model=SuccessResponse | FailedResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
)
async def get_wallet_info(
    address: TronAddressRequest,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        if not settings.api_key:
            return FailedResponse(
                status=False,
                data={None},
                message="Укажите api_ket в env файле",
            )
        client = Tron(provider=HTTPProvider(api_key=settings.api_key))
        address = address.address
        balance = client.get_account_balance(address)
        bandwidth = client.get_bandwidth(address)
        resource_info = client.get_account_resource(address)
        energy_remaining = resource_info.get(
            "EnergyLimit", 0
        ) - resource_info.get("EnergyUsed", 0)
        data = {
            "wallet_address": address,
            "balance": balance,
            "bandwidth": bandwidth,
            "energy_remaining": energy_remaining,
        }
        await tron_crud.create(obj_in=data, session=session)

        return SuccessResponse(status=True, data=data)

    except Exception as e:
        return FailedResponse(status=False, data={None}, message=str(e))


@router.get(
    "/",
    response_model=SuccessResponse[List[TronRequestSchema]],
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
)
async def get_data(session: AsyncSession = Depends(get_async_session)):
    return SuccessResponse(
        status=True,
        data=await tron_crud.get_multi(session=session),
    )
