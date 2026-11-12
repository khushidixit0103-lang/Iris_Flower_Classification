# Comprehensive Viva Examination Questions & Answers (35 Questions)

This document contains 35 high-yield viva questions with clear, simple, MCA-level answers to help you excel in your project examination.

---

### Category 1: Artificial Intelligence & Machine Learning Fundamentals

#### Q1. What is Artificial Intelligence (AI)?
**Answer:** Artificial Intelligence is the broad field of computer science focused on creating systems capable of performing tasks that typically require human intelligence, such as visual perception, decision-making, pattern recognition, and speech understanding.

#### Q2. What is Machine Learning (ML), and how is it related to AI?
**Answer:** Machine Learning is a specific subset of AI that enables computer systems to automatically learn and improve from experience and data without being explicitly programmed with hardcoded rules for every scenario.

#### Q3. What is Supervised Learning?
**Answer:** Supervised Learning is a machine learning paradigm where the algorithm is trained on a labeled dataset. The model is given both input features ($X$) and correct ground-truth outputs ($y$), learning a mathematical mapping function between them.

#### Q4. What is the difference between Classification and Regression?
**Answer:** 
- **Classification** predicts discrete, categorical class labels (e.g., classifying a flower as Setosa, Versicolor, or Virginica).
- **Regression** predicts continuous numerical quantities (e.g., predicting temperature or house price).

#### Q5. What is the Iris Dataset, and why is it famous in AI?
**Answer:** The Iris dataset, introduced by Ronald Fisher in 1936, contains 150 samples of Iris flowers across 3 species (Setosa, Versicolor, Virginica), with 4 measurements each. It is the premier benchmark dataset in machine learning because it is clean, balanced, and perfectly illustrates linear and non-linear classification boundaries.

---

### Category 2: Decision Tree Algorithm

#### Q6. What is a Decision Tree Classifier?
**Answer:** A Decision Tree is a supervised machine learning classifier that organizes decision rules into an inverted tree structure. It makes predictions by answering a sequence of threshold questions about feature values, starting at the root and traversing down to a leaf.

#### Q7. What is the Root Node?
**Answer:** The Root Node is the very first and top-most decision node of the tree. It contains the entire training dataset (all 120 training samples in our project) before any splits occur.

#### Q8. What is an Internal (Decision) Node?
**Answer:** An Internal or Decision Node is an intermediate node where a specific condition or question is evaluated (e.g., *"Is petal length $\le 2.45$ cm?"*). It has outgoing branches corresponding to `True` and `False` outcomes.

#### Q9. What is a Leaf Node?
**Answer:** A Leaf Node (or terminal node) is an endpoint of the tree that has no further branches. It represents the final predicted classification label (e.g., Iris Setosa).

#### Q10. What is Gini Impurity, and how is it used?
**Answer:** Gini Impurity measures how mixed or "impure" the classes are at a given node. 
A Gini score of $0.0$ means the node is purely of one class. 
The algorithm selects splits that minimize the weighted Gini impurity of the child nodes.

#### Q11. What is the difference between Gini Impurity and Entropy?
**Answer:** Both measure impurity. Entropy uses logarithmic calculations (Information Gain) based on Shannon's information theory, whereas Gini Impurity uses squared probabilities. Gini is computationally faster and requires less CPU overhead, which is why it is the default in Scikit-learn.

#### Q12. What is Overfitting, and how did you prevent it in your Decision Tree?
**Answer:** Overfitting occurs when a model memorizes the training data, including its random noise, leading to poor performance on new data. We prevented overfitting by setting `max_depth=4`, which stops the tree from growing indefinitely.

---

### Category 3: Model Training & Evaluation Metrics

#### Q13. Why do we perform a Train-Test Split?
**Answer:** If we evaluate a model on the same data it was trained on, we cannot verify whether it has truly learned general patterns or merely memorized answers. Splitting data into training (80%) and testing (20%) sets allows us to evaluate generalization on unseen data.

#### Q14. What does `random_state=42` mean?
**Answer:** `random_state` is a seed for the pseudo-random number generator. Setting a fixed value like `42` ensures that data shuffling and splitting are completely deterministic and reproducible every time the script is executed.

#### Q15. What is Accuracy in Machine Learning?
**Answer:** Accuracy is the ratio of correctly predicted instances to the total number of evaluated instances:
$$\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}}$$
Our model achieved **93.33% accuracy** on the 30 test samples.

#### Q16. What is a Confusion Matrix?
**Answer:** A Confusion Matrix is a tabular layout that visualizes the performance of a classification model. Each row represents instances in an actual class, while each column represents instances in a predicted class. It clearly exposes exactly where errors or confusions occur.

#### Q17. What information does a Classification Report provide?
**Answer:** A classification report provides three key metrics for each class:
- **Precision**: Of all samples predicted as class $X$, what fraction was actually class $X$?
- **Recall**: Of all actual samples of class $X$, what fraction was correctly identified?
- **F1-Score**: The harmonic mean of precision and recall: $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$.

