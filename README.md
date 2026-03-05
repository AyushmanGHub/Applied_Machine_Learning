# Applied Machine Learning (AML)
This repository contains the Assignments of my `Applied Machine Learning (AML)` in 4th semester(Jan-May)

## **Assignment 01 - SMS spam classification**
 This project is an end-to-end SMS spam classification pipeline, including text preprocessing, feature extraction, model training, hyperparameter tuning, and evaluation. Multiple models were used (Naive Bayes, Logistic Regression, Random Forest) each are benchmarked using Accuracy, Recall, Precision, F1-score,etc to select the best-performing classifier.
> Go to the `Assignment 01` folder to know more about it


## **Assignment 02 – Experiment Tracking & Version Control**

This project implements a reproducible Machine Learning pipeline using **DVC for data version control** and **MLflow for experiment tracking and model versioning**. Multiple dataset splits were generated using different random seeds and tracked with DVC, while three benchmark models (Naive Bayes, Logistic Regression, Random Forest) were trained and evaluated using AUCPR. All experiments and model versions were logged and registered to ensure full reproducibility and traceability.
> Go to the `Assignment 02` folder to know more about it


## **Assignment 03 – Testing & Model Serving**

This project focuses on testing and deploying the SMS spam classification model. A `score()` function was implemented and validated using comprehensive unit tests with `pytest`. The model was then served through a **Flask API** with a `/score` endpoint returning prediction and propensity in JSON format. An integration test was created to automatically launch the server, test the endpoint, and shut it down. Test coverage was generated using `pytest-cov` to ensure reliability.
> Go to the `Assignment 03` folder to know more about it

## **Assignment 04 – Containerization & Continuous Integration**

This project containerizes the SMS spam classification Flask API using **Docker**. A Docker image was built with a `Dockerfile` that installs dependencies and runs the Flask app. Automated tests were written to build the container, send a request to the `/score` endpoint, and validate the response. Test coverage was generated using `pytest-cov`, and a **pre-commit Git hook** was added to automatically run tests before every commit.
> Go to the `Assignment 04` folder to know more about it