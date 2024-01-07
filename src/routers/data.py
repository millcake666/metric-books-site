from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from service.data import DataService
from scheme.data import Data

router = APIRouter(
    prefix='/data',
    tags=['Data']
)


@router.get('/{c_code}')
async def get(c_code: int, db: Session = Depends(get_session)) -> List[Data]:
    return DataService(db).get(c_code)


@router.delete('/{met_code}')
async def delete(met_code: int, db: Session = Depends(get_session)):
    return DataService(db).delete(met_code)


@router.patch('/{u_code}/{np_code}/{np_name}')
async def patch(u_code: int, np_code: int, np_name: str, db: Session = Depends(get_session)):
    return DataService(db).patch(u_code, np_code, np_name)


@router.post('/{u_code}/{np_name}')
async def add(u_code: int, np_name: str, db: Session = Depends(get_session)):
    return DataService(db).add(u_code, np_name)
