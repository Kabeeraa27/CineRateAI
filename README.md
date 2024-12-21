# CineRateAI

This repository contains a machine learning model designed to predict movie ratings based on various features, such as movie title, rating, cast, and other movie-related information. The model uses a Random Forest Regressor and achieves an impressive accuracy of **99.7%**.

## Data Preprocessing

### 1. **Target Encoding and One-Hot Encoding**
To handle categorical variables, two encoding techniques were applied to the dataset:

- **Target Encoding**: Applied to categorical features where the target variable (rating) was encoded based on the mean target value for each category.
- **One-Hot Encoding**: Applied to categorical features to convert them into binary columns, allowing the model to learn from categorical data effectively.

### 2. **Additive Smoothing**
Additive smoothing was applied on the target encoding step to avoid zero probabilities for categories that did not appear in the training data. This ensures smoother results, especially when working with smaller datasets.

### 3. **Features Processed**
The following features were processed:
- `movie_title`
- `movie_info`
- `rating`
- `cast`
- `tomatometer_status`

These features were transformed using the mentioned encoding techniques to prepare them for model training.

## Model

### **Random Forest Regressor**
- A Random Forest Regressor was used as the model to predict movie ratings based on the features.
- **Best Accuracy**: The model achieved an accuracy of **99.7%**, making it highly reliable for predicting ratings.

## Requirements

- Python 3.x
- `pandas` for data manipulation
- `numpy` for numerical operations
- `scikit-learn` for model building and evaluation
- `joblib` for saving and loading models

## Installation

To install the required libraries, use the following:

```bash
pip install -r requirements.txt
