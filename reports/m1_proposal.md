# Proposal

## Section 1: Motivation and purpose

The Earth\'s climate is changing and it can be detrimental to environmental stability, human health, and economic prosperity across the globe. From more frequent storms and floods to unprecedented heatwaves, we\'re feeling the impacts of global warming and necessitates for informed action.

Given consensus among scientists that human activities, especially the emission of carbon dioxide (CO2), are the number one contributor to the global warming, we aim to build an innovative tool to visualize this relationship in an intuitive way. To be more specific, we want to inspect the intricate dynamics between CO2 emissions, global temperature changes, and economic activity indicators (e.g GDP per capita) over the years. By providing a user-friendly interface that allows for investigating the data both globally and at the country level, the dashboard seeks to make the abstract and sometimes overwhelming data on climate change more tangible and understandable. Going beyond merely presenting statistics, our dashboard offers a compelling narrative on the evolution of CO2 emissions over time. It utilizes a diversified visual tools, including line charts, bar charts, and maps to vividly illustrate the profound impact of human activities on our planet's climate.

Possible users and stakeholders who would find value in our dashboard include governments, policy makers, scientists and environmental advocacy organizations. Please find more detailed discussion of the use cases in section 3.

## Section 2: Description of the data

The dataset we will be visualizing contains approximately 50,000 rows of CO2, energy consumption, and general population data spanning 264 countries. There is one data point per location per year between as early as 1750 until 2022. The dataset contains 79 features, however it is important to note that only 1200 of the rows contain values for all 79 features. We will focus on visualizing features with fewer missing values, and discuss the best strategies for imputation where needed. We think the following features are of particular interest for creating insightful visualizations that demonstrate how a country's size and wealth relate to its impact on climate change: <br>

-   `co2` which contains the total CO2 emission in a given year for a given country
-   `temperature_change_from_co2` which contains the temperature change due to CO2 in a given year for a given country
-   `co2_per_capita` which describes the CO2 emission per capita in a given year for a given country
-   Information related to country demographics such as `country`, `population`, and `gdp`

All of the features selected above have at least 30,000 non-null entries. Another feature that would be interesting for visualization would be the total global mean temperature change for a given year, which we can get by adding the individual temperature change contribution columns, or derive using another data source such as NOAA National Centers for Environmental Information.

## Section 3: Research questions and usage scenarios

**A few research questions we could answer based on this:**

1.  How have global CO2 emissions evolved over the past few years?
2.  What are the leading countries that have policies to reduce CO2 emissions?
3.  How does the increase in CO2 emission correlate with changes in average global temperature?

**Some personas that will be using our dashboard:**

-   Sarah is a university student who volunteers for an organization to combat climate change. She aims to understand CO2 emission trends to raise awareness among her peers and advocate for more effective policies.
-   Walkthrough:
    -   Sarah opens the dashboard and adjusts the year from 2010 to now
    -   Sarah clicks on her country of focus, Indonesia, and seeks to understand its cumulative CO2 emissions compared to the global values and the top countries. </br>
-   Drake is a policy maker in the EU (European Union) responsible for environmental regulations. He aims to identify countries in Europe with the highest emissions to inform policy decisions and allocate resources.
-   Walkthrough:
    -   Drake opens the dashboard and adjusts the year from when he implemented a desired policy (e.g. 2015).
    -   He then selects all the countries in Europe to track
    -   He then compares the CO2 emission and trends of all these countries and how the policy implemented affected it
    -   Based on his analysis, he formulates recommendations for the policies and addresses issues

## Section 4: App sketch and description

Below is a sketch of our proposed dashboard.

![sketch](../img/sketch.png)

Our proposed dashboard comprises two parts. At the top, we provide our users with general statistics regarding the total CO2 emission for any given year, which can be adjusted by the toggle bar on the top left hand side. Based on this information, we can also see the top 10 countries in order of CO2 emission at a given point in time (as measured by cumulative CO2 emission up until that year), as well as the CO2 emission per capita for that specific year. Note that the default is set to the most recent year in which data is available (i.e., 2022).

At the bottom, the dashboard provides users with a way to explore the data for a given country in more detail. By default, the map shows the degree of CO2 emission by country on a colour scale, and next to it, the cumulative CO2 emission over time (orange line) as well as the change in average global temperature across the same time frame for reference (dotted blue line). Note that the latter does not change, as it serves as a meausre of global temperature change over time. By clicking on a specific country (e.g., Canada), the user will be able to see its specific cumulative CO2 emission over time.
