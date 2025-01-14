import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['January', 'February', 'March', 'April', 'May', 'June','All']
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = str(input('Please enter Chicago, New York City, or Washington \n')).lower()
        if city not in cities:
            print('Please enter a valid city name')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = str(input('Please enter one of the first 6 months or enter All if you want to select all 6 months.\n')).title()
        if month not in months:
            print('This is invalid.  Please retry. ')
        else:
            break
                       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Please enter a day of the week that you want to filter out.  If not, enter ALL.\n')).title()
        if day not in days:
            print('Please enter a valid day')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # create new columns for month and day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'All':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode=df['month'].mode()[0]
    print('The most common month is: {}'.format(months[month_mode-1]))

    # TO DO: display the most common day of week
    print('The most common day of the week is: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}'.format(df['hour'].mode()[0]))
    

    print("\nThis took %s seconds." % (round((time.time() - start_time),2)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most commonly used end station is: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combination = df['Start Station'].map(str) + ' to ' + df['End Station']
    print('The most frequent combination of start station and end station is: {}'.format(most_common_combination.mode()[0]))

    print("\nThis took %s seconds." % (round((time.time() - start_time),2)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_m, total_s = divmod(df['Trip Duration'].sum(), 60)
    total_h, total_m = divmod(total_m, 60)
    print ('The total travel time is: ',total_h,' hours, ', total_m,' minutes, and ', total_s,' seconds.')

    # TO DO: display mean travel time
    mean_m, mean_s = divmod(df['Trip Duration'].mean(), 60)
    mean_h, mean_m = divmod(mean_m, 60)
    print ('The average travel time is: ',mean_h,' hours, ', mean_m,' minutes, and ', mean_s,' seconds.')

    print("\nThis took %s seconds." % (round((time.time() - start_time),2)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The user can be broken down into \n{}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if('Gender' not in df):
        print('Sorry! Gender data unavailable for Washington')
    else:
        print('The genders are \n{}'.format(df['Gender'].value_counts()))
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('Sorry this birth year data is unavailable for Washington!')
    else:
        print('The Earliest birth year is: {}'.format(int(df['Birth Year'].min())))
        print('The most recent birth year is: {}'.format(int(df['Birth Year'].max())))
        print('The most common birth year is: {}'.format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (round((time.time() - start_time), 2)))
    print('-'*40)

def display_data(df):
    answer = input(
        "would you like to see 5 rows of data? enter yes or no ").lower()
    start_row = 0
    while answer == "yes":
        print(df.iloc[start_row:start_row+5])
        start_row += 5
        answer = input(
            "would you like to see more 5 rows of data? enter yes or no ").lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":

	main()
