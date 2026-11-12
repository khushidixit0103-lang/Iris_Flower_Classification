# n8n Workflow Guide: Iris Flower Classification

This directory contains the complete exported workflow JSON file: `iris_classification_workflow.json`.

## Workflow Overview

The n8n workflow orchestrates the entire user interaction and machine learning prediction lifecycle:

```
[Form Trigger] ➔ [Input Validation] ➔ [Is Valid?] ➔ [HTTP Request to Python API] ➔ [Result Processing & Display]
                                            ↓ (Invalid)
                               [Validation Error Response]
```

### Node Details

1. **Node 1: Form Trigger (`n8n-nodes-base.formTrigger`)**
   - **Title**: `🌸 Iris Flower Classification System`
   - **Fields**:
     - `Sepal Length (cm)` (Number, Required)
     - `Sepal Width (cm)` (Number, Required)
     - `Petal Length (cm)` (Number, Required)
     - `Petal Width (cm)` (Number, Required)
   - **Description**: Displays instructions and prompts the user to enter flower dimensions.
   - **Response Mode**: `lastNode` (Renders the formatted result directly to the user in the browser).

2. **Node 2: Input Validation (`n8n-nodes-base.code`)**
   - Parses the submitted measurements as floating-point numbers.
   - Rejects non-numeric, empty, or negative values.
   - Checks biological boundary limit (max 25 cm).
   - Generates clean, user-friendly error messages if validation fails.

3. **Node 3: Is Input Valid? (`n8n-nodes-base.if`)**
   - Routes valid requests (True branch) to the HTTP Request node.
   - Routes invalid requests (False branch) to the Validation Error Formatter.

4. **Node 4: HTTP Request (`n8n-nodes-base.httpRequest`)**
   - **Method**: `POST`
   - **URL**: `http://127.0.0.1:5000/predict`
   - **Headers**: `Content-Type: application/json`
   - **Payload**:
     ```json
     {
       "sepal_length": "={{ $json.sepal_length }}",
       "sepal_width": "={{ $json.sepal_width }}",
       "petal_length": "={{ $json.petal_length }}",
       "petal_width": "={{ $json.petal_width }}"
     }
     ```
   - Gracefully handles API connection issues with `onError: continueRegularOutput`.

5. **Node 5: Result Processing (`n8n-nodes-base.code`)**
   - Parses the JSON response from the Python model API.
   - Extracts `predicted_species`, `confidence_percentage`, `submitted_measurements`, and botanical explanations.
   - Constructs an HTML response card complete with flower emoji, badges, structured summary table, and machine learning model attribution.

---

## How to Import and Run the Workflow in n8n

### Option A: Local n8n Instance (Recommended)
1. Ensure the Python API is running on `http://127.0.0.1:5000`:
   ```bash
   venv\Scripts\python.exe api/app.py
   ```
2. Open your local n8n interface at `http://localhost:5678`.
3. In the left sidebar, click **Workflows** ➔ **Add Workflow** (or **+**).
4. Click the three dots `...` (Workflow Settings) in the top right corner.
5. Select **Import from File** and choose `n8n/iris_classification_workflow.json` (or copy-paste the JSON).
6. Click **Save** and toggle the workflow to **Active**.
7. Open the Form URL provided by the Form Trigger node (e.g. `http://localhost:5678/form/iris-classify`).
8. Enter measurements and click **Classify Iris Flower**.

### Option B: n8n Cloud Instance
If you are running on n8n Cloud (`https://<your-instance>.app.n8n.cloud`), n8n's cloud servers cannot directly reach `localhost:5000` on your laptop. You can securely expose your local Python API using one of these free, trusted tunnels:
- **Cloudflare Tunnel (cloudflared)**: `cloudflared tunnel --url http://localhost:5000`
- **ngrok**: `ngrok http 5000`
- **LocalTunnel**: `npx localtunnel --port 5000`

Then, in Node 3 (HTTP Request), update the URL from `http://127.0.0.1:5000/predict` to your secure public tunnel URL (e.g. `https://<your-subdomain>.trycloudflare.com/predict`).
