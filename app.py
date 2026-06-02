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
    
    # Check if required field is present
    if "distance" not in data:
        return jsonify({
            "error": "Missing required field 'distance'"
        }), 400
    
    # Sort data by distance
    sorted_items = sorted(
        data,
        key=lambda item: float(item.get('distance', 0))
    )

    # Return sorted data
    return jsonify(sorted_items)

# Sort data by date field
@app.route('/sort/date', methods=['POST'])
def sort_date():

    # Get JSON data from request
    data = request.get_json()

    # Check if data is in array format
    if not isinstance(data, list):
        return jsonify({
            "error": "Expected array in request body"
        }), 400
    
     # Check if field is present
    if "date" not in data:
           return jsonify({
            "error": "Missing required field 'date'"
        }), 400
    
    # Sort data by date
    sorted_items = sorted(
        data,
        key=lambda item: (item.get('date', ''))
    )

    # Return sorted data
    return jsonify(sorted_items)

# Run server
if __name__ == '__main__':
    app.run(debug=True, port=3002)