from pydantic import BaseModel
from datetime import datetime

class FamilyCodeBase(BaseModel):
    
    id: int | None
    family_code: str
    is_registered: bool | None
    registered: datetime | None
    


