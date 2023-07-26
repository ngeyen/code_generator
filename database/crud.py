from sqlalchemy.orm import Session

from database import models, schemas



def get_all_family_codes(db: Session, skip: int = 0, limit: int = 100, used:bool=False):
    return db.query(models.FamilyCodeModel).filter(models.FamilyCodeModel.is_registered==used).offset(skip).limit(limit).all()


def get_family_code(db: Session, code: str, status:bool = False):
    return db.query(models.FamilyCodeModel).filter(
                    models.FamilyCodeModel.family_code == code,
                    models.FamilyCodeModel.is_registered==status).first()
    

def create_family_code(db: Session, serializer: schemas.FamilyCodeBase) -> schemas.FamilyCodeBase:
    db_item = models.FamilyCodeModel(
        family_code=serializer.family_code, is_registered=serializer.is_registered)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return schemas.FamilyCodeBase(id=db_item.id, is_registered=db_item.is_registered, 
                                  registered=db_item.registered, family_code=db_item.family_code)


def update_family_code( instance: models.FamilyCodeModel, model: models.FamilyCodeModel, db: Session) -> schemas.FamilyCodeBase:
    family_code_data = model.dict(exclude_unset=True)
    for key, value in family_code_data.items():
        setattr(instance, key, value)
        
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return schemas.FamilyCodeBase(id=instance.id, is_registered=instance.is_registered, registered=instance.registered, family_code=instance.family_code)


