from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('trained_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)

        # Make predictions using the loaded model
        prediction = model.predict(features)

        # Return the prediction as JSON
        result = {'prediction': int(prediction[0])}
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
