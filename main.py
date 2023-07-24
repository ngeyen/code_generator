from fastapi import FastAPI
from api.generator import code_generator, string_generator, number_generator

from api.docs import (
    description,
    summary, terms_of_service, 
    version, contact,license_info,
)
from fastapi import status

app = FastAPI(
    title='FeverApp Codes API',
    summary=summary,
    description=description,
    terms_of_service=terms_of_service,
    contact=contact,
    version=version,
    license_info=license_info,
    openapi_url='/',
)



@app.get("/generate", description="To generate a unique code, you can make a request to the `/generate` endpoint without providing any additional parameters. The default code length will be used (8 characters)")
async def code_generator():
    code = code_generator()
    context ={}
    context['code'] = code
    context['message'] = 'successful'
    context['status'] = status.HTTP_200_OK
    return context


@app.get("/chars/{length}", description="Takes `length` as parameter and generates codes with only characters with that length")
async def character_generator(length: int):
    code = string_generator(length)
    context ={}
    context['code'] = code
    context['message'] = 'successful'
    context['status'] = status.HTTP_200_OK
    return context


@app.get("/numbers/{length}", description="Takes `length` as parameter and generates codes with only integers with that length")
async def numbers_only(length: int):
    code = number_generator(length)
    context ={}
    context['code'] = code
    context['message'] = 'successful'
    context['status'] = status.HTTP_200_OK
    return context
