# SMS Spam Classification – Applied Machine Learning Project

## Problem Statement

Short Message Service (SMS) spam poses a significant problem for users by causing inconvenience, privacy risks, and potential financial fraud. Manually filtering spam messages is inefficient and error-prone due to the high volume of messages generated daily.
The objective of this project is to build an automated machine learning system that can accurately classify SMS messages as **spam** or **ham (non-spam)**.


## Solution Overview

This project presents an end-to-end **machine learning–based SMS spam classification system**. The solution preprocesses raw SMS text, converts it into numerical features, trains multiple classification models, and evaluates them using appropriate metrics for imbalanced data. The best-performing model is selected based on test-set performance.

## About the Project

<div style="border:2px solid #3344ffff; padding:10px; border-radius:8px; overflow-x:auto; width:100%; box-sizing:border-box;">

### How the Project Works

1. **Data Loading & Preprocessing**

   * SMS messages are cleaned and normalized.
   * Labels are encoded (`0 = ham`, `1 = spam`).
   * The dataset is split into **train, validation, and test** sets.

2. **Feature Extraction and EDA**

   * Text data is transformed using **Bag-of-Words and TF-IDF** representations.
   * This converts unstructured text into numerical vectors suitable for machine learning models.

3. **Model Training**

   * Three benchmark models are trained:

     * Naive Bayes
     * Logistic Regression
     * Random Forest
   * Hyperparameters are tuned using **cross-validation** on the training data.

4. **Evaluation & Model Selection** - Models are evaluated using Accuracy, Precision, Recall, F1-score, PR-AUC, and Special focus is placed on **F1-score and PR-AUC** due to class imbalance.
</div>

## Best Model and Why

### **Best model based on results and Industrial use: `Naive Bayes`**

**Why? —**  
- Naive Bayes is more suitable for spam detection and real-world deployment due to its **perfect precision**, **low inference latency**, and **minimal risk of false positives**.  
- Although its F1-score is slightly lower than Logistic Regression, **precision is prioritized** because misclassifying legitimate (ham) messages as spam is more harmful than allowing some spam messages to pass through.  
- From an industry perspective, Naive Bayes provides **fast, scalable, and interpretable predictions**, making it well-suited for real-time message filtering systems.  
- Logistic Regression, while strong in overall metrics, exhibits lower precision, increasing the risk of false positives, whereas Random Forest shows signs of **overfitting** and does not generalize well on unseen data.

> A two-stage filtering strategy can further balance spam reduction with user trust and operational safety.


## What Was the Problem and How This Project Solves It

**Problem:**

* High volume of SMS messages makes manual spam detection impractical.
* Spam messages often mimic legitimate content, making rule-based systems ineffective.

**Solution:**

* The project applies supervised machine learning to automatically learn patterns in spam messages.
* By leveraging text vectorization and robust evaluation metrics, the system accurately distinguishes spam from legitimate messages.
* The final model generalizes well to unseen data, making it suitable for real-world deployment.


## Industrial Applications

This SMS spam classification system has wide real-world applicability:

* **Telecom Providers:** Automatic filtering of spam SMS before delivery.
* **Mobile Operating Systems:** Built-in spam detection for messaging apps.
* **Banking & Finance:** Blocking phishing and fraud-related SMS.
* **E-commerce Platforms:** Filtering promotional or scam messages.
* **Customer Support Systems:** Prioritizing legitimate user messages.