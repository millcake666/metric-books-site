from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session

from scheme.uezd import Uezd

router = APIRouter(
    prefix='/uezd',
    tags=['Uezd']
)


@router.get('')
async def get(db: Session = Depends(get_session)) -> Uezd:
    # return dict uezd(nasPunkt(Church))......
    return Uezd(u_code=1, u_name='abc')
