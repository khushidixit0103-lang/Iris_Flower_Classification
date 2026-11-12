"""
Comprehensive Test Script for Iris Flower Classification API
=============================================================
Runs unit and integration tests against all test scenarios required
in the project specification.
"""

import sys
import time
import json
import urllib.request
import urllib.error
import subprocess
import os

API_URL = "http://127.0.0.1:5000"

def run_tests():
    print("=" * 60)
    print("  RUNNING COMPREHENSIVE IRIS API INTEGRATION TESTS")
    print("=" * 60)

    test_results = []

    def make_post(endpoint, payload):
        url = f"{API_URL}{endpoint}"
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req) as resp:
                status_code = resp.getcode()
                body = json.loads(resp.read().decode("utf-8"))
                return status_code, body
        except urllib.error.HTTPError as e:
            status_code = e.code
            body = json.loads(e.read().decode("utf-8"))
            return status_code, body

    def make_get(endpoint):
        url = f"{API_URL}{endpoint}"
        try:
            with urllib.request.urlopen(url) as resp:
                status_code = resp.getcode()
                body = json.loads(resp.read().decode("utf-8"))
                return status_code, body
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode("utf-8"))

    # Test 0: Health Check
    print("\n[Test 0] Checking GET /health ...")
    code, res = make_get("/health")
    passed = code == 200 and res.get("status") == "healthy"
    test_results.append(("Health Check", passed, f"Status {code}, healthy={res.get('status')}"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> {res}")

    # Test 1: Iris Setosa
    print("\n[Test 1] Testing Iris Setosa (5.1, 3.5, 1.4, 0.2) ...")
    code, res = make_post("/predict", {
        "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2
    })
    passed = code == 200 and res.get("predicted_species") == "Iris Setosa"
    test_results.append(("Iris Setosa Test", passed, f"Status {code}, Species: {res.get('predicted_species')}"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> {res.get('predicted_species')} (Confidence: {res.get('confidence_percentage')}%)")

    # Test 2: Iris Versicolor
    print("\n[Test 2] Testing Iris Versicolor (6.0, 2.7, 4.0, 1.2) ...")
    code, res = make_post("/predict", {
        "sepal_length": 6.0, "sepal_width": 2.7, "petal_length": 4.0, "petal_width": 1.2
    })
    passed = code == 200 and res.get("predicted_species") == "Iris Versicolor"
    test_results.append(("Iris Versicolor Test", passed, f"Status {code}, Species: {res.get('predicted_species')}"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> {res.get('predicted_species')} (Confidence: {res.get('confidence_percentage')}%)")

    # Test 3: Iris Virginica
    print("\n[Test 3] Testing Iris Virginica (6.9, 3.1, 5.4, 2.1) ...")
    code, res = make_post("/predict", {
        "sepal_length": 6.9, "sepal_width": 3.1, "petal_length": 5.4, "petal_width": 2.1
    })
    passed = code == 200 and res.get("predicted_species") == "Iris Virginica"
    test_results.append(("Iris Virginica Test", passed, f"Status {code}, Species: {res.get('predicted_species')}"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> {res.get('predicted_species')} (Confidence: {res.get('confidence_percentage')}%)")

    # Test 4: Missing measurement (petal_width omitted)
    print("\n[Test 4] Testing Missing Measurement ...")
    code, res = make_post("/predict", {
        "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4
    })
    passed = code == 400 and res.get("status") == "error" and "Missing required measurements" in res.get("message", "")
    test_results.append(("Missing Measurement Validation", passed, f"Status {code}, Error: {res.get('message')}"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> Status {code}: {res.get('message')}")

    # Test 5: Invalid text input ("abc")
    print("\n[Test 5] Testing Invalid Text Input ...")
    code, res = make_post("/predict", {
        "sepal_length": "five", "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2
    })
    passed = code == 400 and res.get("status") == "error" and "valid numeric numbers" in res.get("message", "")
    test_results.append(("Invalid Text Input Validation", passed, f"Status {code}, Error: {res.get('message')}"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> Status {code}: {res.get('message')}")

    # Test 6: Negative measurement (-1.4)
    print("\n[Test 6] Testing Negative Measurement ...")
    code, res = make_post("/predict", {
        "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": -1.4, "petal_width": 0.2
    })
    passed = code == 400 and res.get("status") == "error" and "strictly positive" in res.get("message", "")
    test_results.append(("Negative Measurement Validation", passed, f"Status {code}, Error: {res.get('message')}"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> Status {code}: {res.get('message')}")

    # Test 7: API Unavailable simulation
    print("\n[Test 7] Testing Non-Existent Endpoint / Unavailable Response ...")
    code, res = make_get("/non_existent_endpoint_for_test")
    passed = code == 404
    test_results.append(("Unavailable/404 Handling", passed, f"Status {code} returned gracefully"))
    print(f"Result: {'PASS' if passed else 'FAIL'} -> Status {code}")

    print("\n" + "=" * 60)
    print("                 TEST SUMMARY REPORT")
    print("=" * 60)
    all_passed = True
    for name, ok, detail in test_results:
        symbol = "[PASS]" if ok else "[FAIL]"
        if not ok: all_passed = False
        print(f"{symbol:7} | {name:32} | {detail}")

    print("=" * 60)
    if all_passed:
        print(">> ALL 8 TEST CASES PASSED SUCCESSFULLY!")
    else:
        print(">> SOME TESTS FAILED. CHECK DETAILS ABOVE.")
    print("=" * 60)
    return all_passed

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
