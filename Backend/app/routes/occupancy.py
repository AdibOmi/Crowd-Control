from fastapi import APIRouter
from app.data.fake_data import occupancy_data

router = APIRouter()

@router.get("/occupancy")
def get_occupancy():
    current = occupancy_data["current_count"]
    capacity = occupancy_data["capacity"]

    percentage = (current / capacity) * 100

    if percentage < 40:
        level = "Low"
    elif percentage < 75:
        level = "Medium"
    else:
        level = "High"

    return {
        "venue_name": occupancy_data["venue_name"],
        "current_count": current,
        "capacity": capacity,
        "crowd_level": level,
        "percentage": round(percentage, 2),
    }