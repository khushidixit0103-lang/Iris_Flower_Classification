"""
Iris Flower Classification - Standalone Prediction Script
=========================================================
Loads the trained Decision Tree model and performs classification
on given measurements. Can be run from CLI or imported as a module.
"""

import os
import sys
import joblib
import pandas as pd

MODEL_DIR = os.path.join(os.path.dirname(__file__), "saved_model")
MODEL_PATH = os.path.join(MODEL_DIR, "iris_decision_tree_model.joblib")
METADATA_PATH = os.path.join(MODEL_DIR, "model_metadata.joblib")

SPECIES_MAP = {
    0: "Iris Setosa",
    1: "Iris Versicolor",
    2: "Iris Virginica"
}

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}. Please run train_model.py first.")
    model = joblib.load(MODEL_PATH)
    return model

def predict_species(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    """
    Predict Iris species given 4 measurements in cm.
    """
    model = load_model()
    features = [[float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]]
    feature_columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    df_input = pd.DataFrame(features, columns=feature_columns)

    pred_class = int(model.predict(df_input)[0])
    probabilities = model.predict_proba(df_input)[0]

    species_name = SPECIES_MAP.get(pred_class, f"Unknown ({pred_class})")

    result = {
        "predicted_class_id": pred_class,
        "predicted_species": species_name,
        "confidence": round(float(probabilities[pred_class]) * 100, 2),
        "class_probabilities": {
            SPECIES_MAP[i]: round(float(prob) * 100, 2)
            for i, prob in enumerate(probabilities)
        },
        "input_features": {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        },
        "model": "Decision Tree Classifier (Scikit-learn)"
    }
    return result

if __name__ == "__main__":
    print("-" * 50)
    print("Iris Model CLI Prediction Test")
    print("-" * 50)

    # Test cases:
    test_samples = [
        ("Setosa Test", 5.1, 3.5, 1.4, 0.2),
        ("Versicolor Test", 6.0, 2.7, 4.0, 1.2),
        ("Virginica Test", 6.9, 3.1, 5.4, 2.1)
    ]

    for label, sl, sw, pl, pw in test_samples:
        res = predict_species(sl, sw, pl, pw)
        print(f"[{label}] Input: SL={sl}, SW={sw}, PL={pl}, PW={pw}")
        print(f"  -> Predicted: {res['predicted_species']} (Confidence: {res['confidence']}%)")
        print()