#### Q18. Why was Iris Setosa 100% accurate while Versicolor and Virginica had minor errors?
**Answer:** Iris Setosa is linearly separable from the other two species—all Setosa specimens have petal lengths below 2.45 cm. However, Versicolor and Virginica share overlapping petal length and width regions between 4.8 cm and 5.0 cm, leading to 1 misclassification in each class.

---

### Category 4: Python & Microservice Architecture

#### Q19. What is Scikit-learn?
**Answer:** Scikit-learn is an open-source Python library for machine learning. It provides efficient tools for data preprocessing, model selection, classification, regression, clustering, and performance metrics.

#### Q20. What is Joblib, and why is it used instead of Pickle?
**Answer:** Joblib is a set of tools for lightweight pipelining and object serialization in Python. It is especially optimized for NumPy arrays and Scikit-learn models, providing faster disk storage and memory loading than standard Pickle.

#### Q21. What is an API (Application Programming Interface)?
**Answer:** An API is a software intermediary that allows two separate programs to communicate with each other using standardized protocols and data formats (such as HTTP and JSON).

#### Q22. What is Flask, and why did you choose it over Django or FastAPI?
**Answer:** Flask is a lightweight Python WSGI micro-framework. It was chosen because it has minimal boilerplate, is easy for beginners to understand, starts in milliseconds, and is ideal for wrapping a machine learning model into a REST API.

#### Q23. What is JSON (JavaScript Object Notation)?
**Answer:** JSON is a lightweight, human-readable data-interchange format composed of key-value pairs and arrays. It is the universal standard for exchanging data between web services and APIs.

#### Q24. What is CORS (Cross-Origin Resource Sharing)?
**Answer:** CORS is a security mechanism enforced by web browsers to restrict web pages from making requests to a different domain or port than the one serving the page. We enabled `flask_cors` so that n8n and browser clients can freely communicate with our API.

---

### Category 5: n8n Workflow Automation

#### Q25. What is n8n?
**Answer:** n8n is an open-source, fair-code workflow automation tool. It allows developers to connect disparate APIs, databases, webhooks, and services visually using nodes and automated trigger sequences.

#### Q26. What is the role of n8n in your project?
**Answer:** n8n acts as the primary user interaction and workflow orchestration engine. It renders the input form, validates submitted measurements, calls the Python prediction API over HTTP, and formats the output into an attractive HTML card for the user.

#### Q27. What is a Form Trigger node in n8n?
**Answer:** A Form Trigger node is an n8n node that automatically generates a hosted web form with customized fields. When a user fills out the form and submits it, the form submission triggers workflow execution and passes the form data to downstream nodes.

#### Q28. What does `responseMode: "lastNode"` mean in the Form Trigger?
**Answer:** It instructs n8n to wait until the entire workflow completes and return the output generated by the final node directly to the user's browser, displaying immediate prediction results without refreshing.

#### Q29. What is an HTTP Request node in n8n?
**Answer:** An HTTP Request node sends web requests (GET, POST, PUT, DELETE) to external services. In our project, it sends an HTTP POST request containing the flower measurements to the Python prediction endpoint `http://127.0.0.1:5000/predict`.

#### Q30. Why did you include an Input Validation node in n8n if Python also validates?
**Answer:** This follows the **defense-in-depth** software design principle. Validating inputs at the n8n orchestrator level provides immediate feedback to the user and avoids unnecessary network calls for invalid data. Server-side validation in Python provides a second security boundary against direct API tampering.

---

### Category 6: Technical Integration & Operations

#### Q31. How do Python and n8n communicate in your system?
**Answer:** They communicate through standard HTTP REST protocols over TCP/IP. n8n issues an HTTP POST request with a JSON payload to `http://127.0.0.1:5000/predict`. The Flask server processes the request, computes the prediction, and replies with an HTTP 200 OK JSON response.

#### Q32. Can n8n run locally or in the cloud?
**Answer:** n8n can run both locally (via Node.js/npm or Docker on `http://localhost:5678`) and in the cloud (n8n Cloud). If using n8n Cloud, a local API must be exposed via a secure tunnel (e.g. Cloudflare Tunnel or ngrok) so cloud servers can reach port 5000 on the local laptop.

#### Q33. What happens if the Python API is temporarily offline when a user submits the form?
**Answer:** In Node 4 (HTTP Request), we configured `onError: "continueRegularOutput"`. If the API is unreachable, n8n captures the network error and displays a friendly error card stating that the Python service is offline, rather than crashing or freezing.

#### Q34. What is Git and why is it used in this project?
**Answer:** Git is a distributed version control system that tracks changes in source code files over time. It allows developers to maintain revision histories, collaborate with team members, and publish code repositories to GitHub.

#### Q35. What is the main takeaway you learned from this project?
**Answer:** I learned that real-world AI is not just about model accuracy in a notebook; it is about building modular, maintainable systems where machine learning models are deployed as microservices and connected seamlessly with automated workflow platforms like n8n.
