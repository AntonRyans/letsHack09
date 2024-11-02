from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Initialize the Nominatim geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

@app.route('/get_location', methods=['POST'])
def get_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude is not None and longitude is not None:
        # Perform reverse geocoding
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        
        if location:
            return jsonify({"address": location.address}), 200
        else:
            return jsonify({"error": "Location not found"}), 404
    else:
        return jsonify({"error": "Invalid coordinates"}), 400

if __name__ == '__main__':
    app.run(debug=True)
