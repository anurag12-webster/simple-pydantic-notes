from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    imageUrl : Optional[str] = None
    # imageUrl : str = None # this is how we can set default values
    