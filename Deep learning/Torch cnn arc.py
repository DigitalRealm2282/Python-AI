

from torch.utils.data import dataloader
import torchvision
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data
import torchvision.transforms
import os
import numpy as np


#CNN ARC#
model = nn.Sequential()
model.add_module('conv1',nn.Conv2d(6,24,kernel_size=3))
model.add_module('Relu1',nn.ReLU())
model.add_module('pooling1',nn.MaxPool2d(kernel_size=1))
model.add_module('conv2',nn.Conv2d(24,48,kernel_size=2))
model.add_module('Relu2',nn.ReLU())
model.add_module('pooling2',nn.MaxPool2d(kernel_size=1))



print(model)

L_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.1)

print(L_function, optimizer)

device = torch.device('cuda'if torch.cuda.is_available()else 'cpu')

print(device)