from typing import Optional

from sqlmodel import Field, SQLModel
from datetime import datetime


class FamilyCodeBase(SQLModel):
    family_code: str
    


class FamilyCodeModel(FamilyCodeBase, table=True):
    __tablename__ = "family_codes"

    id: Optional[int] = Field(default=None, primary_key=True)
    registered: Optional[datetime] = Field(default= datetime.now())
    is_registered: Optional[bool] = Field(default=False)


class FamilyCodeCreate(FamilyCodeBase):
    pass
