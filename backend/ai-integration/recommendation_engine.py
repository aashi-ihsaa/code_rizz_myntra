import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Add, Dense
from tensorflow.keras.optimizers import Adam

class RecommendationEngine:
    def __init__(self, num_users, num_items, embedding_dim=50):
        self.num_users = num_users
        self.num_items = num_items
        self.embedding_dim = embedding_dim
        self.model = self._build_model()

    def _build_model(self):
        # Input layers
        user_input = Input(shape=(1,), name='user_input')
        item_input = Input(shape=(1,), name='item_input')

        # Embedding layers
        user_embedding = Embedding(input_dim=self.num_users, output_dim=self.embedding_dim, name='user_embedding')(user_input)
        item_embedding = Embedding(input_dim=self.num_items, output_dim=self.embedding_dim, name='item_embedding')(item_input)

        # Flatten embeddings
        user_vec = Flatten(name='flatten_user')(user_embedding)
        item_vec = Flatten(name='flatten_item')(item_embedding)

        # Dot product of user and item embeddings
        dot_product = Dot(axes=1, name='dot_product')([user_vec, item_vec])

        # Add bias terms
        user_bias = Embedding(input_dim=self.num_users, output_dim=1, name='user_bias')(user_input)
        item_bias = Embedding(input_dim=self.num_items, output_dim=1, name='item_bias')(item_input)

        user_bias = Flatten(name='flatten_user_bias')(user_bias)
        item_bias = Flatten(name='flatten_item_bias')(item_bias)

        # Output layer
        output = Add(name='output')([dot_product, user_bias, item_bias])

        # Build and compile model
        model = Model(inputs=[user_input, item_input], outputs=output)
        model.compile(optimizer=Adam(lr=0.001), loss='mean_squared_error')

        return model

    def train(self, user_ids, item_ids, ratings, epochs=10, batch_size=32):
        self.model.fit([user_ids, item_ids], ratings, epochs=epochs, batch_size=batch_size)

    def predict(self, user_id, item_id):
        return self.model.predict([np.array([user_id]), np.array([item_id])])[0][0]

    def recommend(self, user_id, top_n=5):
        item_ids = np.arange(self.num_items)
        user_ids = np.full(self.num_items, user_id)
        predictions = self.model.predict([user_ids, item_ids])
        recommended_items = np.argsort(predictions.flatten())[::-1][:top_n]
        return recommended_items

# Example usage
# num_users = 1000
# num_items = 500
# recommender = RecommendationEngine(num_users, num_items)
# user_ids = np.array([...])
# item_ids = np.array([...])
# ratings = np.array([...])
# recommender.train(user_ids, item_ids, ratings)
# recommendations = recommender.recommend(user_id)
