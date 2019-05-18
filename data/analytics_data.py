import pandas as pd

from tqdm import tqdm
import numpy as np


data = pd.read_csv("data.csv", header = None)

data.columns = ['user_A', "user_B","event_time"]


analytics_data = data.copy()

analytics_data["event_start"] = np.nan
analytics_data['event_end'] = np.nan


def check_follow_back(data,index,user_A_values, user_B_values):

    # get the user_A and user_B values.
    user_A = user_A_values[index]
    user_B = user_B_values[index]
    
    # find the index where user_A follows user_B
    # find the index where user_B follows user_A
    user_A_follow_index = (user_A_values == user_B)
    user_B_follow_index = (user_B_values == user_A)
    
    # check if user_B follows back user_A.
    if data[user_A_follow_index & user_B_follow_index].shape[0] == 1:
        # get the event-time for when user_A and user_B follows one another. 
        user_A_event_time = data['event_time'][index]
        user_B_index = data[user_A_follow_index & user_B_follow_index].index.values[0]
        user_B_event_time = data['event_time'][user_B_index]
        # print(user_B_index)

        if user_A_event_time < user_B_event_time:
            data.iloc[index] = [user_A, user_B, user_A_event_time, \
                                user_A_event_time, user_B_event_time ]
            
            data.iloc[user_B_index] = [np.nan, np.nan, np.nan,\
                                   np.nan, np.nan ]
            
            
        elif user_B_event_time < user_A_event_time:
            data.iloc[index] = [user_B, user_A, user_A_event_time,\
                               user_B_event_time, user_A_event_time]
            
            data.iloc[user_B_index] = [np.nan, np.nan, np.nan,\
                                   np.nan, np.nan ]
    else:
        data.loc[data.index[index], "event_start"] \
        = data.loc[data.index[index], "event_time"]
                    
    return data
            
            

entire_user_A = analytics_data['user_A'].copy().values
entire_user_B = analytics_data['user_B'].copy().values

# iterate through all the rows. 
# 
for index in tqdm(range(analytics_data.shape[0])):
    analytics_data = check_follow_back(analytics_data,index,\
                                      user_A_values = entire_user_A,
                                  user_B_values = entire_user_B)
    
    
analytics_data.to_csv("analytics_data.csv", index = False)