# Import Libraries and Frameworks
import pyodbc
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Trusted Connection to SQL Server 2022 Named Instance
conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQL2K22;DATABASE=IrisDB;Trusted_Connection=yes;"
conn = pyodbc.connect(conn_str)

# Step 1: Retrieve Training Data from the "iris_data" table
training_query = 'SELECT sepal_length, sepal_width, petal_length, petal_width, species FROM iris_data'
training_data = pd.read_sql(training_query, conn)

# Step 2: Prepare training data
X_train = training_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y_train = training_data['species']
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)

# Step 3: Build and Train Keras Model
model = Sequential()
model.add(Dense(units=64, input_dim=4, activation='relu'))
model.add(Dense(units=3, activation='softmax'))  # Assuming 3 iris species

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train_encoded, epochs=10, batch_size=32)

# Close the connection before proceeding
conn.close()

# Step 4: Generate New Prediction Data (Simulating Unseen Data)
new_prediction_data = pd.DataFrame({
    'sepal_length': [5.1, 6.2, 4.8],
    'sepal_width': [3.5, 3.0, 3.8],
    'petal_length': [1.4, 4.5, 1.6],
    'petal_width': [0.2, 1.5, 0.2],
    'species': ['setosa', 'versicolor', 'setosa']  # Add actual species for accuracy calculation
})

# Display the input data for predictions
print()
print('Input Data for Predictions:')
print(new_prediction_data)
print()

# Step 5: Make Model Predictions on New Prediction Data
prediction_features = new_prediction_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
new_predictions = model.predict(prediction_features)

predicted_labels = label_encoder.inverse_transform(new_predictions.argmax(axis=1))

# Calculate accuracy
correct_predictions = (predicted_labels == new_prediction_data['species']).sum()
total_predictions = len(new_prediction_data)
accuracy = correct_predictions / total_predictions * 100

# Display the predictions and accuracy
print('\nPredicted Labels for the given values:')
print(predicted_labels)
print('\nPrediction Accuracy: {:.2f}%'.format(accuracy))
print()
