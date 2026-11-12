# Academic Project Report: Iris Flower Classification Using n8n and Decision Tree Machine Learning

**Academic Program**: Master of Computer Applications (MCA)  
**Semester**: 7th Semester  
**Course Assessment**: Artificial Intelligence — Third Assessment  
**Project Title**: Iris Flower Classification Using n8n and Decision Tree Machine Learning  
**Student Name**: MCA Student  
**Implementation Year**: 2026  

---

## 1. Introduction

Classification is one of the most foundational tasks in supervised machine learning. It involves training an algorithm on historical labeled data so that it can accurately assign category labels to newly observed, unseen instances. The Iris Flower Classification problem, first introduced by British statistician and biologist Ronald A. Fisher in 1936, remains the premier benchmark problem in pattern recognition, machine learning education, and botanical informatics.

In contemporary software engineering and enterprise environments, machine learning models do not exist in isolation. A machine learning model delivers real value only when it is integrated into automated workflows, connected to user interfaces, and capable of exchanging structured data through Application Programming Interfaces (APIs). 

This project bridges classical machine learning with modern low-code workflow automation by integrating a **Scikit-learn Decision Tree Classifier** with **n8n workflow automation** via a high-performance **Python REST API**.

---

## 2. Problem Statement

Botanists, agricultural researchers, and students frequently need to classify plant species based on morphological measurements of their flowers. Manually distinguishing between visually similar flower species, such as *Iris Versicolor* and *Iris Virginica*, is error-prone, subjective, and requires domain expertise.

Furthermore, traditional machine learning implementations often require end-users to interact with command-line interfaces or write Python scripts, which creates a significant barrier for non-programmers.

The challenge addressed by this project is:
> *How can we accurately classify Iris flower species using a machine learning Decision Tree model while providing an intuitive, interactive, and automated web form interface powered by n8n workflow automation?*

---

## 3. Objectives

The primary objectives of this assessment project are:
1. **Model Development**: Train an authentic Decision Tree Classification model on Fisher's Iris dataset using Python and Scikit-learn, adhering strictly to reproducible train-test split practices (`random_state=42`).
2. **Model Evaluation**: Comprehensively evaluate the classifier's predictive accuracy, confusion matrix, precision, recall, and F1-score.
3. **Model Persistence**: Serialize and save the trained Decision Tree model and associated metadata to disk using `joblib`.
4. **API Development**: Develop a lightweight, robust Python REST API using Flask to expose the model via HTTP endpoints (`/predict` and `/health`) with thorough input validation.
5. **Workflow Orchestration with n8n**: Design and execute an automated 5-node n8n workflow featuring a user-facing Form Trigger, input validation, HTTP communication with the Python API, result processing, and formatted response rendering.
6. **Academic Documentation & Viva Readiness**: Provide comprehensive documentation, architecture diagrams, code walk-throughs, and 30+ viva examination questions with plain-English explanations.

---

## 4. Dataset Description

The project utilizes the classic **Iris Dataset** built directly into Scikit-learn (`sklearn.datasets.load_iris`).

### Dataset Specifications:
- **Total Samples**: 150 flower specimens
- **Total Features (Input)**: 4 continuous numerical measurements (measured in centimeters)
- **Total Classes (Output)**: 3 distinct biological species (50 instances per class — perfectly balanced dataset)

### Feature Attributes:
1. **Sepal Length (cm)**: The longitudinal measurement of the flower's outermost protective calyx leaf. Range: 4.3 cm to 7.9 cm.
2. **Sepal Width (cm)**: The transverse measurement of the sepal across its widest portion. Range: 2.0 cm to 4.4 cm.
3. **Petal Length (cm)**: The longitudinal measurement of the inner, brightly colored flower petal. Range: 1.0 cm to 6.9 cm. (Key discriminatory feature).
4. **Petal Width (cm)**: The transverse measurement across the flower petal. Range: 0.1 cm to 2.5 cm. (Key discriminatory feature).

