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
    return UezdSectionService(db).get()


@router.get('/{u_code}')
async def get_uezd(u_code: int, db: Session = Depends(get_session)) -> Uezd:
    return UezdSectionService(db).get_by_code(u_code)


@router.delete('/{u_code}')
async def delete(u_code: int, db: Session = Depends(get_session)):
    UezdSectionService(db).delete(u_code)


@router.patch('/{u_code}/{u_name}')
async def patch(u_code: int, u_name: str, db: Session = Depends(get_session)):
    return UezdSectionService(db).patch(u_code, u_name)


@router.post('/{u_name}')
async def add(u_name: str, db: Session = Depends(get_session)):
    return UezdSectionService(db).add(u_name)
