# 100_bart_cleanup
# Purpose: Rollup Ridership Data to the cnty/month level
# Author: Kathryn DeWitt (kdewitt3)
# Specifications:
'''
1. Read in the daily ridership data file
    1.1 The data for Jan 2020 - May 2023 were created in 100_bart_cleanup.py
2. Roll up to the month level (grouping by station entry, station exit, date)
3. Roll up to the county level (grouping by station_cnty)
4. Save the final file as a .csv 
    4.1 The file should be called "103_monthly_ridership_data"
    4.2 The file must have the following variables:
        date                   -  format mm/01/yyyy
        station_cnty           - The county in which the station resides 
        cnt_entries            - int representing number of entries to entry station on date
        cnt_exits              - int representing number of entries to entry station on date
        cnt_riders             - int representing sum of exits and entries
'''

import datetime as dt
from ntpath import join
from pickle import TRUE
import pandas as pd
import io_helper as io_hlp

#years to read in
years = ["2019", "2020", "2021", "2022", "2023"]

def rollup_data(data):
    #Remove vars before rollup:
    cleaned_data = data[['date', 'cnt_entries', 'cnt_exits', 'station_cnty']]

    #First calculate rollup by county
    cnty_rollup = cleaned_data.groupby(by=['station_cnty', 'date'])\
                                .sum()\
                                .reset_index()
    #then rollup to the month
    cnty_rollup['date'] = pd.to_datetime(cnty_rollup['date'])
    cnty_rollup['year'] = cnty_rollup.date.dt.year
    cnty_rollup['month'] = cnty_rollup.date.dt.month
    
    cnty_rollup = cnty_rollup.groupby(['station_cnty', 'year', 'month'])\
                                .agg('sum')\
                                .reset_index()

    #restore date var
    cnty_rollup['dateInt'] = cnty_rollup['year'].astype(str) + cnty_rollup['month'].astype(str).str.zfill(2)+ "01"
    cnty_rollup['date'] = pd.to_datetime(cnty_rollup['dateInt'], format='%Y%m%d')

    #create single measure of ridership
    cnty_rollup["cnt_riders"] = cnty_rollup["cnt_exits"] +  cnty_rollup["cnt_entries"]

    return cnty_rollup



def main():
    bart_data = io_hlp.read_data(f"User_Created_Data//100_ridership_data.csv", True)  
    print(bart_data.head())

    final_dataset = rollup_data(bart_data)
    io_hlp.save_data(final_dataset, "User_Created_Data//103_monthly_ridership_data.csv")

main()