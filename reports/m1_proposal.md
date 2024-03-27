## Section 2: Description of the data
The dataset we will be visualizing contains approximately 50,000 rows of CO2, energy consumption, and general population data spanning 264 countries. There is one data point per location per year between as early as 1750 until 2022. The dataset contains 79 features, however it is important to note that only 1200 of the rows contain values for all 79 features. We will focus on visualizing features with fewer missing values, and discuss the best strategies for imputation where needed.
We think the following features are of particular interest for creating insightful visualizations that demonstrate how a country’s size and wealth relate to its impact on climate change: <br>
* `co2` which contains the total CO2 emission in a given year for a given country
* `temperature_change_from_co2` which contains the temperature change due to CO2 in a given year for a given country
* `co2_per_capita` which describes the CO2 emission per capita in a given year for a given country
* Information related to country demographics such as `country`, `population`, and `gdp`
All of the features selected above have at least 30,000 non-null entries. Another feature that would be interesting for visualization would be the total global mean temperature change for a given year, which we can get by adding the individual temperature change contribution columns, or derive using another data source such as  NOAA National Centers for Environmental Information.
