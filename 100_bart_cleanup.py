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
from ntpath import join
from pickle import TRUE
import pandas as pd
import io_helper as io_hlp

#years to read in
years = ["2019", "2020", "2021", "2022"]

def rollup_data(data):
    #Rename columns
    cleaned_data = data.rename(columns={0: 'date', 1: 'hour', 2: 'entry', 3: 'exit', 4: 'count'})
    
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
    print(join_cleaned_data[["station"]].drop_duplicates())
    return join_cleaned_data

def clean_data(data):
    #4.1 update the column names
    cleaned_data = data.rename(columns={'County': 'station_cnty', 'station': 'station_abbr', 'Name': 'station_nm'})

    #4.2 fix character issues
    cleaned_data['station_nm'] = cleaned_data['station_nm'].replace({'16th Street Mission': '16th St/Mission', 
                                        '24th Street Mission': '24th St/Mission', 
                                        'Berryessa / North San José': 'Berryessa/North San Jose', 
                                        '12th Street / Oakland City Center': '12th St/Oakland City Center',
                                        '24th Street Mission' : '24th St/Mission',
                                        'Civic Center' : 'Civic Center/UN Plaza',
                                        '19th Street Oakland' : '19th St/Oakland',
                                        'Warm Springs' : 'Warm Springs/South Fremont',
                                        'Coliseum' : 'Coliseum/Airport Connector',
                                        'Powell Street' : 'Powell St',
                                        'Pleasant Hill': 'Pleasant Hill/Contra Costa Centre',
                                        'Montgomery Street' : 'Montgomery St',
                                        'Bayfair' : 'Bay Fair'})
    print(cleaned_data['station_nm'].unique())
    return cleaned_data

def qa_data(data):
    #3.3 EDA: How many stations in each county?
    print()
    print(">> EDA: How many stations per county?")
    print(data[['station', 'County']].drop_duplicates().groupby(by=['County']).count())

    #3.4 EDA: What is the average exits and entrants of each county by year/month? 
    print()
    print(">> EDA: average exits and entrants of each county by year?")
    tempdata = data.copy(TRUE)
    tempdata['year'] = pd.DatetimeIndex(tempdata['date']).year
    temp_yearly = tempdata[['County', 'year', 'cnt_entries', 'cnt_exits']].groupby(by=['County','year']).mean()
    io_hlp.save_data(temp_yearly, "100_QA_files//100_qa_temp_yearly.csv", True)

    print(">> EDA: average exits and entrants of each county by month?")
    tempdata['month'] = pd.DatetimeIndex(tempdata['date']).month
    temp_monthly = tempdata[['County', 'station', 'year', 'month', 'cnt_entries', 'cnt_exits']].groupby(by=['County','year', 'month']).mean()
    io_hlp.save_data(temp_monthly, "100_QA_files//100_qa_temp_monthly.csv", True)

    #3.5 EDA: Do any rows have 0 exits or entrants?
    print()
    print(">> EDA: Any 0 entries or 0 exits?")
    print("Look at the min value for each station.")
    temp_min_cnts = data[['station', 'Name', 'cnt_entries', 'cnt_exits']].groupby(by=['station']).min()
    print(temp_min_cnts)
    io_hlp.save_data(temp_min_cnts, "100_QA_files//100_qa_min_cnts.csv", True)
    

def add_county(data):
    #read in the station name, station code, county crosswalk
    county_xwalk = io_hlp.read_data("User_Created_Data//station_county_xwalk.csv").rename(columns={'Code':'station'})
    
    #Merge the crosswalks based on county code
    joined_xwalk = county_xwalk.merge(data, on=['station'])
    return joined_xwalk



def main():
    #intialize a list for concatenating
    list_df = []

    for y in years:
        print(f"Processing data for {y}")
        yearly_data = io_hlp.read_data(f"Raw_Data//date-hour-soo-dest-{y}.csv", False)   
         # store DataFrame in list
        list_df.append(yearly_data)
    bart_data = pd.concat(list_df)
        
    bart_data_rolledup = rollup_data(bart_data)
    final_dataset = add_county(bart_data_rolledup)
    qa_data(final_dataset)
    final_dataset = clean_data(final_dataset)
    io_hlp.save_data(final_dataset, "User_Created_Data//100_ridership_data.csv")

main()