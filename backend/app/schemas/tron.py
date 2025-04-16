from pydantic import BaseModel, Field, field_validator
import re


class TronAddressRequest(BaseModel):
    address: str = Field(..., description="Tron address (starts with 'T')")

    @field_validator("address")
    @classmethod
    def validate_tron_address(cls, v: str) -> str:
        if v.startswith("tron:"):
            v = v[5:]
        if not re.match(r"^T[a-zA-Z0-9]{33}$", v):
            raise ValueError("Некорректный Tron-адрес")
        return v
