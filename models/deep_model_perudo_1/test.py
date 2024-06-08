import json
import numpy as np
import tensorflow as tf


with open('../../statistics/believe_normalize_data.json', 'r') as file:
    data = json.load(file)

loaded_model = tf.keras.models.load_model('deep_model_perudo_1.keras')

X_new = np.array([entry['train'] for entry in data[:50]])
y_true = np.array([1 if entry['test'] else 0 for entry in data[:50]])

y_pred = (loaded_model.predict(X_new) > 0.5)

TP = np.sum((y_true == 1) & (y_pred == 1))
TN = np.sum((y_true == 0) & (y_pred == 0))
FP = np.sum((y_true == 0) & (y_pred == 1))
FN = np.sum((y_true == 1) & (y_pred == 0))

accuracy = (TP + FP) / (TP + TN + FP + FN)

print(f"{TP} | {FN}\n{FP} | {TN}")
print(accuracy)
