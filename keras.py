import sys, json, numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = []
results = []

#x_test, y_test = curl "https://ipfs.infura.io:5001/api/v0/get?arg=ipfs_test_x&archive=true", curl "https://ipfs.infura.io:5001/api/v0/get?arg=ipfs_test_y&archive=true"

test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_dataset = test_dataset.batch(64)

#for i in range(0, len(ipfs_train_hash)):
#   model[i] = 'curl "https://ipfs.infura.io:5001/api/v0/get?arg=ipfs_train_hash[i]&archive=true"'
#   results[i] = model[i].evaluate(test_dataset)

dict(zip(model.metrics_names, results))

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()

    #create a numpy array
    np_lines = np.array(lines)

    #use numpys sum method to find sum of all elements in the array
    lines_sum = np.sum(np_lines)

    #return the sum to the output stream
    print lines_sum

#start process
if __name__ == '__main__':
    main()
