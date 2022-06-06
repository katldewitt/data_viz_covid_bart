# CS416 Dashboard: COVID's Impact on BART Ridership

**[Dashboard url](https://public.tableau.com/views/COVIDsImpactonBARTRidership/FinalDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)**

*Title*:  COVID's Impact on BART Ridership

*Caption*: The Bay Area Rapid Transit (BART) system connects five Bay Area counties. Prior to the COVID19 Pandemic, ridership consisted of over 400,000 trips on an average weekday ([source Bart.gov](https://www.bart.gov/sites/default/files/docs/2019%20BARTFacts2019%20FINAL.pdf)). Starting in March 2020, BART ridership decreased dramatically due to the social distancing mandates. The goal of this dashboard is to put county-level COVID data in communication with station-level ridership data to allow the end user to explore the story of how COVID and public transit in the Bay Area.

*What is one question that the dashboard can answer by utilizing two or more simultaneously displayed charts?*

Question: How did San Francisco county's BART stations' ridership change overtime relative to COVID case count per capita during the Omicron wave in winter 2021-2022? 

Answer: We notice that ridership dipped slightly during the Omicron surge in the end of 2021 and beginning of 2022, but this may be due to the holiday period when ridership typically is lower. Overall, it does not appear that the omicron spike discourage ridership in a significant way given the continued upward trend in January that may be related to the push to return to office. 

How: The three charts work in harmony to provide this information. The map demonstrates the geographical layout of the stations in SF, while the COVID Case count illustrates when the omicron spike occurred. Finally, the Ridership chart demonstrates the actual result of the question (the drop relative the previous few weeks). I utilized cross filtering to get this data by subsetting the years to 2021 and 2022 and the county to San Francisco.

*How does the layout of these charts promote visual understanding of the data across multiple charts? Make sure your explanation describes color consistentcy, alignment and any other ways the layout improves visual understanding.*

*How does your dashboard provide details on demand?*
I've added a tooltip that allows the user to see the Station Name, the County, the total number of COVID deaths in the time period, and the total number of station entries. The tool tip allows the end use to explore which stations are more populous before interacting more.

*Indicate which chart is the "first" chart. Then justify the choice of this chart type, its axes and marks based on the data variables it shows.*

*Indicate which chart is the "second" chart. Then justify the choice of this chart type, its axes and marks based on the data variables it shows.*

*How does your dashboard support cross-filtering between these two charts?*
I support cross-filting of station county, station name, and year. If someone selects a particular county, the stations in that county are the only ones listed in the map and both graphs limit to the ridership and case count of that county. An additional detail is that my second filter, station name, will subset to only relevant options (i.e. only stations within that county). I added a filter for year as well to allow users to turn off the 2019 ridership data once they undrestand the previous way the BART system used to operate.

*Challenges of designing this chart*:
1. Since the COVID Data are at the county level and reported on biweekly basis (1 time every 2 weeks), I decided to use the weekly total to ensure artificial spikiness was not introduced into the data.
2. Additionally, the population of each county varies, which means that a few thousand COVID cases in a smaller county may be a different signal than a more populous county. For this reason, I normalized the data to be cases per capita (Case count / population * 100,000).
3. Inclusion of the 2019 data for ridership was intentional to allow the user to see the drastic decrease in the ridership. However, this makes the graph axes very spikey. I attempted to use a year filter to allow the user to turn this off once they understand the big picture.

## Data Source #1 COVID Data

**Url:** [CA CDPH](https://data.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state)

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

## Data Source #4 CA County Shape File

**Url:** [CA Data.gov](https://data.ca.gov/dataset/ca-geographic-boundaries) > CA County Boundaries

**Key Data Documentation Notes:** n/a

**Clean up Requirements:**
1. [Spatial join in Tabelau](https://www.tableau.com/about/blog/2018/8/perform-advanced-spatial-analysis-spatial-join-now-available-tableau-92166)


**Tutorials Used in Tableau**
1. https://community.tableau.com/s/news/a0A4T000001v7SCUAY/dual-axis-mapping-many-ways
2. https://community.tableau.com/s/question/0D54T00000C6SBCSA3/getting-tableau-county-info-for-plotted-latlong
