from pydantic import (
    BaseModel, 
    field_validator, 
    model_validator, 
    computed_field
)

# field validators are used to validate individual fields in a model. They are called when the field is 
# being set, and they can be used to perform validation on the value of that field.

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters long')
        return v

# they are used to validate the entire model after all fields values have been received.
class SignUpData(BaseModel):
    password: str
    confirm_password: str
    
    # model_validator is used to validate the entire model (class) simply to put after all fields have been set.
    @model_validator(mode='after')
    def check_passwords(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueError('Passwords do not match')
        return values

class Product(BaseModel):
    price : float
    quantity : int
    # computed fields are used to define a field that is calculated based on other fields in the model.
    # they are defined using the @computed_field and @property decorator  
    # computed fields main task usually is to calculate a value based on other fields in the model.
    
    @computed_field
    @property
    def total_price(self):
        return self.price * self.quantity