### Output Classes:
1. **Iris Setosa** (Class 0): Characterized by significantly smaller petals. Linearly separable from the other two species.
2. **Iris Versicolor** (Class 1): Displays intermediate petal dimensions.
3. **Iris Virginica** (Class 2): Displays the longest and widest petals among all three species.

---

## 5. Technologies Used

| Technology / Library | Version | Purpose in Project |
|---|---|---|
| **Python** | 3.14.8 | Core programming language for data preprocessing, training, and API service |
| **Scikit-learn** | 1.9.1 | Provides the Iris dataset, train-test splitting, DecisionTreeClassifier, and evaluation metrics |
| **Pandas** | 3.1.1 | Dataframe structures, dataset inspection, and data manipulation |
| **NumPy** | 2.5.4 | High-performance numerical computations and array operations |
| **Flask & Flask-CORS** | 3.1.3 | Lightweight WSGI web framework providing the REST API endpoints and cross-origin communication |
| **Joblib** | 1.6.0 | Model serialization and deserialization (`.joblib` format) |
| **Matplotlib** | 3.11.2 | Tree visualization and diagram export |
| **n8n** | Latest Local/Cloud | Primary workflow automation engine, Form UI provider, and orchestrator |
| **Git & GitHub** | 2.48.1 | Version control and public repository hosting |

---

## 6. Machine Learning Concepts

### 6.1 Supervised Learning
Machine learning is broadly categorized into supervised, unsupervised, and reinforcement learning. This project falls under **Supervised Learning** because the model is trained on labeled historical records where both the input measurements ($X$) and the true species labels ($y$) are known.

### 6.2 Classification vs. Regression
In machine learning:
- **Regression** predicts continuous numerical quantities (e.g., house price, temperature).
- **Classification** predicts discrete categorical class labels (e.g., Setosa, Versicolor, Virginica).
Since the Iris task assigns specimens to one of three discrete categories, it is a **multiclass classification problem**.

### 6.3 Train-Test Split & Overfitting Avoidance
To measure how well the model generalizes to completely new, unseen flower specimens, the dataset of 150 instances was split into:
- **80% Training Data** (120 instances): Used exclusively to construct the decision rules.
- **20% Testing Data** (30 instances): Held back and used exclusively for final evaluation.
Setting `random_state=42` ensures deterministic shuffling and complete reproducibility across computers.

---

## 7. Decision Tree Algorithm

### 7.1 What is a Decision Tree?
A Decision Tree is a non-parametric supervised learning algorithm that breaks down complex decision-making into a hierarchy of simple, interpretable questions about feature thresholds (e.g., *"Is petal length $\le 2.45$ cm?"*).

### 7.2 Key Tree Components:
1. **Root Node**: The very first split at the top of the tree containing all 120 training instances.
2. **Internal (Decision) Nodes**: Intermediate condition nodes where a specific feature is compared against a numeric split threshold.
3. **Branches**: The paths resulting from the decision condition (`True` leads left, `False` leads right).
4. **Leaf Nodes**: The terminal endpoints of the tree where no further splits occur. Each leaf node represents a final predicted class (*Setosa*, *Versicolor*, or *Virginica*).

### 7.3 Splitting Criterion: Gini Impurity
This project utilizes the **Gini Impurity** criterion:
$$I_G(p) = 1 - \sum_{i=1}^{C} p_i^2$$
where $C = 3$ is the number of classes and $p_i$ is the probability of an item belonging to class $i$.
- A Gini score of $0.0$ indicates a **pure node** (every sample belongs to exactly one class).
- The algorithm chooses the feature and threshold that maximizes Information Gain (i.e. minimizes weighted Gini impurity after the split).

### 7.4 Hyperparameter Selection
- `criterion='gini'`: Computationally efficient and standard for classification.
- `max_depth=4`: Caps tree growth to four levels, preventing the tree from memorizing training noise and thereby guarding against **overfitting**.
- `random_state=42`: Guarantees reproducibility.

---

## 8. System Architecture

The overall system architecture follows a decoupled, three-tier modular pattern:

