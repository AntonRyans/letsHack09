# letsHack09
Location based event notification and planner - website ( different to social media  ) 
whats on nearby.

Requirements:
1) needs to be able to access location when started up ( adjustable radius )
2) date and time of events ( comp sci , campus leagues for sports and links to instagram or linktrees )
3) 
https://www.geeksforgeeks.org/gps-tracker-using-python/


code

import requests

def get_location(ip_address=None):
    # Use ipinfo.io to get location data
    url = f"https://ipinfo.io/{ip_address}/json" if ip_address else "https://ipinfo.io/json"
    response = requests.get(url)  # Send a request to the URL
    data = response.json()  # Parse the JSON response
    
    # Extract relevant information
    location = {
        "ip": data.get("ip"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "location": data.get("loc")  # Latitude and longitude
    }
    return location

# Get location data for the current user
user_location = get_location()
print(user_location)  # Print the location data
