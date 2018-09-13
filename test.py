#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/13 17:57'
__author__ = 'ooo'

import numpy as np
import torch as t
import torchvision as tv
import random
from torch.utils import data
from torchvision.datasets import mnist
import cv2
from PIL import Image

mn = mnist.MNIST(root='E:\datasets\mnist', train=True,  download=False)

digits, labels = mn.train_data, mn.train_labels
print(digits.shape, labels.shape)

digit, label = mn[random.randint(0, len(labels)-1)]

Image._show(digit)

# cv2.imshow('images', digit)
# cv2.waitkey(-1)

