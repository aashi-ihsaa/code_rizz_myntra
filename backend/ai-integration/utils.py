import numpy as np

def normalize_data(data):
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)

def split_data(data, test_size=0.2):
    np.random.shuffle(data)
    split_index = int(len(data) * (1 - test_size))
    train_data = data[:split_index]
    test_data = data[split_index:]
    return train_data, test_data

# Example usage
# data = np.array([...])
# normalized_data = normalize_data(data)
# train_data, test_data = split_data(normalized_data)
