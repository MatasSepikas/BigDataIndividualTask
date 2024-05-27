# Import libraries
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from ucimlrepo import fetch_ucirepo
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pandas as pd

# Import the dataset
concrete_compressive_strength = fetch_ucirepo(id=165)

# Split imported dataset into features and dependent variable
X = concrete_compressive_strength.data.features
y = concrete_compressive_strength.data.targets

# Make sure that dependant variable is a 1D array
y = y.values.ravel()

# Split the dataset into training and test sets
# 80 % for training and 20 % for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

# Initialize the machine learning model
gbr = GradientBoostingRegressor()

# Create a pipeline with the initialized regressor
pipe = Pipeline([
    ('regressor', gbr)
])

# Fit the pipeline with training data
pipe.fit(X_train, y_train)

# Make predictions for testing data
y_pred = pipe.predict(X_test)

# Calculate accuracy metrics MAE and RMSE
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Print MAE and RMSE
print(f"MAE: {mae}")
print(f"RMSE: {rmse}")

# Save the fitted pipeline to a file for later usage
with open('trained_pipeline.pkl', 'wb') as f:
    pickle.dump(pipe, f)

print("The model training is complete, and the pipeline has been saved.")

# Load the saved pipeline
with open('trained_pipeline.pkl', 'rb') as f:
    loaded_pipe = pickle.load(f)

# Ensure that the new data for prediction includes valid feature names
# Use the same feature names as used during training
feature_names = [
    'Cement', 'Blast Furnace Slag', 'Fly Ash', 'Water',
    'Superplasticizer', 'Coarse Aggregate', 'Fine Aggregate', 'Age'
]

# Ensure the prediction data matches these feature names exactly
new_data = pd.DataFrame([
    [540.0, 0.0, 0.0, 162.0, 2.5, 1040.0, 676.0, 28],
    [332.5, 142.5, 0.0, 228.0, 0.0, 932.0, 594.0, 28],
    # Add more rows if needed
], columns=feature_names)

# Make predictions with the loaded pipeline
predictions = loaded_pipe.predict(new_data)

# Print the predictions
print("Predictions for new data:")
print(predictions)
