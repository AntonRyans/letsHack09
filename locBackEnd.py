from flask import Flask, request, jsonify
from flask_cors import CORS
from geopy.geocoders import Nominatim
from flask import send_from_directory

app = Flask(__name__, static_folder="C:/Users/anton/Documents/GitHub/letsHack09")
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes


# Geolocator instance
geolocator = Nominatim(user_agent="geoapiExercises")

@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/test', methods=['POST'])
def test():
    return jsonify({'address': 'Sir Bob Burgess Building Leicester LE2 6BF '})

@app.route('/get_location', methods=['POST'])
def get_location():
    data = request.json
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    latitude = data['latitude']
    longitude = data['longitude']

    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    if location:
        return jsonify({'address': location.address})
    else:
        return jsonify({'error': 'Location not found'}), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)  # Bind to localhost
