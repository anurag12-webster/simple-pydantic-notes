from pydantic import(
    BaseModel,
    ConfigDict
)
from typing import (
    List,
    Optional,
)
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S'),
        }
    )

user = User(
    id=1,
    name="Anurag J=K",
    email="anurag@gmail.com",
    created_at=datetime(2024, 1, 1, 12, 0),
    address=Address(
        street="123 Main St",
        city="New York",
        zip_code="10001"
    ),
    tags=["python", "js"]
)
# print(user)

user_dict = user.model_dump() 
print(user_dict) # -> dict

user_json = user.model_dump_json()
print(user_json) # -> str