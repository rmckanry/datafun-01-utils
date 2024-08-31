''' ITERATION 4

Module: Insights Professional Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this fourth iteration, I will declare additional variables and import the statics function.
It will use min(), max(), mean(), and the standard deviation functions.
'''

#####################################
# Import Statistics module
#####################################

import statistics

#####################################
# Declare a global variable named byline.
#####################################

#Boolean variable
has_international_clients: bool = True

#Integer variable 
years_in_operation: int = 10

#Float variables
min_score: float = 0.0
max_score: float = 0.0
mean_score: float = 0.0
stdev_score: float = 0.0

#List of strings 
skills_offered: list = ["Data Analytics", "Machine Learning", "Business Intelligence"]

#List of floats 
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#####################################
# Calculate min, max, mean, and stdev
#####################################

min_score = min(client_satisfaction_scores)
max_score = max(client_satisfaction_scores)
min_score = statistics.mean(client_satisfaction_scores)
min_score = statistics.stdev(client_satisfaction_scores)

#####################################
# Declare a global variable named byline
#####################################

byline: str = f"""
-------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
-------------------------------------------------------
Has International Clients:   {has_international_clients}
Years of Operation:          {years_in_operation}
Skills Offered:              {skills_offered}
Client Satisfaction Scores:  {client_satisfaction_scores}
"""

#####################################
# Declare get_byline function to return byline text.
#####################################
def get_byline() -> str:
   '''Returns byline for analysys'''
   return byline

#####################################
# Define a main() function for this module.
#####################################
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
