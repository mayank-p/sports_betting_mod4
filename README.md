# sports_betting_mod4

**Data Source**: https://stats.nba.com/teams/boxscores-traditional/?Season=2019-20&SeasonType=Regular%20Season

**Problem**: Can I predict NBA games based on information from games played

# Noteook 1
**Collecting Data**: Got scraped data from the data source provided above.

# Noteook 2

**Cleaning**: For the baseline model, I took out data that I felt I didn't need such as Date, Season, etc. Then I created targets for the dataset for covering the spread and if they did or not based on the plus/minus, which indicates how much a team won or lost by. Then I deleted that column and saved the new data frame as a csv file to then train my models in the next noteook.

# Noteook 3

**Modeling**: I ran a simple log regression model for each of the targets indicating spread and cross validated the test set with approximately 90% accuracy. However, my predictions constantly said true for whatever test I gave it. Any ideas would be helpful for making it better. Maybe having probabilities of the stats' standard deviation might be helpful.
