from pydantic import BaseModel



class FamilyCodeBase(BaseModel):
    
    id: int | None
    family_code: str
    is_registered: bool
    
    class Config:
        from_attributes=True


