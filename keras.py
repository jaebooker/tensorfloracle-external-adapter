import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#x_test, y_test = curl "https://ipfs.infura.io:5001/api/v0/get?arg=QmZtmD2qt6fJot32nabSP3CUjicnypEBz7bHVDhPQt9aAy&archive=true", curl "https://ipfs.infura.io:5001/api/v0/get?arg=QmZtmD2qt6fJot32nabSP3CUjicnypEBz7bHVDhPQt9aAy&archive=true"

test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_dataset = test_dataset.batch(64)

#model = 'curl "https://ipfs.infura.io:5001/api/v0/get?arg=QmZtmD2qt6fJot32nabSP3CUjicnypEBz7bHVDhPQt9aAy&archive=true"'

result = model.evaluate(test_dataset)
dict(zip(model.metrics_names, result))
