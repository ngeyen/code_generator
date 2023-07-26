from fastapi import status, Depends, HTTPException
from sqlmodel import SQLModel,Session


from api.generator import code_generator, string_generator, number_generator

from database.database import  engine
from database import crud, models, schemas
from setup.db import get_db
from setup.api import app


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)





@app.patch("/family_codes/{code}/", tags=["Family Codes"], response_model=schemas.FamilyCodeBase)
def update_family_code(code: str, family_code: schemas.FamilyCodeBase, db: Session = Depends(get_db)):
    db_fcode = crud.get_family_code(db, code=code)
    if not db_fcode:
        raise HTTPException(status_code=404, detail="Family code not found")
    return crud.update_family_code(instance=db_fcode, db=db, model=family_code)

  
      
@app.get("/family_codes/", tags=["Family Codes"], response_model=list[schemas.FamilyCodeBase])
def read_family_codes(skip: int = 0, limit: int = 100, used:bool=False, db: Session = Depends(get_db)):
    family_codes = crud.get_all_family_codes(db, skip=skip, limit=limit, used=used)
    return family_codes  


@app.get("/generate/{prefix}/{size}", tags=["Generate"], response_model=list[schemas.FamilyCodeBase], description="To generate a unique code, you can make a request to the `/generate` endpoint without providing any additional parameters. The default code length will be used (8 characters)",)
async def codes_generator_api_view(prefix:str, size:int, db:Session=Depends(get_db)):
    code = code_generator(prefix=prefix)
    if code == False:
        raise HTTPException(status_code=400, detail='Prefix longer than 8 characters')
    codes_list = []
    for i in range(size):
        
        db_fcode = crud.get_family_code(db, code=code)
        if not db_fcode:
            pass
        family_code = schemas.FamilyCodeBase(family_code=code, is_registered=False )
        new_code = crud.create_family_code(db, family_code=family_code)
        codes_list.append(new_code)

    return codes_list



if __name__ == "__main__":
    create_db_and_tables()