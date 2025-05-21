# creaye employee model 
# fields
# id int
# name str min 3 chars
# department optional str default to "general"
# slary float musrt be >=10000
from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id : int
    name : str = Field(..., 
                       min_length=3, 
                       max_length=50,
                       description="Name of the employee",
                       example="Anurag Kanade"
                       )
    # three elipsis (...) means required in the Field.
    department: Optional[str] = "general"
    salary : float = Field(...,
                           ge=10000,
                           description="Salary of the employee"
                           )
    # ge means greater than or equal to
    # le means less than or equal to
    # gt means greater than
    # lt means less than