from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from typing import Optional

from .database import Base
from sqlmodel import Field, SQLModel
from datetime import datetime





class FamilyCodeModel(SQLModel, table=True):
    __tablename__ = "family_codes"

    id: Optional[int] = Field(default=None, primary_key=True)
    family_code = str
    registered: Optional[DateTime] = Field(default= datetime.now())
    is_registered: Optional[bool] = Field(default=False)

