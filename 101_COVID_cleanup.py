# 101_COVID_cleanup
# Purpose: Clean COVID data from CA Department of Public Health
# Author: Kathryn DeWitt (kdewitt3)
# Specifications:
'''
1. Read in the daily level file for COVID cases and deaths
2. Drop counties that do not have BART Stations
    2.1 QA: Verify this drop with an assertion.
3. Check for data quality
    3.1 EDA: Are there any negative case counts or negative deaths?
    3.2 EDA: Are there any invalid dates?
4. Save the final file as a .csv 
    4.1 The file should be called "101_covid_daily_data"
    4.2 The file must have the following variables:
        date                   -  format mm/dd/yyyy
        county                 -  Full county name
        cases                  - an int of the number of cases for the county on date
        deaths                 - an int of the number of deaths for the county on date
        population             - an int representing the reported population of county (used to calculate percapita COVID statistics)
        TODO: Hospitilizations too? Need alternate data source
'''

import datetime as dt
import pandas as pd
import io_helper as io_hlp

###Set up key variables##
#The counties with a BART Station
counties_to_keep = ["Alameda", "Contra Costa", "San Francisco", "San Mateo", "Santa Clara"]

def clean_data(data):
    #General: Keep only useful columns
    data_cleaned = data[['date', 'area', 'population', 'cases', 'deaths']]

    #2. Drop counties that do not have BART Stations
    data_cleaned = data_cleaned[data_cleaned['area'].isin(counties_to_keep)]

    #2.1 QA: Verify this drop with a assertion.
    assert all(data_cleaned['area'].unique() == counties_to_keep)

    #3.1 EDA: Are there any invalid cases?
    any_negative = data_cleaned['cases'].min()
    if any_negative < 0:
        print(f"Warning! Found cases with negative values.")

    #3.1 EDA: Are there any invalid deaths?
    any_negative = data_cleaned['deaths'].min()
    if any_negative < 0:
        print(f"Warning! Found deaths with negative values.")


    #3.2 EDA: Are there any invalid dates?
    num_na_dates =  data_cleaned.isnull().sum().sum()
    if num_na_dates > 0:
        print(f"Found {num_na_dates} dates with NA's. Removing these rows.")
        #3.2 Genearal: Remove NaN dates, which are culmative totals
        data_cleaned = data_cleaned[data_cleaned['date'].notna()]

        #Verify this worked
        num_na_dates = data_cleaned.isnull().sum().sum()
        assert num_na_dates == 0

    #4.2 Meet column name specifications
    data_cleaned = data_cleaned.rename(columns={"area": "county"} )

    return data_cleaned


def main():
    covid_data = io_hlp.read_data("covid19cases_test.csv")
    covid_data = clean_data(covid_data)
    io_hlp.save_data(covid_data, "101_covid_daily_data.csv")

main()