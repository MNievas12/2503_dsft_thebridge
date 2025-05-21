from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"  # the table

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )  # column id, is primary key and has autoincrement
    publication_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    )  # column publication_date, cannot be null, default value is now
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # a short text
    content: Mapped[str] = mapped_column(Text, nullable=False)  # a long text
