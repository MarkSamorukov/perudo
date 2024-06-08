import json
import numpy as np
from tensorflow.keras import layers, models

with open('../../statistics/believe_normalize_data.json', 'r') as file:
    data = json.load(file)

X_train = np.array([entry['train'] for entry in data])
y_train = np.array([1 if entry['test'] else 0 for entry in data])

model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(12, 2)),
    layers.Flatten(),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=6)

model.save('deep_model_perudo_1.keras')

