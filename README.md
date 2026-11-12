# 🌸 Iris Flower Classification Using n8n and Decision Tree Machine Learning

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.1-orange.svg)](https://scikit-learn.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-black.svg)](https://flask.palletsprojects.com/)
[![n8n](https://img.shields.io/badge/n8n-Workflow%20Automation-FF6D5A.svg)](https://n8n.io/)
[![Accuracy](https://img.shields.io/badge/Accuracy-93.33%25-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-Academic%20Assessment-lightgrey.svg)]()

> **Master of Computer Applications (MCA) — 7th Semester**  
> **Artificial Intelligence: Third Assessment**  
> **Student**: MCA Student  

---

## 📌 Project Overview

This project presents an end-to-end Artificial Intelligence classification system that identifies Iris flower species (*Iris Setosa*, *Iris Versicolor*, or *Iris Virginica*) based on four morphological measurements:
1. **Sepal Length (cm)**
2. **Sepal Width (cm)**
3. **Petal Length (cm)**
4. **Petal Width (cm)**

Unlike traditional implementations restricted to offline Jupyter notebooks, this project connects an authentic **Scikit-learn Decision Tree Classifier** to a **Python Flask REST API** and orchestrates the user interaction through an **n8n workflow automation platform**.

---

## 🏛️ System Architecture

```
+-------------------------------------------------------------+
|                      USER INTERFACE                         |
|         n8n Form Trigger (Browser Web Form)                 |
|    Fields: Sepal Length, Sepal Width, Petal Length, Width   |
+------------------------------+------------------------------+
                               |
                               | HTTP POST (JSON Payload)
                               v
+-------------------------------------------------------------+
|                   n8n WORKFLOW ENGINE                       |
|   1. Form Trigger Node: Captures user input                 |
|   2. Input Validation Node: Verifies numeric & positive     |
|   3. If Condition Node: Routes valid / invalid paths        |
|   4. HTTP Request Node: Dispatches to Python API (:5000)    |
|   5. Result Processing Node: Formats rich HTML result card  |
+------------------------------+------------------------------+
                               |
                               | REST API Request (Port 5000)
                               v
+-------------------------------------------------------------+
|                   PYTHON FLASK REST API                     |
|                   Endpoint: POST /predict                   |
|                   Endpoint: GET /health                     |
|   - Server-side Schema & Boundary Validation                |
|   - Loads Serialized Model into Memory                      |
+------------------------------+------------------------------+
                               |
                               | In-Memory Prediction
                               v
+-------------------------------------------------------------+
|              SCIKIT-LEARN DECISION TREE MODEL               |
|            Serialized: iris_decision_tree_model.joblib      |
|            Actual Evaluation Accuracy: 93.33%               |
+-------------------------------------------------------------+
```

---

## 📊 Model Performance & Actual Evaluation Results

The Decision Tree model was trained using a stratified 80% training / 20% testing split with `random_state=42` on the 150-sample Iris dataset.

- **Actual Test Accuracy**: **93.33%** (28/30 test samples correctly classified)
- **Training Samples**: 120
- **Testing Samples**: 30
- **Hyperparameters**: `criterion='gini'`, `max_depth=4`, `random_state=42`

### Confusion Matrix:
| Actual \ Predicted | Predicted Setosa | Predicted Versicolor | Predicted Virginica |
|---|---|---|---|
| **Actual Setosa** | **10** | 0 | 0 |
| **Actual Versicolor** | 0 | **9** | 1 |
| **Actual Virginica** | 0 | 1 | **9** |

### Classification Report:
| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| **Iris Setosa** | 1.00 (100%) | 1.00 (100%) | 1.00 | 10 |
| **Iris Versicolor** | 0.90 (90%) | 0.90 (90%) | 0.90 | 10 |
| **Iris Virginica** | 0.90 (90%) | 0.90 (90%) | 0.90 | 10 |
| **Overall Accuracy** | | | **0.93 (93.33%)** | **30** |

---

## 📁 Project Directory Structure

```
Iris-Flower-Classification/
├── model/
│   ├── train_model.py                     # Machine Learning training & evaluation script
│   ├── predict.py                         # Standalone CLI prediction module
│   └── saved_model/
│       ├── iris_decision_tree_model.joblib # Serialized trained Decision Tree classifier
│       ├── model_metadata.joblib           # Training metadata and feature names
│       └── decision_tree_visualization.png # 300 DPI Decision tree diagram
├── api/
│   ├── app.py                             # Flask REST API microservice (Port 5000)
│   └── test_api.py                        # Automated integration test suite
├── n8n/
│   ├── iris_classification_workflow.json  # Complete exportable n8n workflow definition
│   └── README.md                          # n8n import & configuration instructions
├── documentation/
│   ├── Project_Report.md                  # Comprehensive academic project report
│   ├── Working_Procedure.md               # Step-by-step operational guide
│   ├── Algorithm_Explanation.md           # Decision Tree & Gini Impurity theory
│   └── System_Architecture.md             # Multi-tier architectural specifications
├── screenshots/
│   ├── decision_tree_structure.png        # Exported Decision Tree structure diagram
│   └── README.md                          # Screenshot instructions
├── requirements.txt                       # Python dependencies
├── README.md                              # Main project documentation
└── .gitignore                             # Standard Git ignore file
```

---

## 🚀 Quick Start & Demonstration Guide

### 1. Clone the Repository
```bash
git clone https://github.com/khushidixit0103-lang/Iris_Flower_Classification.git
cd Iris_Flower_Classification
```

### 2. Set Up Python Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. (Optional) Re-train the Model
The pre-trained model is already saved in `model/saved_model/`. To train it again:
```bash
python model/train_model.py
```

### 4. Start the Python REST API
```bash
python api/app.py
```
*The API will start on `http://127.0.0.1:5000`.*  
Verify in your browser by opening: `http://127.0.0.1:5000/health`.

### 5. Start n8n & Import Workflow
In a separate terminal:
```bash
npx n8n
# Or if installed globally:
n8n start
```
1. Open `http://localhost:5678` in your browser.
2. Navigate to **Workflows** ➔ **Import from File**.
3. Select `n8n/iris_classification_workflow.json`.
4. Click **Save** and toggle the workflow to **Active**.
5. Open the Form URL provided by the Form Trigger node.
6. Enter flower measurements and click **Classify Iris Flower**!

---

## 🧪 Verified Test Cases

| Test Case | Inputs (SL, SW, PL, PW) | Expected Result | Actual Verified Result | Status |
|---|---|---|---|---|
| **1. Iris Setosa** | `5.1, 3.5, 1.4, 0.2` | Iris Setosa (100%) | Iris Setosa (Confidence: 100%) | ✅ PASS |
| **2. Iris Versicolor** | `6.0, 2.7, 4.0, 1.2` | Iris Versicolor (100%) | Iris Versicolor (Confidence: 100%) | ✅ PASS |
| **3. Iris Virginica** | `6.9, 3.1, 5.4, 2.1` | Iris Virginica (100%) | Iris Virginica (Confidence: 100%) | ✅ PASS |
| **4. Missing Field** | `5.1, 3.5, 1.4, [None]` | 400 Bad Request | 400 Bad Request ("Missing required measurements: Petal Width") | ✅ PASS |
| **5. Invalid Text** | `"five", 3.5, 1.4, 0.2` | 400 Bad Request | 400 Bad Request ("All measurements must be valid numeric numbers") | ✅ PASS |
| **6. Negative Value** | `5.1, 3.5, -1.4, 0.2` | 400 Bad Request | 400 Bad Request ("Must be strictly positive numbers > 0") | ✅ PASS |
| **7. API Health** | `GET /health` | 200 OK Healthy | `{"status": "healthy", "model_loaded": true}` | ✅ PASS |
| **8. 404 Route** | `GET /invalid_path` | 404 Not Found | 404 JSON Error Handled Gracefully | ✅ PASS |

---

## 🎓 Academic Viva Questions & Presentation

For complete viva readiness:
- Review `viva/Viva_Questions.md` for **35 standard viva questions with simple explanations**.
- Practice the **3-5 minute presentation script** in `viva/Demonstration_Guide.md`.
- Review the **line-by-line code walkthrough** in `viva/Code_Explanation.md`.

---

## 📄 License & Attribution

This project is submitted in partial fulfillment of the **Artificial Intelligence Third Assessment** for the **MCA 7th Semester**. Open-source for academic and educational evaluation.
