# 101_COVID_cleanup
# Purpose: Clean COVID data from CA Department of Public Health
# Author: Kathryn DeWitt (kdewitt3)
# Specifications:
'''
1. Read in the daily level file for COVID cases and deaths
2. Drop counties that do not have BART Stations
    2.1 QA: Verify this drop with a crosstab.
3. Check for data quality
    3.1 EDA: Are there any negative case counts or negative deaths?
    3.2 EDA: Are there any invalid dates?
4. Save the final file as a .csv 
    4.1 The file should be called "101_covid_daily_data"
    4.2 The file must have the following variables:
        date                   -  format mm/dd/yyyy
        county_code            -  Numeric county code from CDPH
        county                 -  Full county name
        cases                  - an int of the number of cases for the county on date
        deaths                 - an int of the number of deaths for the county on date
        population             - an int representing the reported population of county (used to calculate percapita COVID statistics)
        TODO: Hospitilizations too? Need alternate data source
'''


import numpy

def read_data():
    pass

def clean_data():
    pass

def save_data():
    pass

def main():
    read_data()
    clean_data()
    save_data()

main()