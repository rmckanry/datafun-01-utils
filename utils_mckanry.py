''' ITERATION 5

Module: Insights Professional Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this fifth iteration, I will present the min, max, mean, and standard deviation for both the company and my own variables.
I will update the byline code to display these values
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

other_min: float = 0.0
other_max: float = 0.0
other_mean: float = 0.0
other_stdev: float = 0.0

#List of strings 
skills_offered: list = ["Data Analytics", "Machine Learning", "Business Intelligence"]

#List of floats 
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
other_list_of_scores: list = [10.2, 20.3, 15.5, 5.4, 32.8, 25.6, 20.2]

#####################################
# Calculate min, max, mean, and stdev
#####################################

min_score = min(client_satisfaction_scores)
max_score = max(client_satisfaction_scores)
mean_score = statistics.mean(client_satisfaction_scores)
stdev_score = statistics.stdev(client_satisfaction_scores)

other_min = min(other_list_of_scores)
other_max = max(other_list_of_scores)
other_mean = statistics.mean(other_list_of_scores)
other_stdev = statistics.stdev(other_list_of_scores)

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
Other List of Scores:        {other_list_of_scores}

Display Company Min, Max, Mean, and Standard Deviation:
Client Score Minimum:        {min_score}
Client Score Maximum:        {max_score}
Client Score Mean:           {mean_score}
Client Standard Deviation:   {stdev_score}

Display Additional Min, Max, Mean, and Standard Deviation:
Other Score Minimum:         {other_min}
Other Score Maximum          {other_max}
Other Score Mean:            {other_mean}
Other Standard Deviation:    {other_stdev}
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
