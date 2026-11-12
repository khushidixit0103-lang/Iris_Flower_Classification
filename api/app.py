"""
Iris Flower Classification - REST API
=====================================
Built using Flask to expose the trained Decision Tree model as an HTTP service.
This service receives flower measurements from the n8n workflow and returns
real-time botanical classification results in JSON format.
"""

import os
import sys
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# Determine paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "saved_model", "iris_decision_tree_model.joblib")
METADATA_PATH = os.path.join(BASE_DIR, "model", "saved_model", "model_metadata.joblib")

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from n8n webhooks and browsers

# Global variables for model
model = None
metadata = None

SPECIES_MAP = {
    0: "Iris Setosa",
    1: "Iris Versicolor",
    2: "Iris Virginica"
}

SPECIES_EXPLANATIONS = {
    "Iris Setosa": "Iris Setosa is clearly distinguished by its remarkably small petal length (typically < 2.5 cm) and petal width (typically < 0.8 cm).",
    "Iris Versicolor": "Iris Versicolor has intermediate petal dimensions (petal length usually between 3.0 and 5.0 cm, petal width between 1.0 and 1.8 cm).",
    "Iris Virginica": "Iris Virginica possesses the largest petals among the three species (petal length typically > 4.8 cm and petal width > 1.6 cm)."
}

def get_model():
    """Load and cache the trained Decision Tree model."""
    global model, metadata
    if model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}. Train the model first.")
        model = joblib.load(MODEL_PATH)
        if os.path.exists(METADATA_PATH):
            metadata = joblib.load(METADATA_PATH)
        print(">> Decision Tree model loaded successfully into memory.")
    return model

