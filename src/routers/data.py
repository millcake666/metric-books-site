from typing import Sequence, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from scheme.uezd import Uezd
from scheme.data import Data
from service.data import DataService

router = APIRouter(
    prefix='/data',
    tags=['Data']
)


@router.get('/{u_code}/{np_code}/{c_code}/{}')
async def get(db: Session = Depends(get_session)) -> dict:
    # return dict uezd(nasPunkt(Church))......
    # тут возвращают serviceUezdDict обертку, которую надо описать в service/serviceUezdDict.py, которая делает запросы к базе и возвращает словарь из уездов нас пунктов церквей
    return DataService(db).get()
