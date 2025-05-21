# create booking model

# fields
# user_id int
# room_id int
# nights int must be greater than 1
# rate_per_night float
# also add a computed field total_amount = nights * rate_per_night

from pydantic import(
    BaseModel,
    computed_field,
    Field
) 

class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(..., ge=1, description="Number of nights must be greater than 1")
    rate_per_night : float
    # computed field should be used after the field is defined
    @computed_field
    @property
    def toptal_amount(self) -> float:
        return self.nights * self.rate_per_night    
    
booking = Booking(
    user_id=1,
    room_id=101,
    nights=3,
    rate_per_night=100.0
)
