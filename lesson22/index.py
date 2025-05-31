from pydantic import BaseModel, conint, constr
from typing import Optional

# class User (BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str
#
# user = User (id=1, name= 'John', age=25, email='john@example.com')
# print (user)

class User (BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

user1 = User (id=1, name= 'John', age=25, email='john@example.com')
print(user1)
user2 = User (id=1, name= 'John', age=25)
print(user2)
user3 = User (id=1, name= 'John',email='john@example.com')
print(user3)
user4 = User (id=1, name= 'John',)
print(user4)

class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)

validuser = another_user(id=1, name='drilon')
print(validuser)
invaliduser = another_user(id=0, name='po')
print(invaliduser)