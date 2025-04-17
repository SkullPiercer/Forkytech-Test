from app.crud.base import CRUDBase
from app.models.tron_request import TronRequest


class CRUDTron(CRUDBase):
    pass


tron_crud = CRUDTron(TronRequest)
