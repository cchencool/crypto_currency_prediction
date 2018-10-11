#!/usr/bin/env python
# coding: utf-8

import sys
import os
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# load data
def load_data():
      working_folder = "."
      data_folder = "data"
      format1_fdir = 'data_format1_20180930_20181007.h5'#data_format1_201808.h5'#923_20180930.h5'#
      format2_fdir = 'data_format2_20180930_20181007.h5'#data_format2_201808.h5'#923_20180930.h5'#

      format1_dir = os.path.join(working_folder, data_folder, format1_fdir)
      format2_dir = os.path.join(working_folder, data_folder, format2_fdir)

      sys.path.append(working_folder)

      f1_data = pd.HDFStore(format1_dir)
      f1_data.keys()
      keys = ['BCH-USD', 'BTC-USD', 'ETH-USD', 'LTC-USD']
      series_avg = pd.DataFrame()
      for key in keys:
            series_avg[key] = (0.25 * (f1_data[key]['close'] + f1_data[key]['open'] + f1_data[key]['high'] + f1_data[key]['low']))

      f1_data.close()
      return series_avg, keys


def train_test_split_self(data_x, data_y, test_size=0.33):
    size = len(data_x)
    train_size = int(len(data_x) * test_size)
    return data_x[:train_size], data_x[train_size:], data_y[:train_size], data_y[train_size:]


# train model
def train_model(data_x, data_y):
      X_train, X_test, y_train, y_test = train_test_split_self(data_x, data_y, test_size=0.33)#, random_state=42)

      # Create linear regression object
      regr = linear_model.LinearRegression()

      # Train the model using the training sets
      regr.fit(X_train, y_train)

      # Make predictions using the testing set
      y_pred = regr.predict(X_test)

      # The coefficients
      print('Coefficients: \n', regr.coef_)
      print('Intercept: \n', regr.intercept_)

      # The mean squared error
      print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
      # Explained variance score: 1 is perfect prediction
      print('Variance score: %.2f' % r2_score(y_test, y_pred))

      # Plot outputs
      # fig = plt.figure(figsize=(20,10))
      # x_axis = np.arange(len(X_test))
      # plt.scatter(x_axis,y_test,  color='black')
      # plt.plot(x_axis, y_pred, color='blue', linewidth=3)
      # plt.xticks(())
      # plt.yticks(())
      # plt.show()
     

if __name__ == '__main__':
      series_avg, keys = load_data()
      # train model
      shift_period = 60
      data_length = 60 * 24 * 3
      asset = keys[1]

      # Load the diabetes dataset
      data_x = series_avg.values[:-1*shift_period]
      data_y = series_avg[asset].shift(-1 * shift_period)[:-1*shift_period].values

      data_x = data_x[:data_length]
      data_y = data_y[:data_length]

      train_model(data_x, data_y)