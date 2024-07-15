import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

class TrendAnalysis:
    def __init__(self, data, time_steps=10):
        self.data = data
        self.time_steps = time_steps
        self.scaler = MinMaxScaler()
        self.model = self._build_model()
        self._prepare_data()

    def _build_model(self):
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=(self.time_steps, 1)),
            LSTM(50, return_sequences=False),
            Dense(25),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def _prepare_data(self):
        scaled_data = self.scaler.fit_transform(self.data)

        self.x_train = []
        self.y_train = []
        for i in range(self.time_steps, len(scaled_data)):
            self.x_train.append(scaled_data[i-self.time_steps:i, 0])
            self.y_train.append(scaled_data[i, 0])

        self.x_train, self.y_train = np.array(self.x_train), np.array(self.y_train)
        self.x_train = np.reshape(self.x_train, (self.x_train.shape[0], self.x_train.shape[1], 1))

    def train_model(self, epochs=10, batch_size=32):
        self.model.fit(self.x_train, self.y_train, epochs=epochs, batch_size=batch_size)

    def predict_trend(self, future_steps=10):
        last_time_steps = self.data[-self.time_steps:]
        scaled_last_time_steps = self.scaler.transform(last_time_steps)

        predictions = []
        for _ in range(future_steps):
            input_data = np.reshape(scaled_last_time_steps, (1, self.time_steps, 1))
            pred = self.model.predict(input_data)[0][0]
            predictions.append(pred)

            scaled_last_time_steps = np.append(scaled_last_time_steps, pred)[-self.time_steps:]

        predictions = self.scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
        return predictions

# Example usage
# data = pd.DataFrame({'trend_score': [10, 15, 20, 25, ...]})
# trend_analysis = TrendAnalysis(data['trend_score'].values.reshape(-1, 1))
# trend_analysis.train_model()
# future_trends = trend_analysis.predict_trend(future_steps=10)
