import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, GlobalMaxPooling1D
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow.keras.optimizers import Adam

class NLPAnalysis:
    def __init__(self, vocab_size=10000, max_length=100, embedding_dim=50):
        self.vocab_size = vocab_size
        self.max_length = max_length
        self.embedding_dim = embedding_dim
        self.tokenizer = Tokenizer(num_words=self.vocab_size)
        self.sentiment_model = self._build_sentiment_model()

    def _build_sentiment_model(self):
        model = Sequential([
            Embedding(input_dim=self.vocab_size, output_dim=self.embedding_dim, input_length=self.max_length),
            LSTM(64, return_sequences=True),
            GlobalMaxPooling1D(),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def preprocess_text(self, texts):
        self.tokenizer.fit_on_texts(texts)
        sequences = self.tokenizer.texts_to_sequences(texts)
        padded_sequences = pad_sequences(sequences, maxlen=self.max_length, padding='post')
        return padded_sequences

    def train_sentiment_model(self, texts, labels, epochs=10, batch_size=32):
        padded_sequences = self.preprocess_text(texts)
        self.sentiment_model.fit(padded_sequences, labels, epochs=epochs, batch_size=batch_size)

    def sentiment_analysis(self, text):
        padded_sequence = self.preprocess_text([text])
        prediction = self.sentiment_model.predict(padded_sequence)[0][0]
        sentiment = 'positive' if prediction > 0.5 else 'negative'
        return sentiment, prediction

    def extract_keywords(self, texts, top_n=10):
        all_words = ' '.join(texts).split()
        word_freq = tf.keras.preprocessing.text.text_to_word_sequence(' '.join(all_words))
        word_freq = tf.keras.preprocessing.text.Tokenizer(num_words=self.vocab_size)
        word_freq.fit_on_texts(word_freq.word_index.keys())
        sorted_word_freq = sorted(word_freq.word_counts.items(), key=lambda x: x[1], reverse=True)
        keywords = [word for word, freq in sorted_word_freq[:top_n]]
        return keywords

# Example usage
# texts = ["This is a great product!", "I am not happy with this item.", ...]
# labels = [1, 0, ...]  # 1 for positive, 0 for negative
# nlp_analysis = NLPAnalysis()
# nlp_analysis.train_sentiment_model(texts, labels)
# sentiment, score
