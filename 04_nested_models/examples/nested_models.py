from typing import(
    List, 
    Optional
)

from pydantic import(
    BaseModel,
    Field
)

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int
    name : str
    address : Address

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None

# Notes:
# - Forward referencing is needed when a model refers to itself or another model not yet defined.
# - Always call 'model_rebuild()' after the class definition if you use forward references.
# - This ensures type hints are properly resolved at runtime.
    
# Forward referencing is used above because 'Comment' refers to itself in the 'replies' field.
# In Pydantic v1, you would use 'update_forward_refs()' to resolve this.
# In Pydantic v2, you use 'model_rebuild()' to resolve forward references after the class definition.

Comment.model_rebuild()

address = Address(
    street = "123 Main St",
    city = "New York",
    postal_code = "10001"
)

user = User(
    id = 1,
    name = "Anurag K",
    address = address
)

comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(
            id=2,
            content="This is a reply",
            replies=[
                Comment(
                    id=3,
                    content="This is a nested reply"
                )
            ]
        )
    ]
)

print(user)
print(comment) 
print(address)