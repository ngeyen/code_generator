from fastapi import status, Depends, HTTPException
from sqlmodel import Session


from api.generator import code_generator

from database.database import  get_session as get_db, init_db
from database import crud, schemas
from setup.api import app




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


@app.get("/generate/{prefix}/{batch_size}", tags=["Generate"], response_model=list[schemas.FamilyCodeBase], description="To generate a unique code, you can make a request to the `/generate` endpoint without providing any additional parameters. The default code length will be used (8 characters)",)
async def codes_generator_api_view(prefix:str, batch_size:int, db:Session=Depends(get_db)):
    codes_list = []
    for i in range(batch_size):
        code = code_generator(prefix=prefix)
        if code == False:
            raise HTTPException(status_code=400, detail='Prefix longer than 8 characters')
    
        db_fcode = crud.get_family_code(db, code=code)
        if not db_fcode:
            pass
        family_code = schemas.FamilyCodeBase(family_code=code, is_registered=False )
        new_code = crud.create_family_code(db, serializer=family_code)
        codes_list.append(new_code)

    return codes_list






@app.on_event("startup")
def on_startup():
    init_db()