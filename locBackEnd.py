from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from geopy.geocoders import Nominatim
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI()
# Enable CORS for all origins (or specify your frontend origin for added security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origins if possible, e.g., ["http://localhost:8000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Serve static files (like FrontEnd.html)
app.mount("/", StaticFiles(directory="C:/Users/anton/Documents/GitHub/letsHack09", html=True), name="static")

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
        return {"address": location.address}
    else:
        raise HTTPException(status_code=404, detail="Location not found")


if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
print("works")