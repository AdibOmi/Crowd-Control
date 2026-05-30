from fastapi import APIRouter, HTTPException
from app.data.fake_data import venues
import random

router = APIRouter()


def calculate_level(current, capacity):
    percentage = round((current / capacity) * 100, 2)

    if percentage < 40:
        level = "Low"
    elif percentage < 75:
        level = "Medium"
    else:
        level = "High"

    return percentage, level


@router.get("/venues")
def get_venues():
    return venues



@router.get("/venues/{venue_id}/occupancy")
def get_venue_occupancy(venue_id: int):
    for venue in venues:
        if venue["id"] == venue_id:
            # venue["current_count"] = random.randint(5, venue["capacity"])

            percentage, level = calculate_level(
                venue["current_count"],
                venue["capacity"]
            )

            return {
                "id": venue["id"],
                "venue_name": venue["venue_name"],
                "current_count": venue["current_count"],
                "capacity": venue["capacity"],
                "crowd_level": level,
                "percentage": percentage
            }

    raise HTTPException(status_code=404, detail="Venue not found")

@router.post("/venues/{venue_id}/enter")
def enter_venue(venue_id: int):
    for venue in venues:
        if venue["id"] == venue_id:
            if venue["current_count"] >= venue["capacity"]:
                raise HTTPException(status_code=400, detail="Venue is full")

            venue["current_count"] += 1
            return {"message": "Person entered", "current_count": venue["current_count"]}

    raise HTTPException(status_code=404, detail="Venue not found")


@router.post("/venues/{venue_id}/exit")
def exit_venue(venue_id: int):
    for venue in venues:
        if venue["id"] == venue_id:
            if venue["current_count"] <= 0:
                raise HTTPException(status_code=400, detail="Venue is already empty")

            venue["current_count"] -= 1
            return {"message": "Person exited", "current_count": venue["current_count"]}

    raise HTTPException(status_code=404, detail="Venue not found")