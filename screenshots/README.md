# Screenshots Directory

This directory contains visual assets and diagram captures for project demonstrations, presentations, and academic reporting.

## Included Files

1. **`decision_tree_structure.png`**
   - High-resolution (300 DPI) visualization of the trained Decision Tree model.
   - Generated directly by Scikit-learn's `plot_tree()` function during execution of `model/train_model.py`.
   - Illustrates:
     - **Root Node**: Evaluates `petal length (cm) <= 2.45` with Gini impurity of 0.667.
     - **Decision Nodes**: Intermediate splits on `petal width` and `petal length`.
     - **Leaf Nodes**: Terminal classification outcomes color-coded by class (Setosa, Versicolor, Virginica).

## How to Capture Additional Screenshots During Faculty Demo

When running the project live, you can capture and save the following screenshots to this directory for your records:

1. **`01_api_health.png`**: Browser capture of `http://127.0.0.1:5000/health` showing healthy status.
2. **`02_n8n_workflow_canvas.png`**: Full workflow canvas in n8n showing the connected 5 nodes.
3. **`03_n8n_form_input.png`**: The user-facing web form with the four measurement inputs.
4. **`04_prediction_result_setosa.png`**: Form response displaying the Iris Setosa result card.
5. **`05_prediction_result_versicolor.png`**: Form response displaying the Iris Versicolor result card.
6. **`06_prediction_result_virginica.png`**: Form response displaying the Iris Virginica result card.
7. **`07_validation_error_handling.png`**: The red warning card displayed when negative or text values are submitted.
