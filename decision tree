from sklearn.tree import DecisionTreeClassifier
import numpy as np  # Import NumPy for handling array inputs

# XOR Input and Output
X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
y = np.array([0, 1, 1, 0])  # XOR truth table

# Create and train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict outputs for new inputs
predictions = model.predict(np.array([[1, 1], [0, 0]]))
print(predictions)
