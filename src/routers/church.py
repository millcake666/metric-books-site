from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from service.church import ChurchService

router = APIRouter(
    prefix='/church',
    tags=['Church']
)


@router.delete('/{np_code}/{c_code}')
async def delete(np_code: int, c_code: int, db: Session = Depends(get_session)):
    return ChurchService(db).delete(np_code, c_code)


@router.patch('/{np_code}/{c_code}/{c_name}')
async def patch(np_code: int, c_code: int, c_name: str, db: Session = Depends(get_session)):
    return ChurchService(db).patch(np_code, c_code, c_name)


@router.post('/{np_code}/{c_name}')
async def add(np_code: int, c_name: str, db: Session = Depends(get_session)):
    return ChurchService(db).add(np_code, c_name)
