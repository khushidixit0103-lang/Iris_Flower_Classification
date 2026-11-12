# Demonstration Guide & 3-5 Minute Presentation Script

This document provides a timed, spoken presentation script and a step-by-step demonstration checklist for presenting the project to your faculty.

---

## 1. 3–5 Minute Presentation Script (Spoken Guide)

### Part 1: Introduction (0:00 - 0:45)
> *"Respected guide and faculty members, good morning. 
> 
> My name is [Your Name], an MCA 7th-semester student, and today I am pleased to present my Artificial Intelligence Third Assessment project: **'Iris Flower Classification Using n8n and Decision Tree Machine Learning'**.
> 
> The core problem I addressed is: How can we take an authentic machine learning classification model and make it seamlessly usable for non-technical users through modern low-code workflow automation?
> 
> To solve this, I combined a Scikit-learn Decision Tree model, a Python Flask microservice, and an n8n workflow engine."*

### Part 2: Machine Learning Model & Training (0:45 - 2:00)
> *"Let me first explain the machine learning model.
> 
> I used Ronald Fisher's classic Iris dataset from Scikit-learn, consisting of 150 instances of Iris flowers evenly divided into three species: Setosa, Versicolor, and Virginica. Each flower is described by four continuous measurements: Sepal Length, Sepal Width, Petal Length, and Petal Width.
> 
> To ensure genuine academic rigor, I performed an 80-20 stratified train-test split with `random_state=42` for reproducibility.
> 
> For the algorithm, I specifically selected the **Decision Tree Classifier** with Gini Impurity criterion and capped the maximum depth at 4 to prevent overfitting.
> 
> When evaluated on the 30 unseen test samples, the model achieved an actual accuracy of **93.33%**. Iris Setosa achieved 100% precision and recall because it is linearly separable by petal length, while Versicolor and Virginica achieved 90% each due to slight biological overlap in petal dimensions.
> 
> I serialized the trained model to disk using `joblib` and plotted the full visual tree structure."*

### Part 3: Python Microservice & n8n Integration (2:00 - 3:30)
> *"To make this model accessible, I built a lightweight Python REST API using Flask. The API loads the trained model into memory and exposes a `/predict` endpoint that validates inputs, checks for missing or non-positive measurements, and returns the predicted species, confidence percentage, and botanical explanation in JSON format.
> 
> On top of this API, I created an automated 5-node workflow in **n8n**:
> 1. First, an **n8n Form Trigger** generates a clean web interface where users can type the four measurements.
> 2. Second, an **Input Validation node** checks the values in JavaScript to ensure data integrity.
> 3. Third, an **If condition node** directs valid entries to our API.
> 4. Fourth, an **HTTP Request node** sends the data to our Python API.
> 5. Finally, a **Result Processing node** formats the prediction into an attractive HTML card complete with species icons, confidence badges, and summary tables.
> 
> This provides a complete separation of concerns: Python handles the AI computation, while n8n manages user interaction and workflow orchestration."*

### Part 4: Live Demonstration & Conclusion (3:30 - 4:30)
> *"Now, let me demonstrate a quick live test.
> 
> [DEMO STEP] If I enter Sepal Length = 5.1, Sepal Width = 3.5, Petal Length = 1.4, Petal Width = 0.2 and click Submit...
> 
> Within milliseconds, n8n orchestrates the API call, and we immediately see: **Iris Setosa** with **100% confidence**!
> 
> [DEMO STEP] If I test with negative or text inputs, the system catches the error gracefully.
> 
> In conclusion, this project demonstrates an enterprise-grade AI deployment pattern that is modular, transparent, and completely beginner-friendly. 
> 
> Thank you, and I am now ready to answer any questions."*

---

## 2. Step-by-Step Live Demonstration Checklist

Before your faculty arrives, ensure you have:
1. **Started the Python API**:
   ```bash
   venv\Scripts\python.exe api/app.py
   ```
   Confirm message: `>> Starting Iris Prediction API on http://127.0.0.1:5000`
2. **Opened the API in your browser**:
   Visit `http://127.0.0.1:5000/health` to demonstrate `{"status": "healthy"}`.
3. **Opened n8n Form**:
   Open the workflow form URL in Chrome or Edge.
4. **Prepared Test Inputs on a Notepad**:
   - **Setosa**: `5.1, 3.5, 1.4, 0.2` -> Result: *Iris Setosa (100% confidence)*
   - **Versicolor**: `6.0, 2.7, 4.0, 1.2` -> Result: *Iris Versicolor (100% confidence)*
   - **Virginica**: `6.9, 3.1, 5.4, 2.1` -> Result: *Iris Virginica (100% confidence)*
   - **Validation Error Test**: `5.1, 3.5, -1.0, 0.2` -> Result: *Input Validation Failed (Must be > 0)*
5. **Displayed Decision Tree Visualization**:
   Open `screenshots/decision_tree_structure.png` to explain the root node, decision nodes, and leaf nodes directly to your faculty.
