import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ("all", "january", "february", "march", "april", "may", "june")
DAYS = ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

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
        city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Select a month from {}, {}, {}, {}, {}, {} or {}:".format(*MONTHS)).strip().lower()
        if month in MONTHS:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Select a day from {}, {}, {}, {}, {}, {}, {} or {}:".format(*DAYS)).strip().lower()
        if day in DAYS:
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

    # add two columns of month and day to filter
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
        df = df[df['month'] == (MONTHS.index(month) + 1)]

    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}.'.format(MONTHS[most_common_month].title()))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is {}.'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is {}.'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}".format(most_common_start))

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print("The most commonly used end station is {}".format(most_common_end))

    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'].astype(str) + " -> " + df['End Station'].astype(str)
    most_combination = combination.mode()[0]
    print("The most frequent combination of start station and end station trip is {}".format(most_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totoal_time = df['Trip Duration'].sum()
    print("The total traval time is {} seconds".format(totoal_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean traval time is {} seconds".format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type:")
    print(user_types)
    print()

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print("Gender:")
        print(genders)
        print()
    except KeyError:
        print("There isn't a [Gender] column in this spreedsheet!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("The oldest user is borned in {}. The youngest is borned in {}. People borned in {} uses this service most".format(earliest, most_recent, most_common))
    except KeyError:
        print("There isn't a [Birth Year] column in this spreedsheet!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
