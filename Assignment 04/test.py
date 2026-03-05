import requests
import subprocess
import time

MESSAGES = [
    "Project deadline is next Friday.",
    "Meeting tomorrow at 10 AM.",
    "Congratulations! You've won a free vacation!"
]

def test_docker():
    subprocess.run(["docker", "stop", "spam_classifier"], check=False)
    subprocess.run(["docker", "rm", "spam_classifier"], check=False)

    subprocess.run(["docker", "build", "-t", "flask-spam-classifier", "."], check=True)

    subprocess.run([
        "docker", "run", "-d",
        "-p", "5000:5000",
        "--name", "spam_classifier",
        "flask-spam-classifier"
    ], check=True)

    time.sleep(5)

    try:
        # Test home endpoint
        response = requests.get("http://127.0.0.1:5000/")
        assert response.status_code == 200

        # Test /score endpoint
        for message in MESSAGES:
            response = requests.post(
                "http://127.0.0.1:5000/score",
                json={"text": message}
            )
            assert response.status_code == 200
            data = response.json()

            assert "prediction" in data
            assert "propensity" in data

            assert isinstance(data["prediction"], bool)
            assert data["prediction"] in [True, False]

            assert isinstance(data["propensity"], float)
            assert 0 <= data["propensity"] <= 1

    finally:
        subprocess.run(["docker", "stop", "spam_classifier"])
        subprocess.run(["docker", "rm", "spam_classifier"])