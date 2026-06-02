from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)

# Allow requests from other applications
CORS(app)

# Home route
@app.route('/')
def home():
    return "Sorting Microservice is running!"

# Sort data by distance field
@app.route('/sort/distance', methods=['POST'])
def sort_distance():

    # Get JSON data from request
    data = request.get_json()

    # Check if data is in array format
    if not isinstance(data, list):
         return jsonify({
            "error": "Expected array in request body"
        }), 400
    
    # Sort data by distance
    sorted_items = sorted(
        data,
        key=lambda item: float(item.get('distance', 0))
    )

    # Return sorted data
    return jsonify(sorted_items)

# Sorting endpoint
@app.route('/sort', methods=['POST'])
def sort_races():

    # Get JSON data from request
    data = request.get_json()

    # Get races list
    races = data.get('races', [])

    # Get sorting type
    sort_by = data.get('sortBy', 'date')

    # Sort by distance
    if sort_by == 'distance':
        sorted_races = sorted(
            races,
            key=lambda race: race.get('distance', 0)
        )

    # Sort by date
    elif sort_by == 'date':
        sorted_races = sorted(
            races,
            key=lambda race: race.get('date', '')
        )

    # Invalid sort type
    else:
        return jsonify({
            "error": "Invalid sort type"
        }), 400

    # Return sorted races
    return jsonify(sorted_races)


# Run server
if __name__ == '__main__':
    app.run(debug=True, port=3002)