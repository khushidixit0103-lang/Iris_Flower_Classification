# System Architecture: Iris Flower Classification System

This document outlines the detailed system architecture, component interaction patterns, and data flow pipelines for the **Iris Flower Classification System**.

---

## 1. High-Level Architecture Diagram

```
+-----------------------------------------------------------------------------------+
|                                  USER BROWSER                                     |
|               Enters: Sepal Length, Sepal Width, Petal Length, Petal Width        |
+----------------------------------------+------------------------------------------+
                                         |
                                         | HTTP GET / POST (Form Submission)
                                         v
+-----------------------------------------------------------------------------------+
|                        n8n WORKFLOW AUTOMATION PLATFORM                           |
|                                                                                   |
|  [Node 1: Form Trigger]                                                           |
|       Displays interactive web form & collects user measurements                  |
|          |                                                                        |
|          v                                                                        |
|  [Node 2: Input Validation & Sanitization (JavaScript)]                           |
|       Checks non-null, numeric data types, positive values (>0), & bounds (<=25)  |
|          |                                                                        |
|          v                                                                        |
|  [Node 3: Is Input Valid? (Conditional Router)]                                   |
|       ├── If Valid: Routes to Node 4                                              |
|       └── If Invalid: Routes to Format Validation Error Node                      |
|          |                                                                        |
|          v (Valid)                                                                |
|  [Node 4: HTTP Request Node]                                                      |
|       Constructs JSON payload & sends POST request to http://127.0.0.1:5000/predict|
|          |                                                                        |
|          v                                                                        |
|  [Node 5: Result Processing & Display]                                            |
|       Extracts species, confidence, & creates formatted HTML response card        |
+----------------------------------------+------------------------------------------+
                                         |
                                         | HTTP POST (JSON Payload)
                                         v
+-----------------------------------------------------------------------------------+
|                            PYTHON REST API (Flask)                                |
|                               Port: 5000                                          |
|                                                                                   |
|  - Server: Flask with CORS Enabled                                                |
|  - Endpoint: POST /predict                                                        |
|  - Endpoint: GET /health                                                          |
|  - Server-side Schema Validation & Type Casting                                   |
|  - Dynamic Species Map & Botanical Explanations                                   |
+----------------------------------------+------------------------------------------+
                                         |
                                         | Memory Inference
                                         v
+-----------------------------------------------------------------------------------+
|                      SCIKIT-LEARN DECISION TREE MODEL                             |
|                                                                                   |
|  - Serialized File: model/saved_model/iris_decision_tree_model.joblib             |
|  - Algorithm: DecisionTreeClassifier (Gini, max_depth=4, random_state=42)         |
|  - Actual Accuracy: 93.33%                                                       |
|  - Input: [Sepal Length, Sepal Width, Petal Length, Petal Width]                  |
|  - Output: Class ID (0, 1, or 2) & Confidence Probabilities                       |
+-----------------------------------------------------------------------------------+
```

---

## 2. Component Communication Matrix

| Source Component | Target Component | Protocol | Payload Format | Description |
|---|---|---|---|---|
| User Browser | n8n Form Trigger | HTTP / HTTPS | Web Form Fields | User enters four physical flower dimensions in centimeters |
| n8n (Node 3) | Python Flask API | HTTP POST | JSON (`application/json`) | Transmits validated numeric measurements to `/predict` |
| Python Flask API | Serialized Model | Python in-memory call | Pandas DataFrame | Passes 4-column feature row to `model.predict()` |
| Serialized Model | Python Flask API | Python in-memory call | NumPy Arrays | Returns integer class index (`0, 1, 2`) and probability array |
| Python Flask API | n8n (Node 4) | HTTP 200 OK (JSON) | JSON (`application/json`) | Returns predicted species, confidence percentage, and explanation |
| n8n (Node 5) | User Browser | HTTP HTML Response | Styled HTML Card | Displays final result card with species name, emoji, and explanation |

---

## 3. Data Flow and Error Boundary Architecture

To ensure robustness, validation is applied at two distinct tiers:

### Tier 1: Client/Orchestrator Validation (n8n Node 2)
- Prevents unnecessary network calls if fields are missing.
- Rejects negative numbers or text strings entered in number inputs.
- Displays immediate visual error warnings on the form.

### Tier 2: Server-Side Validation (Flask API `app.py`)
- Guards against malformed JSON or direct API attacks.
- Enforces strict numeric bounds ($0.1 \le \text{measurement} \le 25.0$ cm).
- Returns structured HTTP 400 Bad Request JSON payloads with error type and message.

This dual-layer validation guarantees that no invalid data can reach the Scikit-learn model.
