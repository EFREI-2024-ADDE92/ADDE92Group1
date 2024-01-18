import joblib
import numpy as np
from flask import Flask, jsonify
from flask_cors import CORS
from sklearn.datasets import load_iris
from prometheus_flask_exporter import PrometheusMetrics


iris = load_iris()

app = Flask(__name__)
CORS(app)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

# Load the pre-trained model
model = joblib.load('trained_model.joblib')

@app.route('/predict/<sl>/<sw>/<pl>/<pw>', methods=['POST'])
@metrics.do_not_track()
@metrics.counter('counter', 'count_of_preds')
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
    app.run()
