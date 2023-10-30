#!/usr/bin/python3

import pandas as pd

test = pd.read_csv('https://drive.google.com/file/d/15xAJkOUoqKuuwSf4vcvjlKObjQbCxCF_/view?usp=drive_link')
train = pd.read_csv('https://drive.google.com/file/d/1PY5d0iZDasinTZsLrS2fIbJYjj_lpwqy/view?usp=drive_link')

test.to_csv('/home/akashy/Projects/MLops_practice/data/raw/Test.csv', columns = test.columns)
train.to_csv('/home/akashy/Projects/MLops_practice/data/raw/Train.csv', columns = test.columns)
