# some imports
from __future__ import division

import numpy as np
import random

from discriminator import *
from transformer import *
from data_utils import *
from util import *

# Load the (preprocessed) CIFAR10 data.
data = get_CIFAR10_data()

# unpack CIFAR data
X_train, y_train = data['X_train'], data['y_train']
X_val, y_val = data['X_val'], data['y_val']
X_test, y_test = data['X_test'], data['y_test']

print 'training dataset shapes:', X_train.shape, y_train.shape
print 'validation dataset shapes:', X_val.shape, y_val.shape
print 'testing dataset shapes:', X_test.shape, y_test.shape

# create transformer / discriminator objects
transformer = Transformer()

# if we have a trained model saved
if os.path.isfile('../models/discrim.p'):
    # load it from the pickle file
    discriminator = pickle.load('../models/discrim.p', 'rb')
else:
    # create a new discriminator object
    discriminator = Discriminator()
<<<<<<< HEAD
    
    
=======
>>>>>>> 7a44fb9c7efdaabecc65b4cf6835966be8b7ec27


