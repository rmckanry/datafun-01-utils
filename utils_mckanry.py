''' ITERATION 3

Module: Insights Professional Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this third iteration, I declared variables to show skills with different data types.
'''

#####################################
# Declare a global variable named byline.
#####################################

#Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

#Integer variable for the number of years in operation
years_in_operation: int = 10

#List if strings representing the skills offered by the company
skills_offered: list = ["Data Analytics", "Machine Learning", "Business Intelligence"]

#List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#####################################
# Declare a global variable named byline
#####################################

byline: str = f"""
-------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
-------------------------------------------------------
Has International Clients:   (has_international_clients)
Years of Operation:          (years_in_operation)
Skills Offered:              (skills_offered)
Client Satisfaction Scores:  (client_satisfaction_scores)
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