```
+-------------------------------------------------------------+
|                     PRESENTATION TIER                       |
|          n8n Form Trigger (Browser Web Interface)           |
|      Inputs: Sepal Length, Sepal Width, Petal Length/Width  |
+------------------------------+------------------------------+
                               |
                               | HTTP POST (JSON Payload)
                               v
+-------------------------------------------------------------+
|                    ORCHESTRATION TIER                       |
|               n8n Workflow Automation Engine                |
|      - Form Trigger & Input Schema Enforcement              |
|      - JavaScript Input Validation & Sanity Verification    |
|      - Conditional Branching (Valid vs. Invalid)            |
|      - HTTP Request Dispatcher                              |
|      - Result Transformation & HTML Card Formatting         |
+------------------------------+------------------------------+
                               |
                               | REST API Request (Port 5000)
                               v
+-------------------------------------------------------------+
|                      APPLICATION TIER                       |
|               Python Flask Microservice (app.py)            |
|      - Endpoints: GET /, GET /health, POST /predict         |
|      - Strict Field & Range Validation                      |
|      - Loads Serialized Model into Memory                   |
+------------------------------+------------------------------+
                               |
                               | Memory Reference
                               v
+-------------------------------------------------------------+
|                     INTELLIGENCE TIER                       |
|          Scikit-Learn Decision Tree Classifier              |
|      - Serialized Model: iris_decision_tree_model.joblib     |
|      - Computes Predictions & Class Probabilities           |
+-------------------------------------------------------------+
```

---

## 9. Workflow Architecture (n8n)

The n8n workflow contains five dedicated nodes:

1. **Node 1: Form Trigger**
   - Renders a clean browser form with introductory text and four numeric fields.
   - Configured with `responseMode: "lastNode"` so the user sees results immediately after submission.
2. **Node 2: Input Validation**
   - JavaScript code node checking for missing values, non-numeric strings, negative numbers, and unrealistic values ($>25$ cm).
3. **Node 3: Conditional Branching (`If` Node)**
   - If inputs are valid, routes execution to Node 4.
   - If invalid, routes to the error formatting branch.
4. **Node 4: HTTP Request Node**
   - Transmits a POST request to `http://127.0.0.1:5000/predict` with JSON body.
   - Handles connection errors gracefully without breaking workflow execution.
5. **Node 5: Result Processing & Display**
   - Parses the JSON output from the Python API.
   - Assembles an attractive, color-coded HTML summary card containing the predicted species, confidence percentage, submitted values, and botanical explanations.

---

## 10. Implementation Details

### 10.1 Model Training Pipeline (`model/train_model.py`)
1. Imports Scikit-learn, Pandas, NumPy, and Matplotlib.
2. Loads `load_iris()` and casts into a Pandas DataFrame.
3. Performs exploratory inspection (`head()`, `shape`, `isnull().sum()`).
4. Performs an 80/20 stratified train-test split.
5. Instantiates `DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)`.
6. Fits model on `(X_train, y_train)` and predicts `y_pred` on `X_test`.
7. Computes actual accuracy, confusion matrix, and classification report.
8. Persists model using `joblib.dump()`.
9. Generates `decision_tree_visualization.png` using `plot_tree()`.

### 10.2 REST API Microservice (`api/app.py`)
1. Initializes Flask application with `CORS(app)`.
2. Implements lazy-loading model cache via `get_model()`.
3. Defines `/health` endpoint returning server and model readiness.
4. Defines `/predict` endpoint supporting both JSON and Form payloads.
5. Flexible feature name matching (supports `sepal_length`, `Sepal Length (cm)`, camelCase).
6. Multi-layer input validation (missing check, float parsing check, $>0$ check, $\le 25$ cm check).
7. Invokes model inference and calculates confidence percentage using `predict_proba()`.
8. Returns structured JSON containing predicted species, probabilities, and botanical explanation.

---

## 11. Results and Evaluation

The model was genuinely trained and evaluated on 30 test samples (20% of the dataset).

### Actual Experimental Metrics:
- **Accuracy**: **93.33%** (28 out of 30 test samples correctly classified)
- **Training Samples**: 120
- **Testing Samples**: 30

