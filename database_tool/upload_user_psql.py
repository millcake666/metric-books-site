from database.database import Base, get_session, engine
from database.users import Users
from database.role import Role


# Грузим таблицы в базу
# Base.metadata.create_all(engine)
Base.metadata.drop_all(engine)
quit(0)

# Добавляем значения их csv файлов в базу
session = get_session()

session.add_all([
    Role(
        id=0,
        name='Admin'
    ),
    Role(
        id=1,
        name='Editor'
    ),
    Role(
        id=2,
        name='Default'
    )
])
session.commit()

session.add_all([
    Users(
        role_id=0,
        id=0,
        first_name='Dmitry',
        last_name='Gryaznov',
        middle_name='Aleksandrovich'
    ),
    Users(
        role_id=1,
        id=1,
        first_name='Max',
        last_name='Popov',
        middle_name='Vladimirovich'
    ),
    Users(
        role_id=2,
        id=2,
        first_name='Pavel',
        last_name='Morozov',
        middle_name='Ivanovich'
    ),
    Users(
        role_id=2,
        id=3,
        first_name='Default',
        last_name='Default',
        middle_name='Default'
    )
])

session.commit()
