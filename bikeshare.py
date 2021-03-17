import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
            'new york city': 'new_york_city.csv',
            'washington': 'washington.csv' }

def filters():
    """
    This function selects the city to explore its data.

    The user is asked to select a city.
    The input is verified to be in CITY_DATA

    Returns:
    city: (str) name of the selected city
    """
    while True:
        city = input('Please, select one city: chicago, new york city or washington\n').lower()
        #Checks if the input is a correct city in CITY_DATA:
        if city in CITY_DATA:
            print('\nYou have selected: {}\n'.format(city).title())
            return city
        else:
            print('{} is not a valid city. Try again.\n'.format(city))

def load_data(city):
    """
    Loads data for the specified city and filters by month, day, both or none,
    depending on the user selection.

    Args:
        (str) city - name of the city to analyze

    Returns:
        df - pandas DataFrame containing city data filtered by month and/or day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day from the Start Time column to create month and day columns:
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # list of month, day values that exist in df:
    month_list = df['month'].unique().tolist()
    day_list = df['day_of_week'].unique().tolist()
    # possible filters to be applied
    filter_list = ['month', 'day', 'both', 'none']
    # default value for month and day filters:
    month = 'all'
    day = 'all'
    while True:
        #asks user to input filters:
        filter = input('\nWould you like to filter the data by month, day, both or none?\n').lower()
        #check if filter is correct
        if filter in filter_list:
            if filter == 'both' or filter == 'month':
                #asks input for month and checks if it is correct
                while True:
                    month = input('\nSelect month: {}\n'.format(month_list)).title()
                    if month in month_list:
                        print('\nSelected month: {}\n'.format(month))
                        break
                    else:
                        print('\nNot a correct filter for month')
            if filter == 'both' or filter == 'day':
                #asks input for day and checks if it is correct
                while True:
                    day = input('\nSelect day: {}\n'.format(day_list)).title()
                    if day in day_list:
                        print('\nSelected day: {}\n'.format(day))
                        break
                    else:
                        print('\nNot a correct filter for day')
            if filter == 'none':
                print('\nNo filter applied')
            break
        else:
            print('\nNot a correct filter. Try again')
    #if the user has applied any filter, the df will be filtered accordingly:
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    return df

def pop_times(df):
    """
    This function provides information about popular times of travel

    Args:
        df - pandas DataFrame containing city data filtered by month and day

    The function prints:
        - most frequent month
        - most frequent day of the week
        - most frequent start hour

    Returns: nothing
    """
    print('*'*30, '\nPOPULAR TIMES OF TRAVEL \n')
    #extract hour from Start Time to create new hour column
    df['hour'] = df['Start Time'].dt.hour
    # prints the most frequent month
    print('Most frequent month: {}'.format(df['month'].value_counts().index[0]))
    print('-' * 30)
    # prints the most frequent month
    print('Most frequent day of the week: {}'.format(df['day_of_week'].value_counts().index[0]))
    print('-' * 30)
    # prints the most frequent start hour
    print('Most frequent start hour: {} \n'.format(df['hour'].value_counts().index[0]))

def stations(df):
    """
    This function provides information about stations and trips

    Args:
        df - pandas DataFrame containing city data filtered by month and day

    The function prints:
        - most common start station and number of times used
        - most common end station and number of times used
        - most common trip and number of times ridden

    Returns: nothing
    """
    print('*'*30, '\nPOPULAR STATIONS AND TRIP: \n')
    #prints most popular start station and the number of times used
    print('Most common start station: {}'.format(df['Start Station'].value_counts().index[0]))
    print('Number of times as start station: {}'.format(df['Start Station'].value_counts()[0]))
    print('-' * 30)
    #prints most popular end station and the number of times used
    print('Most common end station: {}'.format(df['End Station'].value_counts().index[0]))
    print('Number of times as end station: {}'.format(df['End Station'].value_counts()[0]))
    print('-' * 30)
    #new trip column as aggregation of start station + to + end station
    df['Trip'] = df['Start Station'] + str(' to ') + df['End Station']
    #prints most common trip and the number of times ridden
    print('The most common trip is: {}'.format(df['Trip'].value_counts().index[0]))
    print('which has been ridden {} times \n'.format(df['Trip'].value_counts()[0]))

def trip(df):
    """
    This function provides information about trip duration

    Args:
        df - pandas DataFrame containing city data filtered by month and day

    The function prints:
        - total travel time
        - average travel per trip
    Returns: nothing
    """
    print('*'*30,'\nTRIP DURATION:\n')
    #prints total travel time. sum of trip duration column
    print('Total travel time: {} seconds'.format(df['Trip Duration'].sum()))
    print('-' * 30)
    #prints average travel time
    print('Average travel time: {} seconds \n'.format(df['Trip Duration'].mean()))

def user_info(df):
    """
    This function provides information about user characteristics

    Args:
        df - pandas DataFrame containing city data filtered by month and day

    The function prints:
        - type and amount of users
        - gender and amount of users
        - earliest, most recent and most common birth year

        *if any information does not exist, the function prints 'x information is not available'

    Returns: nothing
    """
    print('*'*30,'\nUSER INFORMATION:\n')
    #prints type and amount of users types
    print('User type:    Amount:\n')
    print(df['User Type'].value_counts().to_string())
    print('\nNo User type information in {} trips.'.format(df['User Type'].isnull().sum()))
    #to_string() used to remove Name and dtype from output
    print('-' * 30)
    try:
        #when 'Gender' column exists, breaks down genders, amount and also cases with null information
        gender = df['Gender'].value_counts().to_string()
        print('\nGender:   Amount:\n')
        print(gender)
        print('\nNo Gender information in {} trips.'.format(df['Gender'].isnull().sum()))
        print('-' * 30)
    except KeyError:
        #when there is no 'Gender' column, prints the message:
        print('\nGender information is not available')
    try:
        #when 'Birth Year' column exists, prints earliest, most recent and most common birth year
        #np.int64 to change type of output from float64 to int64
        early_yb = np.int64(df['Birth Year'].min(skipna = True))
        recent_yb = np.int64(df['Birth Year'].max(skipna = True))
        mcommon_yb = np.int64(df['Birth Year'].mode()[0])
        print('\nBirth year information:\n')
        print('Earliest birth year: {}\n'.format(early_yb))
        print('Most recent birth year: {}\n'.format(recent_yb))
        print('Most common birth year: {}\n'.format(mcommon_yb))
        print('-' * 30)
    except KeyError:
        #when there is no 'Birth Year' column, prints the message:
        print('\nBirth information is not available\n')

def raw_data(df):
    """
    This function prints raw data of the filtered information

    Args:
        df - pandas DataFrame containing city data filtered by month and day

    The user is asked to print raw data in groups of 5 lines (trips).
    As the user answers 'y' the function prints 5 rows of trip data.
    The function stops printing (or does not start) when the user inputs 'n'

    Returns: nothing
    """
    rows = 0
    while True:
        print_rows = input('Would you like to print the first 5 lines of raw data? (y) (n)\n').lower()
        while print_rows == 'y':
            print(df.iloc[rows:rows + 5])
            rows += 5
            print_rows = input('Continue with next 5 lines? (y) (n)\n').lower()
        if print_rows == 'n':
            break
        elif print_rows != 'n' and print_rows != 'y':
            print('Try again')


def main():
    """
    This is the main function
    It calls the other functions
    """
    while True:
        print('\nEXPLORE US BIKESHARE DATA')
        city = filters()
        df = load_data(city)
        pop_times(df)
        stations(df)
        trip(df)
        user_info(df)
        raw_data(df)
        while True:
            #the user is asked to restart.
            restart = input('\nRestart and select city again? (y) (n)\n').lower()
            if restart != 'y' and restart != 'n':
                print('Try again\n')
            else:
                break
        #if the user inputs 'n' the program ends
        if restart == 'n':
            break

if __name__ == "__main__":
	main()
