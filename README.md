# data_viz_covid_bart

Goal: Interactively visualize how COVID Cases at the county level impacted BART Ridership.

## Data Source #1 COVID Data
**Url:** [CA CDPH](https://www.buzzfeed.com/donnad/9-pokemon-inspired-high-fashion-designs?s=mobile)
**Key Data Documentation Notes:**
- "Data is from the California COVID-19 State Dashboard at https://covid19.ca.gov/state-dashboard/"
- "NOTE: Data is being updated on Tuesdays and Fridays."
- "Data on cases, deaths, and testing is not reported on weekends or state holidays. This data is reported on the first day following the weekend or holiday. All metrics include people in state and federal prisons, US Immigration and Customs Enforcement facilities, US Marshal detention facilities, and Department of State Hospitals facilities. Members of California's tribal communities are also included."
**Clean Up Requirements:**
1. Remove State level sums (tableau will calculate this manually)
2. Keep only Bay Area counties with Bart Stations
3. Roll up to the week level (?)

## Data Source #2 BART Ridership Data
**Url:** [Bay Area Rapid Transit](https://www.bart.gov/about/reports/ridership) > Hourly Data 
**Key Data Documentation Notes:**
- "For those of you looking to take a deeper dive into BART’s data - check out our hourly trip datasets. These files will allow you to analyze trips between all stations in the BART system by hour. The data is organized in the following columns: Date, Hour (24-hour clock), Origin Station, Destination Station, Number of Exits. All stations are abbreviated using the 4-Letter station codes, please refer to the station name abbreviations (.xls) for translation."
**Clean up Requirements:**
1. Crosswalk between station code and the Station Name
2. Include Station County as a linkage variable
3. Roll up to the day level (at the exit-entrant level)

## Data Source #3 BART  Geospatial Data
**Url:** [Bay Area Rapid Transit](https://www.bart.gov/schedules/developers/geo) > KML Format
**Key Data Documentation Notes:** n/a
**Clean up Requirements:**
1. Crosswalk between Ridership Data (Station Code) and geographical Bart Station location
