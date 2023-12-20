from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from service.uezdSection import UezdSectionService
from scheme.uezd import Uezd

router = APIRouter(
    prefix='/uezd',
    tags=['Uezd']
)


@router.get('')
async def get(db: Session = Depends(get_session)) -> List[Uezd]:
    # return dict uezd(nasPunkt(Church))......
    # тут возвращают serviceUezdDict обертку, которую надо описать в service/serviceUezdDict.py, которая делает запросы к базе и возвращает словарь из уездов нас пунктов церквей
    return UezdSectionService(db).get()
