# **Assignment 05 – Transfer Learning**

The dataset used in this assignment is large and cannot be hosted on GitHub. Download it from the following link:  
https://mega.nz/folder/rmAhyS4Q#LTT6PWC8HcRR7eW74NZu8A

### Dataset Details
- `Problem01_DuckChicken_Dataset`: Raw downloaded image data (duck and chicken images collected from the internet)
- `Problem01_RawData`: Processed and cleaned dataset used for **image classification (duck vs chicken)**
- `Problem02_Dataset`: Dataset used for **text sentiment classification (positive, neutral, negative)**


## Problem 01. **Transfer Learning for Image Data using CNN**
**Task**: Build a image classification model with three classes: `Duck` and `Chicken`

### Step 1: Data Collection (Problem01_DataDownloading)

- Images of ducks and chickens were collected from the internet
- Automated downloading was performed using scripts (e.g., web scraping / image search APIs)
- Around:
  - 100 duck images
  - 100 chicken images
- Raw data was stored in `Problem01_RawData`

### Step 2: Data Preprocessing

- Removed corrupted and irrelevant images
- Resized images to a fixed shape
- Organized into class-wise folders (duck / chicken) into train, test and validation dataset
- Final cleaned dataset stored in `Problem01_DuckChicken_Dataset`

### Step 3: Model Training using Transfer Learning

- Loaded a pre-trained CNN model (e.g., ResNet, VGG, MobileNet)
- Replaced final classification layer for binary classification
- Fine-tuned the model on the dataset

### Step 4: Evaluation

- Model was evaluated on validation/test data

### Output:

- Classification report including:
  - Precision
  - Recall
  - F1-score
  - Accuracy
- **Sample Classification including example image, classification probability and classified class**



## Problem 02. **Transfer Learning for Text Data using Transformer**

**Task:** Build a sentiment classification model with three classes:`Positive`, `Neutral` and `Negative`
**Dataset**: https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset


### Steps

- Load and preprocess the dataset
- Clean and tokenize text data
- Use a pre-trained transformer model (e.g., BERT, DistilBERT)
- Fine-tune the model on the dataset
- Evaluate model performance

### Output

- Classification report including:
  - Precision
  - Recall
  - F1-score
  - Accuracy
- **Sample Classification including example text, classification probability and classified class**