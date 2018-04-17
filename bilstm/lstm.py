import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

