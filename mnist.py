#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/13 8:52'
__author__ = 'ooo'

import numpy as np
import torch as t
import torchvision as tv
from torch.utils import data
from torchvision.datasets import mnist, FakeData


class Mnist(data.Dataset):
    def __init__(self, img_shape=(1024, 1024, 3), img_nums=100, digit_nums=(2, 4), transform=None,
                 data_root='', data_set='train', download=False, data_transform=None):

        self.mnist = mnist.MNIST(data_root, data_set, data_transform, None, download)
        self.img_shape = img_shape
        self.img_nums = img_nums
        self.digit_nums = digit_nums
        self.transform = transform
        self.index_list = []

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def __repr__(self):
        print('Mnist fake data for detection')

    def init_index(self):
        if self.mnist.train:
            digits, labels = self.mnist.train_data, self.mnist.train_labels
        else:
            digits, labels = self.mnist.test_data, self.mnist.test_labels

        digits_index = range(0, len(labels))
        self.index_list = [()]*self.img_nums
        for index in self.index_list:
            step =


    def get_digits(self, index):
        index = index if isinstance(index, (tuple, list)) else tuple([index])
        digits = []
        for i in index:
            img = mnist.MNIST.
