# Code Explanation: Complete Line-by-Line Guide

This document breaks down every important code file in the project so you can confidently answer questions from faculty during your viva.

---

## 1. `model/train_model.py` Walkthrough

### 1.1 Loading the Dataset
```python
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].apply(lambda x: iris.target_names[x])
```
- **What it does**: Fetches the 150-sample Iris dataset built into Scikit-learn and wraps it in a Pandas DataFrame for structured exploration.
- **Why we do it**: DataFrames allow us to view tabular data, inspect column names, and check for missing values.

### 1.2 Train-Test Splitting
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
```
- **`test_size=0.20`**: Allocates 80% (120 samples) for training and reserves 20% (30 samples) for testing.
- **`random_state=42`**: Sets the random seed so the split is identical on every run (100% reproducible).
- **`stratify=y`**: Ensures each of the three species is proportionally represented in both the training set (40 each) and the testing set (10 each).

### 1.3 Decision Tree Classifier Training
```python
dt_classifier = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
    random_state=42
)
dt_classifier.fit(X_train, y_train)
```
- **`criterion='gini'`**: Uses Gini Impurity to measure the quality of a split.
- **`max_depth=4`**: Restricts the tree to a maximum depth of 4 levels to prevent overfitting.
- **`.fit(X_train, y_train)`**: Trains the decision rules on the feature vectors and known target labels.

### 1.4 Evaluation & Accuracy
```python
y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
```
- Compares the model's predictions on unseen test data (`y_pred`) with actual ground truth labels (`y_test`).
- Yields actual test accuracy of **93.33%**.

### 1.5 Model Serialization with Joblib
```python
joblib.dump(dt_classifier, model_filepath)
```
- Serializes the Python object to a binary file on disk. The API can load this file directly without retraining from scratch.

---

## 2. `api/app.py` Walkthrough

### 2.1 Lazy Model Loading
```python
def get_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)
    return model
```
- Loads the model into RAM on the first request and caches it, ensuring sub-millisecond prediction times for subsequent requests.

### 2.2 Input Extraction & Validation
```python
raw_sl = extract_val(["sepal_length", "sepalLength", "Sepal Length", "Sepal Length (cm)"])
...
if raw_sl is None: missing_fields.append("Sepal Length")
```
- Accommodates flexible naming variations from different n8n Form trigger node versions.
- Validates:
  1. Non-empty / non-missing
  2. Parses to valid float
  3. Strictly greater than 0
  4. Realistically $\le 25.0$ cm

### 2.3 Generating the Prediction & Probabilities
```python
pred_class_id = int(m.predict(df_input)[0])
probabilities = m.predict_proba(df_input)[0]
confidence = round(float(probabilities[pred_class_id]) * 100, 2)
```
- `m.predict()` returns the most probable class index (`0`, `1`, or `2`).
- `m.predict_proba()` calculates the exact probability distribution across all three species, allowing the API to return a confidence percentage.
