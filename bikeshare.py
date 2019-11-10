import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all','january','february','march','april','may','june']
DAYS = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def main():
    city, month, day = '', '', ''
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('\nSelect a city:\nChicago\nNew York City\nWashington\n\nYour selection: ').lower()
        if city in list(CITY_DATA.keys()): break
        else: print('\nPlease try again!\n')
    while True:
        month = input('\nSelect a month:\nAll\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\n\nYour selection: ').lower()
        if month in MONTHS: break
        else: print('\nPlease try again!\n')
    while True:
        day = input('\nSelect a day:\nAll\nSunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\n\nYour selection: ').lower()
        if day in DAYS: break
        else: print('\nPlease try again!\n')
    print('-'*40)
    df = pd.read_csv(CITY_DATA[city], index_col=0)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of week'] = df['Start Time'].dt.weekday_name
    if month != 'all': df = df[df['Month'] == MONTHS.index(month)]
    if day != 'all': df = df[df['Day of week'] == day.title()]
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('Most common month:\n', MONTHS[df['Month'].mode()[0]].title())
    print('\nMost common day of week:\n', df['Day of week'].mode()[0])
    df['Hour'] = df['Start Time'].dt.hour
    print('\nMost common start hour:\n', int(df['Hour'].mode()[0]) % 12, ['AM', 'PM'][int(df['Hour'].mode()[0]) >= 12])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('Most commonly used start station:\n', df['Start Station'].mode()[0])
    print('\nMost commonly used end station:\n', df['End Station'].mode()[0])
    df['From To'] = df['Start Station'].str.cat(df['End Station'],sep=' to ')
    print('\nMost frequent combination of start to end trip:\n', df['From To'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:\n',
          '{:,}'.format(round(total_travel_time, 2)), 'seconds or,\n',
          '{:,}'.format(round(total_travel_time / 60, 2)), 'minutes or,\n',
          '{:,}'.format(round(total_travel_time / 3600, 2)), 'hours or,\n',
          '{:,}'.format(round(total_travel_time / 86400, 2)), 'days.\n')
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:\n',
          '{:,}'.format(round(mean_travel_time, 2)), 'seconds or,\n',
          '{:,}'.format(round(mean_travel_time / 60, 2)), 'minutes or,\n',
          '{:,}'.format(round(mean_travel_time / 3600, 2)), 'hours.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print('User types:\n')
    for user, count in user_types.items():
        print('{:<13s}{:>7d}'.format(user, count))
    print('\nGender count:\n')
    try:
        gender = df['Gender'].value_counts()
        for user, count in gender.items():
            print('{:<13s}{:>7d}'.format(user, count))
    except:
        print('The city you selected does not have Gender data.')
    print('\nYear of birth stats:\n')
    try:
        print('Earliest year of birth:\n', df['Birth Year'].min())
        print('\nMost recent year of birth:\n', df['Birth Year'].max())
        print('\nMost common year of birth:\n', df['Birth Year'].mode()[0])
    except:
        print('The city you selected does not have Birth Year data.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    for i in range(0, df.shape[0], 5):
        print("\nI can show you 5 lines of raw data at a time if you like.")
        if input("Type 'yes' to continue: ") != 'yes': break
        else: print(df.iloc[i: i + 5])

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'yes': main()
if __name__ == "__main__":
    main()