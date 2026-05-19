from fastapi import FastAPI
from pydantic import BaseModel
from shapely import wkt
from shapely.geometry import Point
import csv
from pathlib import Path

app = FastAPI()

CSV_PATH = Path(__file__).with_name("3-ers-grids-parents-only.csv")


class CoordinateRequest(BaseModel):
    longitude: float
    latitude: float


def load_regions():
    regions = []

    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            parent = row.get("parent")
            geometry = row.get("geometry")

            if parent and geometry:
                regions.append({
                    "parent": parent,
                    "polygon": wkt.loads(geometry)
                })

    return regions


regions = load_regions()


@app.get("/")
def health_check():
    return {
        "status": "API is running",
        "regions_loaded": len(regions)
    }


@app.post("/check-location")
def check_location(request: CoordinateRequest):
    point = Point(request.longitude, request.latitude)

    matches = []

    for region in regions:
        if region["polygon"].covers(point):
            matches.append(region["parent"])

    return {
        "longitude": request.longitude,
        "latitude": request.latitude,
        "inside": len(matches) > 0,
        "parent": matches[0] if matches else None,
        "matches": matches
    }
