# import libraries
from flask import Flask, request, jsonify, render_template_string
import pickle
import joblib
from score import score
import warnings
import os


# # Initializing Flask app
app = Flask(__name__)

# Loading trained model
MODEL_PATH = "BestModel_NaiveBayes.pkl"
model = joblib.load(MODEL_PATH)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Spam Classifier</title>
    <style>
        body {
            background: linear-gradient(135deg, #121212, #1a1a1a);
            color: #ffffff;
            font-family: 'Segoe UI', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            flex-direction: column;
        }

        .container {
            background-color: rgba(30, 30, 30, 0.95);
            padding: 40px;
            border-radius: 14px;
            box-shadow: 0 0 25px rgba(0,0,0,0.6);
            text-align: center;
            width: 420px;
        }

        h1 {
            margin-bottom: 30px;
            letter-spacing: 1px;
        }

        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            border-radius: 8px;
            border: none;
            outline: none;
            font-size: 14px;
        }

        .button-group {
            display: flex;
            gap: 10px;
        }

        .reset-btn {
            flex: 1;
            padding: 12px;
            background-color: #555;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.2s ease;
        }

        .reset-btn:hover {
            background-color: #777;
        }

        input[type="submit"] {
            flex: 2;
            padding: 12px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.2s ease;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
            transform: translateY(-1px);
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            background-color: rgba(42, 42, 42, 0.9);
            border-radius: 12px;
            animation: fadeIn 0.4s ease-in-out;
        }

        .message-box {
            background-color: #2f2f2f;
            padding: 12px;
            border-radius: 8px;
            margin-top: 8px;
            word-wrap: break-word;
            font-size: 15px;
            color: #dddddd;
        }

        hr {
            border: 1px solid #444;
            margin: 20px 0;
        }

        .footer {
            margin-top: 25px;
            font-size: 14px;
            color: #aaaaaa;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Spam Classifier</h1>

    <form action="/score" method="post">
        <input type="text" name="text" placeholder="Enter text"
               value="{{ message if message else '' }}" required>

        <div class="button-group">
            <button type="button" onclick="window.location.href='/'" class="reset-btn">
                Reset
            </button>
            <input type="submit" value="Classify">
        </div>
    </form>

    {% if message %}
    <div class="result">

        <p><strong>Message:</strong></p>
        <div class="message-box">
            {{ message }}
        </div>

        <hr>

        <p><strong>Prediction (False/True):</strong> {{ prediction01 }}</p>

        <p><strong>Classification:</strong>
            <span style="color: {% if pred_value == 1 %}#ff4d4d{% else %}#4CAF50{% endif %};
                         font-weight: bold;">
                {{ prediction }}
            </span>
        </p>

        <p><strong>Propensity:</strong> {{ probability }}</p>

    </div>
    {% endif %}

    <div class="footer">
        Created by Ayushman Anupam
    </div>
</div>

</body>
</html>
"""



# Home route 
@app.route("/", methods=["GET"])
def home():
    return render_template_string(html, message=None)



# /score endpoint
# ----------------------------
@app.route("/score", methods=["POST"])
def score_endpoint():

    # Case (I) JSON request (used in integration test)
    if request.is_json:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        prediction, propensity = score(data["text"], model)

        return jsonify({
            "prediction": prediction,
            "propensity": propensity
        })

    # Case (2) Form submission (used by browser UI)
    text = request.form.get("text")

    if not text:
        return render_template_string(html, prediction=None)

    prediction, propensity = score(text, model)

    label = "Spam" if prediction else "Ham"

    return render_template_string(
        html,
        message=text,
        prediction01 = prediction,
        prediction=label,
        probability=round(propensity, 4)
    )



# run app
if __name__ == '__main__':    
    app.run(host="0.0.0.0", port=5000, debug=True)
