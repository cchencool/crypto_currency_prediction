#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/9/28 14:42
# @Author  : chen
# @Site    : 
# @File    : prj.py
# @Software: PyCharm

__author__ = "chen"

import h5py
import pandas as pd
import numpy as np
import copy
import os
import sys
import matplotlib.pyplot as plt
import warnings
from sklearn.externals import joblib

warnings.filterwarnings('ignore')

working_folder = "."
data_folder = os.path.join(working_folder, 'data')

format1_files = ['data_format1_201807.h5', 'data_format1_201808.h5']
format2_files = ['data_format2_201807.h5', 'data_format2_201808.h5']

cur_datas = pd.DataFrame()
opened_files = list()
for f in format1_files:
    f_fp = os.path.join(data_folder, f)
    print(f_fp)
    f1_data = pd.HDFStore(f_fp)
    opened_files.append(f1_data)
    cur_bch = f1_data['BCH-USD']

    if not cur_datas.empty:
        cur_datas = cur_datas.append(cur_bch)
        print(len(cur_datas))
    else:
        for key in f1_data.keys():
            print(key)
        cur_datas = cur_bch
        print(len(cur_datas))


for f in opened_files:
    f.close()

#
# cur_data = f1['BCH-USD']
# times= cur_data.index
# print(cur_data.iloc[1].name)
#
#
#
# model = joblib.load('model.pkl')
# o_c = cur_data[['open', 'close']]
# prob_pred = model.predict_proba(o_c)
# # prob_pred[prob_pred < 0.45] = -1
# # prob_pred[prob_pred > 0.55] = 1
#
# cur_data = f1['BCH-USD']
#
# cur_data = cur_data.resample('W').max()
# high_series = cur_data['high']
# low_series = cur_data['low']
# open_series = cur_data['open']
# close_series = cur_data['close']
# volumn_series = cur_data['volume']
#
#
# fig = plt.figure()
# import matplotlib.style as style
#
# style.use('ggplot')
#
# plt_data = pd.DataFrame()
# plt_data['o/c'] = open_series - open_series.shift(periods=1) #open_series #close_series
# # plt_data['o/c'] /= plt_data['o/c'].max()
# # plt_data['o/c'][plt_data['o/c']>0] = 1
# # plt_data['o/c'][plt_data['o/c']<0] = -1
# # plt_data['h/l'] = high_series - low_series
# # plt_data['h/l'] /= plt_data['h/l'].max()
#
# # plt_data['o/c'].plot(figsize=(20,10), label='Series')
#
# plt_data.plot(figsize=(20,10), subplots=True, title='trend', grid=True)
# fig.show()#block=True)
#
#
# fig_cur = plt.figure()
# cur_data.plot(figsize=(20,10), title='currency', grid=True)
# fig_cur.show()
