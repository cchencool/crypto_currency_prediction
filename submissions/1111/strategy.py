# Here you can
# 1. import necessary python packages for your strategy
# 2. Load your own facility files containing functions, trained models, extra data, etc for later use
# 3. Set some global constants
# Note:
# 1. You should put your facility files in the same folder as this strategy.py file
# 2. When load files, ALWAYS use relative path such as "data/facility.pickle"
# DO NOT use absolute path such as "C:/Users/Peter/Documents/project/data/facility.pickle"
from sklearn.externals import joblib
from auxiliary import Deal_record, check_balance_warning, get_current_avg_price, get_history_avg_price, generate_bar
import pandas as pd
import numpy as np
import random

# Data Settings

model_list = []
use_model = [True for i in range(len(model_list))]     # use corresponding model or not
asset_list = ['BCH-USD', 'BTC-USD', 'ETH-USD', 'LTC-USD']
feature_list = ['close', 'high', 'low', 'open', 'volume']

# User Settings

expect_return_rate = 0.05
decision_period = 60 * 4  # Number of minutes to generate next new bar

cash_balance_lower_limit = 20000    # cash balance problem!! if my cash balance rise back to 10,000 after sell the crypto, I still cannot make any deal.
crypto_balance_limit = 80000

piror = 0.7     # the assumed chance that price will go up/down next week. get by analysis historcal data
piror_weight = 0.2      # piror weight for each deal. 
fluctuate_volumn_per_crypto = [15, 100, 6, 1.3]     # assumeed fluctunate volumn for each period. get by analysis historical data. and should fit for each different currency
deal_unit_per_crypto = [3, 1, 5, 10]       # unit amount for each deal period

# Load Models
# model = joblib.load('./model/model.pkl')



# decision_count=0
# failed_count = 0
# random.seed(123)
# is_reverse = False


# Here is your main strategy function
# Note:
# 1. DO NOT modify the function parameters (time, data, etc.)
# 2. The strategy function AWAYS returns two things - position and memory:
# 2.1 position is a np.array (length 4) indicating your desired position of four crypto currencies next minute
# 2.2 memory is a class containing the information you want to save currently for future use

def handle_bar(counter,  # a counter for number of minute bars that have already been tested
               time,  # current time in string format such as "2018-07-30 00:30:00"
               data,  # data for current minute bar (np.array)
               init_cash,  # your initial cash, a constant
               transaction,  # transaction ratio, a constant
               cash_balance,  # your cash balance at current minute
               crypto_balance,  # your crpyto currency balance at current minute
               total_balance,  # your total balance at current minute
               position_current,  # your position for 4 crypto currencies at this minute
               memory  # a class, containing the information you saved so far
               ):
    # Here you should explain the idea of your strategy briefly in the form of Python comment.
    # You can also attach facility files such as text & image & table in your team folder to illustrate your idea

    # The idea of my strategy:
    # Logistic regression with label = rising/falling signal. 

    # Pattern for long signal:
    # for rising/falling prediction, long/short one unit of & according to the confidence to calculate the goal price, once it reachs sell the crypto.

    global deal_unit_for_each_crypto   
    global piror
    global piror_weight
    global period
    global failed_count
    global decision_count
    global is_reverse
    global use_model

    # Get position of last minute
    position_new = position_current


    return position_new, memory