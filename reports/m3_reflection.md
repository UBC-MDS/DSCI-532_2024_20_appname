## Milestone 3: Reflection

So far, we have consistently adhered to the best practices for visualization we learned in 532. We have successfully implemented most of the components outlined in our initial sketch. The only feature yet to be implemented is the CO2 emissions per capita chart. The decision to delay this implementation isn't due to technical challenges; rather, we intend to reserve it as a key enhancement for future versions of the dashboard. The current version remains functional and intuitive, ready to be launched for potential users.

For Milestone 3, we have accomplished the following improvements:

### Major changes

-   Add map interactivity to select countries from the map by either clicking (for selecting only one country) or circling (for selecting multiple countries).

-   Optimize dashboard layout. We moved the widgets and summary statistics to the left sidebar, while we positioned the more detailed charts and map on the right side to fill the entire screen.

-   Adjust color scheme in CSS styling. Our final choice is coloring the sidebar light grey and leaving the other spaces (including the title) white because this scheme won the vote and looks more aesthetically appealing than the previous scheme. Also, to attract sufficient attention and to be more consistent with the name of the dashboard---Hotspot---we changed the bar charts to all red.

-   Make clearer separation between columns.

### Minor changes

-   Remove the label "country" from the bar plot.

-   Add units to some missing labels in the plot.

-   Use a log scale for the map colors for better visualization. We did this because the emissions from top emitters would overshadow the other countries if we used the original scales.

-   Remove the scale label for the map.

-   Change file structures to follow best practices (break into components, callbacks, and data).

### Inspiration from Peers
Looking at our peers' dashboards, we realized we could utilize the space on our dashboard better and make our map visualation more prominent. In particular, we really liked the layout group 9 (Solar Savers) chose for their dashboard, with the toggles in the side bar, and minimal white space at the top of the dashboard. We implemened this in our own dashboard on this milestone to make our dashboard more aesthetic.

### Strengths

Our dashboard provides potential users with a handy tool for investigating the trend of CO2 emissions among different countries since 1900. The card in the sidebar gives the user a sense of how much CO2 is emitted based on the filtering condition. There's also a fun fact about the equivalent number of Empire State Buildings in volume to make the number more intuitive. The interactive world map enables users to select and visualize data based on personalized needs. For example, users can circle the continent they are interested in to check the total emissions and top emitters in that specific continent.

### Limitations and Future Improvements

One notable limitation of the current dashboard is its presentation of absolute CO2 emissions data without accounting for per capita emissions or emissions intensity relative to GDP. Incorporating per capita emissions and GDP-adjusted emissions metrics would offer a more nuanced view, allowing for fairer comparisons and a clearer understanding of each country's relative impact and efficiency in terms of emissions. 

We would also like to implement more of the feedback we received from our peers in Milestone 4. Some peers pointed out that there is a use case to visualize a single year of data, so we could add this functionality rather than keeping our multi-year restriction on the filtering. We would also like to improve the response time of our dashboard, perhaps by reducing the size of our dataset. Finally, we could make our dashboard responsive to screen size so users do not need to scroll to view the entire dashboard.