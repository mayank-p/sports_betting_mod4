# Sports_Betting_mod4

**Data Source**: https://stats.nba.com/teams/boxscores-traditional/?Season=2019-20&SeasonType=Regular%20Season

**Problem**: Can I predict the spread of NBA games based on halftime scores and stats?

## Notebook 1 and 2
**Collecting Data**: Got scraped data from the data source provided above. I used chromedriver, BeautifulSoup, and selenium, got the xpaths for the stats that I wanted to model on like first half stats and full game stats. If you want to run these notebooks and get updated stats, then you can copy and paste the xpaths in the functions and try running it again. 

## Notebook 3

**Cleaning**: For the baseline model, I took out data that I felt I didn't need such as Date, Season, etc. Then I created targets for the dataset for covering the spread and if they did or not based on the plus/minus, which indicates how much a team won or lost by. Then I deleted that column and saved the new data frame as a csv file to then train my models in the next notebook.

## Notebook 4

**Modeling**: I ran a simple log regression model for each of the targets indicating spread and cross validated the test set ranging from 70 to 80% accuracy. This notebook also has functions for finding feature importances for each model that identifies what features are the most important for each different model. The higher point spreads end up having a lower F1 score, which is a combination in the confidence the model is in predicting the true positive rate and getting it right. In order to make it better, I will have to try using imbalancing methods in order to get it more information.

## Notebook 5

**Predicting**: This notebook allows you predict game outcomes based on halftime stats. By running the get_bet() function, you can enter the halftime stats of a team, and the function will predict how much the team will win by and how confident it is. You can set whatever threshold you want in order to decide what to actually bet on. 

# Next Steps

Next steps for these models would include adding more stats, like advanced stats such as rating, including opponent's stats during halftime, and adding spread lines and odds during halftime as features. 
