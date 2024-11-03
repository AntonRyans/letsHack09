import folium 
import pandas as pd

# Corrected data with proper coordinates for Leicester area
data = {
    "place": [
        "Attenborough Arts Centre",
    ],
    "latitude": [52.6246],
    "longitude": [-1.1256],
    "address": [
        "Attenborough Arts Centre, University of Leicester, Lancaster Rd, Leicester LE1 7HA",
    ],
    "rating": [4.7]
}

places_df = pd.DataFrame(data)

# Center the map around the average latitude and longitude of all places
map_center = [places_df['latitude'].mean(), places_df['longitude'].mean()]
map_ = folium.Map(location=map_center, zoom_start=13)

# Add markers to the map for each location
for _, place in places_df.iterrows():
    folium.Marker(
        location=[place['latitude'], place['longitude']],
        popup=folium.Popup(f"<b>{place['place']}</b><br>{place['address']}<br>Rating: {place['rating']}"),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(map_)

# Replace this line with a local file path
map_file_path = "C:/Users/anton/Documents/GitHub/letsHack09/attenboroughMap.html"

# Save map to HTML file
map_.save(map_file_path)
print(f"Map has been saved as '{map_file_path}'")
