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