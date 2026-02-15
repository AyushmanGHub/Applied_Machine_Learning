# Assignment 02 – Experiment Tracking & Version Control

## Problem Statement

This project focuses on implementing reproducible Machine Learning workflows using:

* **Data Version Control (DVC)** for dataset versioning
* **MLflow** for experiment tracking and model versioning

The tasks required:

### Data Version Control

* Track dataset versions in `prepare.ipynb` using DVC
* Save:

  * `raw_data.csv`
  * `train.csv`
  * `validation.csv`
  * `test.csv`
* Regenerate splits using different random seeds
* Checkout older data versions using DVC
* Compare target distribution (0s and 1s) across versions
* `bonus: (decouple compute and storage)` track the data versions using google drive as storage

### Model Version Control & Experiment Tracking

* Train 3 benchmark models in `train.ipynb`
* Track experiments using MLflow
* Log and register models
* Compare model selection metric (AUCPR)

## Solution Approach

### 🔹 Data Versioning with DVC

* Initialized Git + DVC repository
* Generated dataset splits using different random seeds: [2, 9, 13, 42, 123]

* Tracked dataset changes using:

  ```bash
  dvc add data/
  git commit
  ```
* Verified reproducibility by:

  ```bash
  git checkout <commit>
  dvc checkout
  ```
* Printed class distribution (0s & 1s) for each version
Each commit corresponds to a deterministic dataset split.


### 🔹 Model Versioning with MLflow

In `train.ipynb`:

* Trained 3 benchmark models:

  * Naive Bayes
  * Logistic Regression
  * Random Forest
* Logged:

  * `model_type`
  * `split_seed`
  * `AUCPR`
* Registered models under MLflow Model Registry
* Retrieved and printed AUCPR programmatically

---

### 🌩️ `bonus: (decouple compute and storage)` track the data versions using google drive as storage
> In `bonus (decouple compute and storage)` folder
In this part, as an additional enhancement, Google Drive was configured as a **DVC remote storage backend** to decouple compute and storage.

Instead of storing dataset versions only on the local machine:

* DVC tracks dataset versions locally (metadata via Git).
* Actual data versions (DVC cache objects) are stored remotely in Google Drive.
* Each data split version is pushed using `dvc push`.
* Data can be restored on any machine using `dvc pull`.

This demonstrates a production-style MLOps architecture where:

```
Local Machine → Compute Layer
Google Drive  → Storage Layer
```

The system ensures reproducibility, portability, and separation of concerns between data storage and model training.

---




## About the Project

This project demonstrates a complete reproducible ML pipeline:

```
Data Layer      → DVC (versioned datasets)
Model Layer     → MLflow (tracked experiments)
Version Control → Git
```

Key properties:

* Deterministic dataset splits
* Full data lineage tracking
* Experiment reproducibility
* Model comparison across data versions
* Clean separation of data and model versioning


## Results

### Git Log (Data Versions)

```
619453e Data split seed=123
1a82e84 Data split seed=42
3472277 Data split seed=13
3223923 Data split seed=9
b248a19 Data split seed=2
378476b Initialize DVC - Starting the run
```

### AUCPR Results Across Seeds

| Seed | Logistic Regression | Naive Bayes | Random Forest |
| ---- | ------------------- | ----------- | ------------- |
| 2    | 0.9718              | 0.9728      | **0.9781**    |
| 9    | 0.9801              | 0.9827      | **0.9851**    |
| 13   | 0.9878              | **0.9886**  | 0.9861        |
| 42   | 0.9729              | 0.9731      | **0.9790**    |
| 123  | 0.9822              | 0.9822      | **0.9853**    |



## Industrial Application

This workflow mirrors real-world MLOps systems:

* Data stored in versioned snapshots
* Experiments fully reproducible
* Models registered and tracked
* Ability to rollback data or models
* Clear separation between:

  * Data generation
  * Model training
  * Experiment evaluation

Such pipelines are used in:

* Fraud detection
* Spam classification
* Recommendation systems
* Financial risk modeling
* Healthcare prediction systems



## 🚀 Final Architecture

```
prepare.ipynb  → Data versioning (DVC)
train.ipynb    → Experiment tracking (MLflow)
Git            → Metadata version control
```

This project successfully implements reproducible ML experimentation with proper version control at both data and model levels.