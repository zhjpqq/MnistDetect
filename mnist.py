#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/13 8:52'
__author__ = 'ooo'

import numpy as np
import torch as t
import torchvision as tv
import random
from torch.utils import data
from torchvision.datasets import mnist
import cv2, PIL, skimage


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

    def digit_index_list(self, shuffle=True):
        # index_list [(0,2,3),(1,9,8),(1,2),(4,6,7,3,9),...]
        if self.mnist.train:
            labels = self.mnist.train_labels
        else:
            labels = self.mnist.test_labels

        # def get_digit_index(max_index, digit_nums):
        #     curr_num = digit_nums[random.randint(0, len(digit_nums)-1)]
        #     curr_digit_index = tuple([random.randint(0, max_index) for _ in range(curr_num)])
        #     return curr_digit_index
        # self.index_list = [get_digit_index(len(labels), self.digit_nums) for _ in range(self.img_nums)]

        digits_index = np.random.permutation(len(labels)) if shuffle else np.arange(0, len(labels))
        start = 0
        for i in range(self.img_nums):
            step = self.digit_nums[random.randint(0, len(self.digit_nums) - 1)]
            idxs = digits_index[start:start + step]
            self.index_list.append(tuple(idxs))
            start = start + step
            start = start if start + step < len(labels) else 0
        return self.index_list, digits_index

    def make_image(self, digits_index):
        # 拉取任意数量的digits, 填充到一张新的图片, 比如digit_index = (2,3,4) or (6,1,5,9)，...
        digits, labels = [], []
        for index in digits_index:
            digit, label = self.mnist[index]
            digits.append(digit)
            labels.append(label)




