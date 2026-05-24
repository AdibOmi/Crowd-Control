from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Venue
from app.schemas import VenueCreate, VenueOut

router = APIRouter(prefix="/venues", tags=["Venues"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VenueOut)
#returned data follows VenueOut schema
def create_venue(venue: VenueCreate, db: Session = Depends(get_db)):
    new_venue = Venue(
        name=venue.name,
        address=venue.address,
        capacity=venue.capacity
    )

    db.add(new_venue)
    db.commit()
    db.refresh(new_venue)

    return new_venue


@router.get("/", response_model=list[VenueOut])
def get_venues(db: Session = Depends(get_db)):
    return db.query(Venue).all()
    #all venue rows