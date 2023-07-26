from sqlalchemy.orm import Session

from database import models, schemas



def get_all_family_codes(db: Session, skip: int = 0, limit: int = 100, used:bool=False):
    return db.query(models.FamilyCodeModel).filter(models.FamilyCodeModel.is_registered==used).offset(skip).limit(limit).all()

def get_family_code(db: Session, code: str, status:bool = False):
    return db.query(models.FamilyCodeModel).filter(models.FamilyCodeModel.family_code == code, models.FamilyCodeModel.is_registered==status).first()

def create_family_code(db: Session, family_code: schemas.FamilyCodeBase):
    db_item = models.FamilyCodeModel(**family_code.model_dump(), )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_family_code( instance: models.FamilyCodeModel, model: models.FamilyCodeModel, db: Session):
    family_code_data = model.dict(exclude_unset=True)
    for key, value in family_code_data.items():
        setattr(instance, key, value)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

