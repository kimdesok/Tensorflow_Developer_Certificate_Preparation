import collections
import pathlib

import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization

import tensorflow_datasets as tfds
import tensorflow_text as tf_text

# Example 1 - predict the tag for a question from Stack Overflow
# download and explore the dataset
data_url = 'https://storage.googleapis.com/download.tensorflow.org/data/stack_overflow_16k.tar.gz'
dataset_dir = utils.get_file(
    origin=data_url,
    untar=True,
    cache_dir='stack_overflow',
    cache_subdir='')
dataset_dir = pathlib.Path(dataset_dir).parent

print(list(dataset_dir.iterdir()))

train_dir = dataset_dir/'train'
print(list(train_dir.iterdir()))

sample_file = train_dir/'python/1755.txt'
with open(sample_file) as f:
    print(f.read())

# Load the dataset
batch_size=32
seed=42
raw_train_ds = utils.text_dataset_from_directory(
    train_dir,
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed
)

# Ten examples
for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(10):
        print('Question:', text_batch.numpy()[i])
        print('Label:', label_batch.numpy()[i])

# Class name
for i, label in enumerate(raw_train_ds.class_names):
  print("Label", i, "corresponds to", label)

# Create a validation set
raw_val_ds = utils.text_dataset_from_directory(
    train_dir,
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed
)

test_dir = dataset_dir/'test'

# Create a test set
raw_test_ds = utils.text_dataset_from_directory(
    test_dir,
    batch_size=batch_size
)

# Prepare the dataset for training









