## Milestone 4: Reflection

So far, we have consistently adhered to the best practices for visualization we learned in 532. We have successfully implemented most of the components outlined in our initial sketch. The only feature yet to be implemented is the CO2 emissions per capita chart. The decision to delay this implementation isn't due to technical challenges; rather, we intend to reserve it as a key enhancement for future versions of the dashboard. The current version remains functional and intuitive, ready to be launched for potential users.

For Milestone 4, we have accomplished the following improvements:

### Major changes

- Add an additional output plot of co2 emissions per capita

- Remove Antarctica from map to improve scaling and allow map to occupy more horizontal white space.

- Changed our processed data file to parquet format to improve dashboard response time

- Add the selected year range to the output text

### Minor changes

- Add a note explaining the average temperature change metric

- Set default tool as box select in world map


### Suggestions we chose not to implement
Peer feedback was a valuable tool for improving on our previous dashboard iteration. While we chose to incorporate most major pieces of feedback, we did not address a suggestion to allow the selection of a single year of data. This is because we want our dashboard to prioritize demonstrating trends over time, and we feel our 15-year minimum toggle is neccesary to show meaningful trends.


### Strengths

Our dashboard provides users with a handy tool for investigating the trend of CO2 emissions among different countries since 1900. We believe it is intuitive to use and has a clean design. There's also a fun fact about the equivalent number of Empire State Buildings in volume to make the number easier to visualize. The interactive world map paired with the country search bar feature enables users to select and visualize data based on personalized needs. Aditionally, the year toggle allows users to observe how relative contributions between selected countries have varied over time.


### Limitations

Point form for now:
- response time will likely still not be great - discuss why
- Plotly selection limitations for individually clicking on countries
- the temperature change per country data - still not totally sure how it was calculated, and can be a bit confusing
- other ideas?

### Future Improvements

Add more functionality? Ideas:
- More outputs - ie toggle for co2 per capita plot
- Data engineering to obtain other data - maybe something we understand better on temp change/country side
