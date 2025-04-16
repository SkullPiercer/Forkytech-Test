from typing import Union

from tronpy import Tron
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

        client = Tron()
        address = address.address
        # balance = client.get_account_balance(address)
        bandwidth = client.get_bandwidth(address)
        # get_estimated_energy
        data = {
            # "balance": balance,
            "bandwidth_usage": bandwidth,
            # "energy_usage": energy,
            # "bandwidth_limit": bandwidth_limit,
            # "energy_limit": energy_limit,
        }

        return SuccessResponse(status=True, data=data)

    except Exception as e:
        return FailedResponse(status=False, data={None}, message=str(e))
