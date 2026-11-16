'''Find below my CPI-based Inflation Calculator.
    This code uses the CSV file provided on the Bank of Canada website (as of November 16, 2026). 
    It provides information like cost changes over time, annual percent changes and more. The calculator was made
    for my second Python coding assignment. I hope you find it useful and enjoy looking through it. Happy coding!'''

import pandas as pd
    # Importing Pandas.

cpi_data = pd.read_csv("BankofCanadaFile.csv", skiprows=8)
    # Reading the CSV file using Pandas. Skipping the first 8 rows to avoid unnecessary/unformated data.
    # For the code to run, the file and code need to be in the same open folder. Alternatively, users can download and input the file themselves.
cpi_data = cpi_data.rename(columns={'STATIC_INFLATIONCALC':'cpi'})
    # Renaming column in the name of understandability and consistency.

cpi_data['date'] = pd.to_datetime(cpi_data['date'])
    # Changing the type of the data in the 'date' column to datetime. 
    # Parses the data. Comes in handy when looking up values later.

def cpi_value (date):
    if cpi_data['date'].max() >= date >= cpi_data['date'].min():
        value = cpi_data[(cpi_data['date'].dt.year == date.year) 
                         & (cpi_data['date'].dt.month == date.month)]
        return value['cpi'].iloc[0]
    
    # This function locates the CPI data from the CSV file. It goes through the file, into the 'date' column, then locates the index in the 'cpi' column.
    # The equality operations ensure that the year and month given are correctly used in finding their corresponding CPI level.
    # Only using one function, referencing it for each of the two dates required in the calculations.
   
    else:
        print(60*'-')
        print('The date that you inputted is not within the available range.\nOnly dates between 1914-01 and 2026-09 are accepted.\nTo avoid an error, re-run the code with dates that are in the functional range.')
        print(60*'-')
        return None
    
    # The 'if' statement ensures that the dates are within range. Otherwise, it prints the statement above.

def inflation_calculator (cost1, cpi1, cpi2, date1, date2):
    # This function takes the different CPI levels, dates and the initial cost and performs all required calculations.
        # These values are provided by the user, prompted by the inputs at the bottom of the code.
        # Accordingly, it prints the messages with formatted answers based on inputs provided.
    
    cost2 = cost1 * (cpi2/cpi1)
    percent_change = (cost2-cost1)/cost1 * 100

    print(100*'-')
    print('A "basket" of goods and services that cost ${:,.2f} (CAD) in {}, would cost ${:,.2f} (CAD) in {}!'.format(cost1, date1.strftime("%B %Y"), cost2, date2.strftime("%B %Y")))
    print('The percent change totalled: {:,.2f}%.'.format(percent_change))


    if date1 != date2:
        time_elapsed = date2-date1
        number_of_years = time_elapsed/pd.Timedelta(days=365.2425)
        average_annual_inflation = ((percent_change/100+1)**(1/abs(number_of_years))-1) * 100

        print('This is equal to a rate of {:,.2f}%, compounded annually over {:,.0f} years.'.format(average_annual_inflation, abs(number_of_years)))
        print('The CPI for {} is {:,.1f}, while the CPI for {} is {:,.1f}.'.format(date1.strftime("%B %Y"),cpi1, date2.strftime("%B %Y"), cpi2))
        print(100*'-')
        return cost2

        # Above lies all of the main calculations with their user outputs.
    
    else:
        print(100*'-')
        print('The dates inputted are equal. The cost at the first date is equal to the cost at the second date.\nThe percentage change is 0%.')
        print(100*'-')
        return None

        # If the dates provided are equal, a special message will be delivered explaining such.


date1 = pd.to_datetime(input('Please enter the date of the first period (YYYY-MM): ').strip(), format='%Y-%m')
cpi1 = cpi_value(date1)

date2 = pd.to_datetime(input('Enter the second date (YYYY-MM): ').strip(), format='%Y-%m')
cpi2 = cpi_value(date2)

cost1 = float(input('Enter the cost of the "basket" at the first date (with no formatting): ').replace('$','').replace(',',''))
    # cost1, cpi1, cpi2, date1 and date2 all work in the inflation_calculator function. They are defined here when inputted.
    # Certain formatting adjustments are used to help validate the code. Formatting advice is also explicitly stated.

initiate_calculations = inflation_calculator(cost1, cpi1, cpi2, date1, date2)
    # Used to call on function; performs calculations and prints results.