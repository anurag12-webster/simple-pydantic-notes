
from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name: str
    price: str
    in_stock: bool
    # in_stock: bool = True # this is how we can set default values

