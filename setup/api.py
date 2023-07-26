from fastapi import FastAPI
from api.docs import (
    description,
    summary, terms_of_service, 
    version, contact,license_info,
)


app = FastAPI(
    title='FeverApp Codes API',
    summary=summary,
    description=description,
    terms_of_service=terms_of_service,
    contact=contact,
    version=version,
    license_info=license_info,
)