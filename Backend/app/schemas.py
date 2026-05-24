from pydantic import BaseModel
#pydantic validates data automatically and returns clean JSON

class VenueCreate(BaseModel):
#input from user
    name: str
    address: str
    capacity: int


class VenueOut(VenueCreate):
#output
#inherits from VenueCreate
    id: int

    class Config:
        from_attributes = True
        #allows pydantic to convert database objects into schema objects