# Workflow Explanation: n8n Node-by-Node Walkthrough

This document details the configuration, logic, and operational behavior of every node in the n8n workflow for faculty presentation.

---

## 1. Complete Workflow Topology

```
+-----------------------------------+
|       Node 1: Form Trigger        |
|  - Title: Iris Flower System      |
|  - 4 Numeric Measurement Fields   |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|     Node 2: Input Validation      |
|  - JavaScript Code Node           |
|  - Checks non-null, >0, & <=25cm  |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|      Node 3: Is Input Valid?      |
|  - If Node (Condition check)      |
+--------+-----------------+--------+
         | (True)          | (False)
         v                 v
+------------------+  +-------------------------------+
| Node 4: HTTP Req |  | Format Validation Error Node  |
| - POST to :5000  |  | - Displays error list card    |
+--------+---------+  +-------------------------------+
         |
         v
+-----------------------------------+
|    Node 5: Result Processing      |
| - Parses species & confidence     |
| - Generates stylized HTML card    |
+-----------------------------------+
```

---

## 2. Detailed Node Descriptions

### Node 1: Form Trigger (`n8n-nodes-base.formTrigger`)
- **Node Identifier**: `iris-classify-form`
- **User Role**: Provides the public web interface accessible via browser URL.
- **Fields Configured**:
  1. `Sepal Length (cm)` (Field Type: `number`, Required: `true`)
  2. `Sepal Width (cm)` (Field Type: `number`, Required: `true`)
  3. `Petal Length (cm)` (Field Type: `number`, Required: `true`)
  4. `Petal Width (cm)` (Field Type: `number`, Required: `true`)
- **Key Setting**: `responseMode: "lastNode"`. This critical configuration ensures that the browser receives the output of the final processing node rather than a generic "Form submitted" message.

### Node 2: Input Validation & Sanitization (`n8n-nodes-base.code`)
- **Node Identifier**: `Node 2: Input Validation`
- **Language**: JavaScript (executed within n8n's sandbox engine).
- **Core Logic**:
  ```javascript
  const sl = parseFloat(item["Sepal Length (cm)"] ?? item.sepal_length);
  // Rejects NaN, numbers <= 0, and numbers > 25
  ```
- **Output**: Attaches a boolean `isValid` flag and an array of descriptive error strings.

### Node 3: Conditional Branching (`n8n-nodes-base.if`)
- **Node Identifier**: `Is Input Valid?`
- **Logic**: Evaluates `{{ $json.isValid }} == true`.
- **True Path**: Routes to Node 4 to initiate prediction.
- **False Path**: Routes to the error formatting node to display guidance to the user.

### Node 4: HTTP Request (`n8n-nodes-base.httpRequest`)
- **Node Identifier**: `Node 3: HTTP Request`
- **HTTP Method**: `POST`
- **URL**: `http://127.0.0.1:5000/predict`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "sepal_length": "={{ $json.sepal_length }}",
    "sepal_width": "={{ $json.sepal_width }}",
    "petal_length": "={{ $json.petal_length }}",
    "petal_width": "={{ $json.petal_width }}"
  }
  ```
- **Error Resilience**: `onError: continueRegularOutput`. If the Python API is stopped or unreachable, execution continues without breaking, allowing Node 5 to catch the error.

### Node 5: Result Processing (`n8n-nodes-base.code`)
- **Node Identifier**: `Node 4: Result Processing`
- **Role**: Transforms raw JSON into an attractive user-facing presentation.
- **Output Formatting**:
  - Dynamically assigns species emojis (🌸 for Setosa, 🌿 for Versicolor, 🪻 for Virginica).
  - Displays confidence score percentage with a colored badge.
  - Generates a neat 2-column table summarizing the submitted input parameters.
  - Inserts botanical context explaining why the decision tree classified the flower as that species.
