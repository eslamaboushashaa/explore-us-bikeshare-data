import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
 
print('Hello! Let\'s explore some US bikeshare data!')
def get_filters():
    all_city  = ["chicago" , "new york" , "washington"]
    all_month = ["january" , "february" , "march" , "april" , "may" , "june" , "all" ]
    all_day   = ["Satarday", "Sunday", "Monday", "Tuesday" , "Wednesday" , "Thursday", "Friday", "All"]
    while True:
        city  = input("chooise the city  that want more information about it Chicago or New york and Washington ")
        if city.lower() in all_city: 
            print (" now, you will choise a month")
            break  
        else :
            print("--"*5)
            print ("please, enter avaliable city")
            print("--"*5)
    while True:        
        month = input("chooise the month that want more information about it ")
        if month.lower() in all_month:
            print (" now, you will choise a day ")
            break  
        else :
            print("--"*5)
            print ("please, enter avaliable month")
            print("--"*5)
    while True:     
        day   = input("chooise the day   that want more information about it ")  
        if day.title() in all_day: 
            print (" now, you finish the first step")
            break  
        else :
            print("--"*5)
            print ("please, enter avaliable day ")
            print("--"*5)
    return(city, month , day)    
def load_data(city, month, day):
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
    #convert the csv file to data frame to python can read it .
    df = pd.read_csv(CITY_DATA[city.lower()])
    # convert the date to date time because i can filtrate and analyis it.
    df["Start Time"] =pd.to_datetime(df["Start Time"])
    # i make the new colum and then add data month to analysis.
    df["month_data"]= df["Start Time"].dt.month
    # i make the new colum and then add data day to analysis.
    df["day_data"]= df["Start Time"].dt.day_name
    
    df["hour_data"] = df["Start Time"].dt.hour
    
    all_month = ["january" , "february" , "march" , "april" , "may" , "june" ]
    all_day   = ["Satarday", "Sunday", "Monday", "Tuesday" , "Wednesday" , "Thursday", "Friday"]
    
    if month !="all":
        # note a month which user input it is string but i delling with integer  
        # here i add 1 because the number in Python start 0
        month = all_month.index(month)+1
        
        df =df[month == df["month_data"]]
    
    if day != "all":
        
        day = all_day.index(day.title())+1
        
        df = df[day == df["day_data"]]
    return df
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    print(df["month_data"].mode())

    #display the most common day of week
    print(df["day_data"].mode())
          
    #display the most common start hour
    print(df["hour_data"].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('---------'*4)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    start_station=df["Start Station"].mode()
    
    print(start_station)
    #display most commonly used end station
    
    end_station = df["End Station"].mode() 
    print(end_station)
    # display most frequent combination of start station and end station trip
    df["trip"]= df["Start Station"] + "_" + df["End Station"]
    print(df["trip"].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total= df["Trip Duration"].sum()
    print(total)
    # display mean travel time
    avrage = df["Trip Duration"].mean()
    print(avrage)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    #Displays statistics on bikeshare users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
       # value_count can calulcate number the male and number the female 
       # value_count looking redundancy of the element  
    user_type = df["User Type"].value_counts()
    print(user_type)
    # Display earliest, most recent, and most common year of birth
    # Display counts of gender
    # note gender and bith day not find in washington
    if city != "washington":
       #user_gender = df["Gender"].value_counts()
       #print(user_gender)
       #the earliest is mean minmam value  
       earliest = df["Birth Year"].min()
       print(earliest)
       #the most recent is mean maximam value 
       most_recent = df["Birth Year"].max()
       print (most_recent)
       #  most common year of birth
       most_common = df["Birth Year"].mode()
       print (most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data (city):
          
    while True:
        CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
        display_chooise = input(" if you want display 5 raw data , please enter yes or no .  ")
        if display_chooise.lower() == "yes":
            raw = pd.read_csv(CITY_DATA[city.lower()])
            i = 1 
            e = 6
            print(raw.iloc[i:e,:])
            while True:
                add_raw = input("if you want add 5 raw enter yes ")
                if add_raw =="yes": 
                    print (raw.iloc[i+5:e+5,:])
                else :
                    break
            break
        else :
            print("thank\'s for you")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data (city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()