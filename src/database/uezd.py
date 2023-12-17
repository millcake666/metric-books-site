from database.database import Base


class Uezd(Base):
    __tablename__ = 'uezd'

    u_code = Column(Integer(), primary_key=True)
    u_name = Column(Text(), nullable=False)
    nas_punkt = relationship("NasPunkt")