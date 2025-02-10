import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset (Ensure the CSV file has relevant ad engagement data)
df = pd.read_csv("ad_performance_data.csv")

# Feature Engineering (Modify according to available data)
features = ["ad_spend", "impressions", "clicks", "conversions"]
target = "engagement_rate"

X = df[features]
y = df[target]

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:\nMAE: {mae}\nR² Score: {r2}")

# Save Model for future predictions
import joblib
joblib.dump(model, "ad_performance_model.pkl")
