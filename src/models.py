from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from db import Base

class Action(Base):
    __tablename__ = 'action'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[BigInteger]
    articul: Mapped[BigInteger]
    timestamp: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())