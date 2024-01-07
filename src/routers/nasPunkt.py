from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from service.nasPunkt import NasPunktService
from scheme.nasPunkt import NasPunkt

router = APIRouter(
    prefix='/nasPunkt',
    tags=['NasPunkt']
)


@router.get('')
async def get(db: Session = Depends(get_session)) -> List[NasPunkt]:
    return NasPunktService(db).get()


@router.get('/{np_code}')
async def get_uezd(np_code: int, db: Session = Depends(get_session)) -> NasPunkt:
    return NasPunktService(db).get_by_code(np_code)


@router.delete('/{u_code}/{np_code}')
async def delete(u_code: int, np_code: int, db: Session = Depends(get_session)):
    return NasPunktService(db).delete(u_code, np_code)


@router.patch('/{u_code}/{np_code}/{np_name}')
async def patch(u_code: int, np_code: int, np_name: str, db: Session = Depends(get_session)):
    return NasPunktService(db).patch(u_code, np_code, np_name)


@router.post('/{u_code}/{np_name}')
async def add(u_code: int, np_name: str, db: Session = Depends(get_session)):
    return NasPunktService(db).add(u_code, np_name)
