# Project Explanation: Guide for Faculty Presentation

**Project Title**: Iris Flower Classification Using n8n and Decision Tree Machine Learning  
**Target Audience**: Academic Faculty, External Examiners, Project Guides  
**Tone**: Confident, Beginner-Friendly, Technically Sound  

---

## 1. High-Level Summary (The 30-Second Elevator Pitch)

> *"Good morning respected faculty. My project is 'Iris Flower Classification Using n8n and Decision Tree Machine Learning'. In this project, I have built an end-to-end AI solution that classifies an Iris flower into one of three species—Setosa, Versicolor, or Virginica—based on four morphological measurements: Sepal Length, Sepal Width, Petal Length, and Petal Width. 
> 
> Rather than relying on simple command-line scripts or notebooks, I have connected an authentic Scikit-learn Decision Tree model (achieving 93.33% actual accuracy) to a Python Flask REST API, and integrated it with an n8n workflow automation platform. Non-technical users can open a clean web form, input measurements, and immediately view the predicted species, confidence score, and botanical explanation."*

---

## 2. Why is This Project Important?

1. **Practical Machine Learning Integration**: In real-world industry scenarios, ML models are rarely run in Jupyter Notebooks. They must be packaged as microservices and integrated into business workflow automation tools. This project demonstrates that enterprise-level integration pattern.
2. **Interpretability**: The Decision Tree model is completely transparent. We can visually inspect every decision threshold that the computer used to reach its conclusion.
3. **Dual-Layer Validation**: Both the n8n orchestrator and the Python REST API enforce strict data integrity, preventing invalid or malicious inputs from reaching the classifier.

---

## 3. How the Project Works (The Three Pillars)

### Pillar 1: Machine Learning (Python & Scikit-learn)
- Uses the built-in Iris dataset (150 samples across 3 species).
- Splits into 80% training (120 samples) and 20% testing (30 samples) with `random_state=42`.
- Trains a `DecisionTreeClassifier` with `criterion='gini'` and `max_depth=4`.
- Achieves **93.33% evaluation accuracy**.
- Saves the trained model using `joblib`.

### Pillar 2: Microservice API (Flask & REST)
- Loads the trained model file into memory.
- Exposes `/predict` (POST) and `/health` (GET).
- Validates data types, missing fields, positive values, and realistic biological limits.
- Returns clean JSON with species name, confidence score, and explanation.

### Pillar 3: Workflow Automation (n8n)
- Serves as the user-facing interface via a Form Trigger node.
- Validates inputs in JavaScript before transmission.
- Sends an HTTP POST request to the Python API.
- Formats the JSON response into a rich HTML result card with icons, badges, and tables.
