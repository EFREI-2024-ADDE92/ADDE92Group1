from flask import Flask, request, jsonify
import joblib
import numpy as np
from Model import iris
app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('trained_model.joblib')

@app.route('/predict/<sl>/<sw>/<pl>/<pw>', methods=['POST'])
def predict(sl, sw, pl, pw):
    try:
        # Get the input data from the request
        features = np.array([[sl, sw, pl, pw]])

        # Make predictions using the loaded model
        prediction = model.predict(features)

        # Return the prediction as JSON
        retour = iris.target_names[prediction[0]]
        result = {'prediction': retour}
        
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
