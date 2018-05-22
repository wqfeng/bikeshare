import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
                      month filter
        (str) day - name of the day of week to filter by, or "all" to apply
                    no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        sm = ("Would you like to see data for {}, {}, or {}?"
             .format(*CITY_DATA.keys()))
        city = input(sm).title()
        if city in CITY_DATA.keys():
            break

    # get user input for month (all, january, february, ... , june)
    mon_list = ["All", "January", "February", "March", "April", "May", "June"]
    while True:
        sm = "Which month - {}, {}, {}, {}, {}, {}, or {}?".format(*mon_list)
        month = input(sm).title()
        if month in mon_list:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                 "Saturday", "Sunday"]
    while True:
        sm = "Which day - {}, {}, {}, {}, {}, {}, {}, or {}?".format(*days_list)
        day = input(sm).title()
        if day in days_list:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if
    applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
                      month filter
        (str) day - name of the day of week to filter by, or "all" to apply
                    no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_num]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('the most common month: ', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of week: ', popular_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station: ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('most commonly used end station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    trip_series = df['Start Station'].astype(str) + " -> " + \
        df['End Station'].astype(str)

    popular_cmd_start_end = trip_series.mode()[0]

    print('most frequent combination of start station and end station trip: ',
          popular_cmd_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_tm = df['Trip Duration'].sum()
    print("total travel time: {} seconds.".format(total_travel_tm))

    # display mean travel time
    mean_travel_tm = df['Trip Duration'].mean()
    print("mean travel time: {} seconds.".format(mean_travel_tm))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_ct = df['User Type'].value_counts()
    print("counts of user types:\n" + str(user_type_ct))

    # Display counts of gender
    try:
        gender_ct = df['Gender'].value_counts()
        print("\ncounts of gender:\n" + str(gender_ct))
    except KeyError:
        print("\n[Warn]: There is no *Gender* column exist.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_y = df['Birth Year'].min()
        recent_y = df['Birth Year'].max()
        common_y = df['Birth Year'].mode()[0]
        print("\nearliest year: {}, most recent year: {}, most common year: {}".
              format(earliest_y, recent_y, common_y))
    except KeyError:
        print("\n[Warn]: There is no *Birth Year* column exist.")

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

