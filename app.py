from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('trained_model.pkl', 'rb'))

# Define a route for prediction API
@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from JSON request
    input_features = request.json['features']
    input_features = np.array(input_features).reshape(1, -1)

    # Make prediction using the loaded model
    prediction = model.predict(input_features)
    prediction = prediction.tolist()  # Convert NumPy array to Python list
    # Format prediction result
    result = {'prediction': prediction[0]}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
