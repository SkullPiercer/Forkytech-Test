from typing import Union

from tronpy import Tron
from tronpy.providers.http import HTTPProvider

from fastapi import APIRouter
from app.schemas.tron import TronAddressRequest
from app.schemas.dto import FailedResponse, SuccessResponse

router = APIRouter()


@router.post(
    "/",
    response_model=Union[SuccessResponse, FailedResponse],
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
)
async def create_new_donation(
    address: TronAddressRequest,
):
    try:

        client = Tron(
            provider=HTTPProvider(
                api_key="ade25cd0-3a2c-40a3-8322-9cc4d2ad3cfc"
            )
        )
        address = address.address
        balance = client.get_account_balance(address)
        bandwidth = client.get_bandwidth(address)
        resource_info = client.get_account_resource(address)
        energy_remaining = resource_info.get(
            "EnergyLimit", 0
        ) - resource_info.get("EnergyUsed", 0)
        data = {
            "balance": balance,
            "bandwidth": bandwidth,
            "energy": energy_remaining,
        }

        return SuccessResponse(status=True, data=data)

    except Exception as e:
        return FailedResponse(status=False, data={None}, message=str(e))
