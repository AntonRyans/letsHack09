from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from geopy.geocoders import Nominatim

# Initialize FastAPI
app = FastAPI()

# Initialize the Nominatim geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Define the request body schema
class Coordinates(BaseModel):
    latitude: float
    longitude: float

@app.post("/get_location")
async def get_location(coordinates: Coordinates):
    latitude = coordinates.latitude
    longitude = coordinates.longitude

    # Perform reverse geocoding
    location = geolocator.reverse((latitude, longitude), exactly_one=True)

    if location:
        print(location.address)
    else:
        raise HTTPException(status_code=404, detail="Location not found")
    
print("works")

