# 199_helper_functions
# Purpose: House common functions used for bart and COVID clean up
# Author: Kathryn DeWitt (kdewitt3)
import datetime as dt
import pandas as pd

def read_data(file_name, header = True):
    data = None
    try:
        if header:
            data = pd.read_csv(file_name)
        else:
            data = pd.read_csv(file_name, header=None)
    except Exception as e:
        print("Unable to read the file '" + file_name + "' as expected. Please review error: ")
        print(e)
    finally:
        return data

def save_data(data, save_name):
    try:
        data.to_csv(save_name, index=False)  
        print("Successfully saved file " + save_name)
    except Exception as e:
        print("Unable to save the file as expected. Please review error: " )
        print(e)