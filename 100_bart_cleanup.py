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
        entry_station_abbr     -  4 letter station abbreviation
        entry_station          -  Full station name
        entry_station_cnty     - The county in which the exit station resides 
        cnt_entries            - int representing number of entries to entry station on date
        exit_station_abbr      - 4 letter station abbreviation
        exit_station           - Full station name
        exit_station_cnty      - The county in which the exit station resides 
        cnt_exits              - int representing number of entries to entry station on date
'''

import numpy

def read_data():
    pass

def add_county():
    pass

def save_data():
    pass

def main():
    read_data()
    add_county()
    save_data()

main()