### Confusion Matrix:
| Actual Class \ Predicted | Predicted Setosa | Predicted Versicolor | Predicted Virginica |
|---|---|---|---|
| **Actual Setosa** | **10** | 0 | 0 |
| **Actual Versicolor** | 0 | **9** | 1 |
| **Actual Virginica** | 0 | 1 | **9** |

### Classification Report:
| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| **Setosa** | 1.00 (100%) | 1.00 (100%) | 1.00 | 10 |
| **Versicolor** | 0.90 (90%) | 0.90 (90%) | 0.90 | 10 |
| **Virginica** | 0.90 (90%) | 0.90 (90%) | 0.90 | 10 |
| **Overall Accuracy** | | | **0.93 (93.33%)** | **30** |
| **Macro Average** | 0.93 | 0.93 | 0.93 | 30 |
| **Weighted Average** | 0.93 | 0.93 | 0.93 | 30 |

### Key Analytical Findings:
1. **Iris Setosa** achieves **100% precision and recall**. It is completely linearly separable from the other two species because its petal length is always less than 2.45 cm.
2. **Iris Versicolor** and **Iris Virginica** have a small region of overlap where petal length is between 4.8 and 5.0 cm, resulting in 1 sample from each class being misclassified.
3. A 93.33% test accuracy demonstrates strong generalization without overfitting.

---

## 12. Advantages of the Proposed System

1. **Clear Separation of Concerns**: Python handles mathematical training and model execution; n8n handles workflow orchestration, user interface, and integration.
2. **High Explainability**: Unlike black-box neural networks, Decision Trees are fully transparent and auditable. Every decision corresponds to a human-readable rule.
3. **Zero Coding Required for End Users**: Non-technical users can interact with the machine learning model through a clean web form without touching Python code.
4. **Resilient Error Handling**: Invalid measurements, non-numeric values, negative numbers, or missing parameters are intercepted and reported with friendly messages before reaching the model.
5. **Enterprise-Ready Extensibility**: Because predictions are exposed as a REST API, other enterprise applications, mobile apps, or databases can consume the same endpoint simultaneously.

---

## 13. Limitations

1. **Fixed Botanical Domain**: The current model is trained exclusively on the 3 species in Fisher's Iris dataset. It cannot classify other flowering plant species.
2. **Feature Dependency**: The model requires all four measurements. If a damaged specimen lacks a petal or sepal, classification cannot proceed.
3. **Axis-Parallel Splits**: Decision Trees make splits perpendicular to coordinate axes, which can sometimes produce stepped approximations rather than smooth decision boundaries.

---

## 14. Future Scope

1. **Automated Retraining**: Implement an automated n8n webhook schedule that collects new authenticated botanical data and triggers periodic model retraining.
2. **Computer Vision Enhancement**: Integrate image classification (Convolutional Neural Networks) so users can simply upload a photograph of an Iris flower instead of taking physical ruler measurements.
3. **Database Integration**: Connect the n8n workflow to PostgreSQL, MongoDB, or Google Sheets to automatically archive all user submissions and prediction histories.

---

## 15. Conclusion

This project successfully implemented an end-to-end, automated AI classification system for Iris flowers. By combining a Scikit-learn Decision Tree model (achieving an actual evaluation accuracy of **93.33%**) with a Flask REST API microservice and an n8n workflow automation engine, the system bridges the gap between academic machine learning and practical, accessible software solutions. 

The modular architecture, robust validation layers, reproducible training pipeline, and comprehensive documentation fully satisfy all requirements for the MCA 7th Semester Artificial Intelligence Assessment.

---

## 16. References

1. Fisher, R. A. (1936). *The use of multiple measurements in taxonomic problems*. Annals of Eugenics, 7(2), 179-188.
2. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.
3. Breiman, L., Friedman, J. H., Olshen, R. A., & Stone, C. J. (1984). *Classification and Regression Trees*. Wadsworth & Brooks/Cole Advanced Books & Software.
4. n8n Documentation. *n8n - Free and open fair-code workflow automation tool*. https://docs.n8n.io/
5. Flask Documentation (v3.1). *Pallets Projects*. https://flask.palletsprojects.com/
