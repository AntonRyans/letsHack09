import folium 
import pandas as pd

# Corrected data with proper coordinates for Leicester area
data = {
    "place": [
        "Charles Wilson Building",
    ],
    "latitude": [52.6218],
    "longitude": [-1.1236],
    "address": [
        "Charles Wilson Building, University of Leicester, Leicester LE1 7RH",
    ],
    "rating": [4.8]
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
map_file_path = "C:/Users/anton/Documents/GitHub/letsHack09/cwMap.html"

# Save map to HTML file
map_.save(map_file_path)
print(f"Map has been saved as '{map_file_path}'")
