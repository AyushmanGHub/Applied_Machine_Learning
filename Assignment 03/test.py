import joblib
from score import score
import requests
import subprocess
import time

# Load trained model once for testing
MODEL_PATH = "BestModel_NaiveBayes.pkl"
model = joblib.load(MODEL_PATH)

def test_score():
    """
    Unit tests for score() function.
    """
    message = "Hello, this is a simple test message."

    # 1. Smoke test: Does it run without crashing?
    prediction, propensity = score(message, model, 0.5)

    assert prediction is not None
    assert propensity is not None
    
    # 2. Format test: Are outputs in expected format?
    # Note: score() must return bool(propensity > threshold) to pass this.
    assert isinstance(prediction, bool), f"Prediction must be bool, got {type(prediction)}"
    assert isinstance(propensity, float), f"Propensity must be float, got {type(propensity)}"

    # 3. Sanity check
    assert prediction in [True, False], "Prediction must be True or False"
    assert 0 <= propensity <= 1, "Propensity must be between 0 and 1"

    # 4. Edge case: threshold = 0, always predict True
    pred_zero, _ = score("Random message", model, 0)
    assert pred_zero is True, "Threshold 0 should always predict True"

    # 5. Edge case: threshold = 1, always predict False
    pred_one, _ = score("Random message", model, 1)
    assert pred_one is False, "Threshold 1 should always predict False"

    # 6. Typical spam inputs
    spam_text = "Congratulations! You won a free lottery ticket. Click now!"
    assert score(spam_text, model, 0.5)[0] is True

    # 7. Typical ham input
    ham_text = "Hey, are we meeting tomorrow for lunch?"
    assert score(ham_text, model, 0.5)[0] is False


def test_flask():
    """
    Integration test for Flask /score endpoint

    This test starts the Flask app in a separate process, sends requests to the app,
    and checks the responses to ensure that the app is working correctly.
    """

    # 01. Start the Flask app in a separate process
    process = subprocess.Popen(["python", "app.py"])

    time.sleep(2) # Give server time to start - 2 or 3 seconds

    try: 
        # Test the /home endpoint
        response = requests.get("http://127.0.0.1:5000/")
        assert response.status_code == 200
        assert "Spam Classifier" in response.text

        # 2️. Sending POST request
        response = requests.post(
            "http://127.0.0.1:5000/score",
            json={"text": "Congratulations! You won a free lottery ticket!"}
        )

        assert response.status_code == 200
        data = response.json()

        assert "prediction" in data
        assert "propensity" in data

        assert isinstance(data["prediction"], int)
        assert isinstance(data["propensity"], float)

        assert data["prediction"] in [0, 1]
        assert 0 <= data["propensity"] <= 1

    finally:
        # 03. closing  Flask app
        process.terminate()
        process.wait()