@app.route("/", methods=["GET"])
def index():
    """API Root endpoint providing documentation and status."""
    return jsonify({
        "service": "Iris Flower Classification API",
        "description": "Decision Tree Machine Learning API integrated with n8n workflow automation",
        "model_type": "Decision Tree Classifier (Scikit-Learn)",
        "status": "online",
        "endpoints": {
            "GET /": "Service overview and documentation",
            "GET /health": "Health and readiness probe",
            "POST /predict": "Submit 4 measurements to obtain species prediction"
        },
        "expected_payload_example": {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    }), 200

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint for n8n or monitoring systems."""
    try:
        m = get_model()
        return jsonify({
            "status": "healthy",
            "model_loaded": m is not None,
            "algorithm": "DecisionTreeClassifier"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

@app.route("/predict", methods=["POST"])
def predict():
    """
    Main prediction endpoint.
    Accepts JSON payload with 4 numerical flower measurements.
    Returns predicted Iris species and confidence percentage.
    """
    if not request.is_json:
        # Check if received as form data
        data = request.form.to_dict() if request.form else None
        if not data:
            return jsonify({
                "status": "error",
                "error_type": "InvalidContentType",
                "message": "Request body must be valid JSON with Content-Type: application/json."
            }), 400
    else:
        data = request.get_json(silent=True)

    if not data or not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "error_type": "EmptyPayload",
            "message": "No input data provided or payload is empty."
        }), 400

    # Flexible key extraction to support various n8n Form trigger field names:
    # Handles: sepal_length, sepalLength, Sepal Length, Sepal Length (cm)
    def extract_val(keys):
        for k in keys:
            if k in data and data[k] is not None and str(data[k]).strip() != "":
                return data[k]
        return None

    raw_sl = extract_val(["sepal_length", "sepalLength", "Sepal Length", "Sepal Length (cm)", "sepal_len"])
    raw_sw = extract_val(["sepal_width", "sepalWidth", "Sepal Width", "Sepal Width (cm)", "sepal_wid"])
    raw_pl = extract_val(["petal_length", "petalLength", "Petal Length", "Petal Length (cm)", "petal_len"])
    raw_pw = extract_val(["petal_width", "petalWidth", "Petal Width", "Petal Width (cm)", "petal_wid"])

    # 1. Validation: Missing measurement check
    missing_fields = []
    if raw_sl is None: missing_fields.append("Sepal Length")
    if raw_sw is None: missing_fields.append("Sepal Width")
    if raw_pl is None: missing_fields.append("Petal Length")
    if raw_pw is None: missing_fields.append("Petal Width")

    if missing_fields:
        return jsonify({
            "status": "error",
            "error_type": "MissingFields",
            "message": f"Missing required measurements: {', '.join(missing_fields)}.",
            "details": "All four measurements (Sepal Length, Sepal Width, Petal Length, Petal Width) are mandatory."
        }), 400

    # 2. Validation: Numeric conversion check
    try:
        sl = float(raw_sl)
        sw = float(raw_sw)
        pl = float(raw_pl)
        pw = float(raw_pw)
    except (ValueError, TypeError):
        return jsonify({
            "status": "error",
            "error_type": "InvalidDataType",
            "message": "All measurements must be valid numeric numbers (integers or decimals).",
            "received_values": {
                "sepal_length": str(raw_sl),
                "sepal_width": str(raw_sw),
                "petal_length": str(raw_pl),
                "petal_width": str(raw_pw)
            }
        }), 400

    # 3. Validation: Positive numbers check
    if sl <= 0 or sw <= 0 or pl <= 0 or pw <= 0:
        return jsonify({
            "status": "error",
            "error_type": "NonPositiveValue",
            "message": "Flower measurements must be strictly positive numbers greater than 0.",
            "received_values": {
                "sepal_length": sl,
                "sepal_width": sw,
                "petal_length": pl,
                "petal_width": pw
            }
        }), 400

    # 4. Validation: Realistic botanical measurement check (0.1 cm to 25.0 cm)
    if sl > 25.0 or sw > 25.0 or pl > 25.0 or pw > 25.0:
        return jsonify({
            "status": "error",
            "error_type": "OutOfRealisticRange",
            "message": "Measurements exceed realistic biological limits for Iris flowers (max 25 cm).",
            "received_values": {
                "sepal_length": sl,
                "sepal_width": sw,
                "petal_length": pl,
                "petal_width": pw
            }
        }), 400

    # 5. Predict using the trained Decision Tree model
    try:
        m = get_model()
        feature_columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
        df_input = pd.DataFrame([[sl, sw, pl, pw]], columns=feature_columns)

        pred_class_id = int(m.predict(df_input)[0])
        probabilities = m.predict_proba(df_input)[0]
        confidence = round(float(probabilities[pred_class_id]) * 100, 2)
        predicted_species = SPECIES_MAP.get(pred_class_id, "Unknown Species")
        explanation = SPECIES_EXPLANATIONS.get(predicted_species, "Prediction determined by Decision Tree splitting rules.")

        response_payload = {
            "status": "success",
            "predicted_species": predicted_species,
            "model": "Decision Tree Classifier",
            "confidence_percentage": confidence,
            "submitted_measurements": {
                "sepal_length": sl,
                "sepal_width": sw,
                "petal_length": pl,
                "petal_width": pw
            },
            "class_probabilities": {
                SPECIES_MAP[i]: round(float(prob) * 100, 2)
                for i, prob in enumerate(probabilities)
            },
            "explanation": explanation,
            "attribution": "Prediction orchestrated by n8n workflow and computed by Scikit-learn Decision Tree Model"
        }

        return jsonify(response_payload), 200

    except Exception as exc:
        return jsonify({
            "status": "error",
            "error_type": "PredictionError",
            "message": f"An error occurred while evaluating the model: {str(exc)}"
        }), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "status": "error",
        "error_type": "NotFound",
        "message": "The requested endpoint was not found on this server."
    }), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({
        "status": "error",
        "error_type": "InternalServerError",
        "message": "An internal server error occurred."
    }), 500

if __name__ == "__main__":
    # Load model on startup
    get_model()
    port = int(os.environ.get("PORT", 5000))
    print(f">> Starting Iris Prediction API on http://127.0.0.1:{port} (all interfaces 0.0.0.0)")
    app.run(host="0.0.0.0", port=port, debug=False)
