# 100_bart_cleanup
# Purpose: Clean Ridership Data
# Author: Kathryn DeWitt (kdewitt3)
# Specifications:
'''
1. Read in the hourly ridership data files
    1.1 The data for Jan 2020 - May 2022 are in three files, read each in separately then append the data sets.
2. Roll up to the day level (grouping by station entry, station exit, date)
3. Include the county names, the station names, by merging in additional files
    3.1 Verify via crosstabs that a station is only ever assigned to 1 county
    3.2 Verify via crosstabs that a station name is only ever assigned to 1 station
    3.3 EDA: How many stations in each county?
    3.4 EDA: What is the average exits and entrants of each county by week? 
    3.5 EDA: Do any rows have 0 exits or entrants?
4. Save the final file as a .csv 
    4.1 The file should be called "100_ridership_data"
    4.2 The file must have the following variables:
        date                   -  format mm/dd/yyyy
        station_abbr           -  4 letter station abbreviation
        station_nm             -  Full station name
        station_cnty           - The county in which the station resides 
        cnt_entries            - int representing number of entries to entry station on date
        cnt_exits              - int representing number of entries to entry station on date
'''

import datetime as dt
import pandas as pd
import numpy as np
import io_helper as io_hlp


def rollup_data(data):
    #Rename columns
    cleaned_data = data.rename(columns={0: 'date', 1: 'hour', 2: 'entry', 3: 'exit', 4: 'count'})
    print(cleaned_data)
    #Remove hour before roll up:
    cleaned_data = cleaned_data[['date', 'entry', 'exit', 'count']]

    #First calculate Entrants
    cleaned_entrants = cleaned_data.groupby(by=['date', 'entry'])\
                                    .sum()\
                                    .reset_index()\
                                    .rename(columns={'entry': 'station', 'count' : 'cnt_entries'})

    #Then calculate Exits
    cleaned_exits = cleaned_data.groupby(by=['date', 'exit'])\
                                .sum()\
                                .reset_index()\
                                .rename(columns={'exit': 'station', 'count' : 'cnt_exits'})

    #Finally, join the datasets to create a single df that is unique at the Date-Station Level 
    join_cleaned_data = cleaned_entrants.merge(cleaned_exits, on=['station', 'date'])

    print(join_cleaned_data)
    return join_cleaned_data

def clean_data(data):
    pass

def add_county():
    pass

def main():
    bart_data = io_hlp.read_data("date-hour-soo-dest-2020.csv", False)
    bart_data = rollup_data(bart_data)
    #bart_data = clean_data(bart_data)
    io_hlp.save_data(bart_data, "100_ridership_data.csv")

main()