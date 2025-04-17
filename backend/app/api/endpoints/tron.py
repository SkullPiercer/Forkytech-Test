from tronpy import Tron
from tronpy.providers.http import HTTPProvider

from fastapi import APIRouter
from app.schemas.tron import TronAddressRequest
from app.schemas.dto import FailedResponse, SuccessResponse
from app.core.config import settings

router = APIRouter()


@router.post(
    "/",
    response_model=SuccessResponse | FailedResponse,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
)
async def create_new_donation(
    address: TronAddressRequest,
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
            "balance": balance,
            "bandwidth": bandwidth,
            "energy": energy_remaining,
        }

        return SuccessResponse(status=True, data=data)

    except Exception as e:
        return FailedResponse(status=False, data={None}, message=str(e))
