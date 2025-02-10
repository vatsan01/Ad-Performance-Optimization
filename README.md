# Ad-Performance-Optimization

## Overview
This project builds a **Machine Learning Model** to analyze **advertising engagement trends** and optimize **ad performance**.

## Features
- Predicts **engagement rate** using a **Random Forest Regressor**
- Processes historical **ad performance data**
- Evaluates **model performance** using **Mean Absolute Error (MAE) and R² Score**
- Saves the trained model for **future predictions**

## Technologies Used
- **Python** (pandas, numpy, scikit-learn, joblib)
- **Machine Learning** (Random Forest Regressor)
- **Data Processing** (pandas, numpy)
- **Model Storage** (joblib)

## Installation
Clone the repository and install dependencies:
 ```bash
git clone git clone https://github.com/vatsan01/Ad-Performance-Optimization.git
cd Ad-Performance-Optimization
pip install -r requirements.txt
```
## Usage
- Place the ad performance dataset (ad_performance_data.csv) in the project folder.
- Run the script to train the model:
  python ad_performance_model.py
- The model will generate predictions and save a trained model (ad_performance_model.pkl).

## Dataset Format
Ensure your dataset (`ad_performance_data.csv`) has the following columns:

| Date       | Ad Spend | Impressions | Clicks | Conversions | Engagement Rate |
|------------|----------|-------------|--------|-------------|-----------------|
| 2024-01-01 | 500      | 10000       | 200    | 50          | 5.0             |


## Future Enhancements
Implement Hyperparameter Tuning to improve model performance.
Add more ML models for comparative analysis.
Deploy model as a web API for real-time predictions.



