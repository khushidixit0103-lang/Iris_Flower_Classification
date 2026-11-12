"""
Iris Flower Classification - Decision Tree Model Training
=========================================================
Academic Project: Artificial Intelligence Third Assessment
Student: MCA 7th Semester
Dataset: Built-in Scikit-learn Iris Dataset

This script performs end-to-end Machine Learning training:
1. Loads and inspects the Iris dataset
2. Checks dimensions and missing values
3. Splits into 80% Train and 20% Test sets (random_state=42)
4. Trains a DecisionTreeClassifier
5. Evaluates model performance (Accuracy, Confusion Matrix, Classification Report)
6. Saves the trained model and feature/target metadata using joblib
7. Generates a tree visualization image saved to disk
"""

import os
import sys
import numpy as np
import pandas as pd
import joblib
import matplotlib
matplotlib.use('Agg')  # Headless mode for server / script execution
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main():
    print("=" * 70)
    print("  IRIS FLOWER CLASSIFICATION - DECISION TREE TRAINING")
    print("=" * 70)

    # 1. Load Iris Dataset from Scikit-learn
    print("\n[Step 1] Loading built-in Iris dataset from scikit-learn...")
    iris = load_iris()

    feature_names = iris.feature_names
    target_names = iris.target_names

    print(f"Features: {feature_names}")
    print(f"Target Species: {list(target_names)}")

    # 2. Convert to Pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=feature_names)
    df['target'] = iris.target
    df['species'] = df['target'].apply(lambda x: target_names[x])

    # 3. Display first five records
    print("\n[Step 2] Displaying First 5 Records:")
    print(df.head())

    # 4. Check Dataset Dimensions
    print("\n[Step 3] Dataset Dimensions:")
    print(f"Rows (Samples): {df.shape[0]}, Columns: {df.shape[1]}")
    print(f"Class Distribution:\n{df['species'].value_counts()}")

    # 5. Check for Missing Values
    print("\n[Step 4] Checking for Missing (Null) Values:")
    missing = df.isnull().sum()
    print(missing)
    if missing.sum() == 0:
        print(">> No missing values detected. Dataset is clean and ready.")

    # 6. Separate input features (X) and target labels (y)
    X = df[feature_names]
    y = df['target']

    # 7. Split into 80% Training and 20% Testing (random_state=42)
    print("\n[Step 5] Splitting dataset: 80% Training, 20% Testing (random_state=42)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples:  {X_test.shape[0]}")

    # 8. Train the Decision Tree Classifier
    print("\n[Step 6] Training DecisionTreeClassifier...")
    # criterion='gini' is standard for classification, max_depth=4 prevents overfitting
    dt_classifier = DecisionTreeClassifier(
        criterion='gini',
        max_depth=4,
        random_state=42
    )
    dt_classifier.fit(X_train, y_train)
    print(">> Model training completed successfully!")

    # 9. Predict on Test Data
    print("\n[Step 7] Evaluating Model on Unseen Test Data...")
    y_pred = dt_classifier.predict(X_test)

    # 10. Calculate Actual Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_percentage = accuracy * 100
    print(f"\n>> ACTUAL MODEL ACCURACY: {accuracy_percentage:.2f}% ({accuracy:.4f})")

    # 11. Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print("\n[Step 8] Confusion Matrix:")
    print(pd.DataFrame(cm, index=[f"Actual {s}" for s in target_names],
                          columns=[f"Pred {s}" for s in target_names]))

    # 12. Classification Report
    print("\n[Step 9] Classification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))

    # 13. Save Trained Model and Metadata
    output_dir = os.path.join(os.path.dirname(__file__), "saved_model")
    os.makedirs(output_dir, exist_ok=True)

    model_filepath = os.path.join(output_dir, "iris_decision_tree_model.joblib")
    metadata_filepath = os.path.join(output_dir, "model_metadata.joblib")

    model_bundle = {
        'model': dt_classifier,
        'feature_names': feature_names,
        'target_names': list(target_names),
        'accuracy': accuracy,
        'criterion': 'gini',
        'max_depth': 4,
        'random_state': 42
    }

    joblib.dump(dt_classifier, model_filepath)
    joblib.dump(model_bundle, metadata_filepath)

    print(f"\n[Step 10] Model saved to: {model_filepath}")
    print(f"[Step 10] Metadata saved to: {metadata_filepath}")

    # 14. Visualize and Save Decision Tree Diagram
    print("\n[Step 11] Generating Decision Tree Diagram...")
    plt.figure(figsize=(14, 8), dpi=300)
    plot_tree(
        dt_classifier,
        feature_names=feature_names,
        class_names=target_names,
        filled=True,
        rounded=True,
        fontsize=10
    )
    plt.title("Decision Tree Visualization - Iris Flower Classification", fontsize=14, weight='bold')

    diagram_path = os.path.join(output_dir, "decision_tree_visualization.png")
    plt.savefig(diagram_path, bbox_inches='tight')
    plt.close()
    print(f">> Tree visualization saved to: {diagram_path}")

    # Copy diagram to screenshots directory as well for easy viva demo
    screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    shutil_target = os.path.join(screenshots_dir, "decision_tree_structure.png")
    import shutil
    shutil.copyfile(diagram_path, shutil_target)
    print(f">> Copy saved to screenshots folder: {shutil_target}")

    print("\n" + "=" * 70)
    print(f" TRAINING AND EVALUATION COMPLETED WITH ACCURACY: {accuracy_percentage:.2f}%")
    print("=" * 70)

    return accuracy

if __name__ == "__main__":
    main()
