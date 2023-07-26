import string
import random
import math


def code_generator( prefix:str, chars=string.ascii_lowercase + string.digits) -> str | bool:
    prefix_length = len(prefix)
    if prefix_length >=8:
        return False
    
    size = 8- prefix_length
    
    return prefix + (''.join(random.choice(chars) for _ in range(size)))


def string_generator(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def number_generator(length):
    digits = "1234567890"
    code = ""

    for i in range(length):
        code += digits[math.floor(random.random() * 10)]
    return code

# from data import existing_users
# from database import crud
# from database import schemas

# def register_users(db):
#     for index,item in enumerate(existing_users):
#         code = schemas.FamilyCodeBase( id=index,
#             family_code=item, is_registered=True
#         )
#         crud.create_family_code(db, family_code=code)