# Working Procedure: Step-by-Step Execution Guide

This document explains the exact working procedure of the **Iris Flower Classification System**, clearly detailing which component is executed by Python and which component is managed by n8n.

---

## 1. Division of Responsibilities

| Stage | Responsible Component | Technology | Description |
|---|---|---|---|
| **Data Ingestion & Cleaning** | Python Model Engine | Scikit-learn & Pandas | Loads Iris dataset, validates shape, checks null values |
| **Model Training & Evaluation** | Python Model Engine | Scikit-learn Decision Tree | Splits data (80/20), trains tree, computes 93.33% accuracy, saves `.joblib` |
| **Visualization Generation** | Python Model Engine | Matplotlib | Plots tree structure and saves high-resolution diagram |
| **REST API Microservice** | Python Web Service | Flask & Flask-CORS | Listens on port 5000, accepts JSON, validates inputs, returns prediction |
| **User Interface (Form)** | n8n Orchestrator | n8n Form Trigger | Collects 4 measurements from user in browser |
| **Input Validation & Sanity** | n8n Orchestrator | n8n JavaScript Node | Checks numeric bounds, non-null, and positive values |
| **Service Integration** | n8n Orchestrator | n8n HTTP Request Node | Sends measurements over HTTP to Flask API |
| **Result Presentation** | n8n Orchestrator | n8n Code Node (HTML) | Formats rich color-coded result card and displays to user |

---

## 2. Step-by-Step Execution Procedure

### Step 1: Environment Setup
1. A dedicated project folder `Iris_Flower_Classification` was established.
2. A Python virtual environment (`venv`) was created to isolate dependencies.
3. Required libraries (`scikit-learn`, `pandas`, `numpy`, `flask`, `flask-cors`, `joblib`, `matplotlib`) were installed.

### Step 2: Training the Decision Tree Model
1. Run the training script:
   ```bash
   venv\Scripts\python.exe model/train_model.py
   ```
2. The script loads the 150 Iris flower samples from Scikit-learn.
3. The dataset is split into 120 training samples and 30 testing samples using `random_state=42`.
4. The `DecisionTreeClassifier` is fitted on the training data.
5. The model achieves **93.33% accuracy** on the unseen test set.
6. The trained model is serialized to `model/saved_model/iris_decision_tree_model.joblib`.
7. A decision tree diagram is generated at `model/saved_model/decision_tree_visualization.png`.

### Step 3: Starting the Python REST API
1. Launch the Flask API server:
   ```bash
   venv\Scripts\python.exe api/app.py
   ```
2. The server loads the `.joblib` model into memory and binds to `http://127.0.0.1:5000`.
3. The API exposes:
   - `GET /health`: Health and readiness probe
   - `POST /predict`: Prediction endpoint

### Step 4: Running the n8n Workflow
1. Start n8n locally (`npx n8n` or `n8n start`) on `http://localhost:5678`.
2. Import `n8n/iris_classification_workflow.json`.
3. Activate the workflow.
4. Open the form URL in any web browser.

### Step 5: End-to-End Prediction Flow
1. **User Action**: The user inputs Sepal Length = 5.1, Sepal Width = 3.5, Petal Length = 1.4, Petal Width = 0.2 and clicks "Classify Iris Flower".
2. **n8n Validation**: Node 2 verifies that all four fields are positive floating-point numbers.
3. **HTTP Dispatch**: Node 4 sends the JSON payload to `http://127.0.0.1:5000/predict`.
4. **Python Prediction**: Flask receives the JSON, feeds it to `model.predict()`, and returns:
   ```json
   {
     "status": "success",
     "predicted_species": "Iris Setosa",
     "confidence_percentage": 100.0,
     "model": "Decision Tree Classifier"
   }
   ```
5. **n8n Response**: Node 5 formats a rich HTML card and presents the user with:
   - Species Name: **Iris Setosa** 🌸
   - Confidence: **100%**
   - Submitted measurements summary table
   - Botanical explanation
