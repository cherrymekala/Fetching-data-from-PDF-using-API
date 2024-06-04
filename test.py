from pydantic import BaseModel

#extending the BaseModel
class User(BaseModel):
    user: str
    age: int

user = User(user="Om",age="21")
print(user)