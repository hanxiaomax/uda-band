import time
import pandas as pd
import numpy as np

# 定义全局变量
# 1.全局变量可以被本文件里面的所有函数访问
# 2.在这里我们定义一些常量
# 3.变量名大写是一种风格

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITYS =  ["chicago","new york city","washington" ]
MONTH = ["january","february","march","april","may","june","july","august","september","october","november","december",'all']
DAYSOFWEEK = ["monday" ,"tuesday" ,"wednesday", "thursday", "friday" ,"saturday" ,"sunday",'all']


############################################
#   函数定义
#   阅读代码最好从 main 函数开始，请跳到最下方先看 main
############################################


# 过滤函数
# 它的作用是获取用户输入，并返回过滤条件，city, month, day
# 函数的可以看做是一个黑盒，通过参数输入，通过返回值输出，具体请参考：
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city , month ,day = None,None,None # 初始化变量
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city = input('please in put city:')
    city = input('Enter a city name: ')
    while city not in CITYS :
        city = input('Enter a city name: ')
        print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    # 通过 lower 函数将用户的输入转换为小写
    # 转换成小写是因为 MONTH 里面的元素全部为小写
    month = input('Enter a month name: ').lower() 
    while month not in MONTH :  #如果输入的不是 MONTH 中的月份则不合法，重新输入
        month = input('Enter a month name: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter a day name: ').lower()
    while day not in DAYSOFWEEK:
        day = input('Enter a day name: ').lower()

    print('-'*40)
    return city, month, day

# 这个函数的功能是根据用户输入的过滤条件，从 dataframe 中过滤数据，得到新的 dataframe
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
    print(city,month,day) # 打印一下输入，用于调试，确认输入是否和我们输入的一致，包括大小写
    # load data file into a dataframe
    # CITY_DATA = { 'chicago': 'chicago.csv',
    #           'new york city': 'new_york_city.csv',
    #           'washington': 'washington.csv' }
    df = pd.read_csv(CITY_DATA[city]) # 加载城市对应的 csv 文件
    
    
    # convert the Start Time column to datetime
    # 转换原 csv 文件中的时间格式
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # MONTH 存的是月份的名字，而 df 中存的是月份的数字
         #index 函数可以通过元素获取元素的索引，索引从0开始，而月份从1开始，所以需要+1
        month = MONTH.index(month) + 1
        print(month)
        print(df['month'].unique())
        # filter by month to create the new dataframe
        df = df[df['month'] == month] #根据月份过滤

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day] #根据日过滤

    return df #返回已经过滤过的 df


# 这个函数的功能是打印时间相关的数据信息
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    print("\nThe most common month is {0}".format(MONTH[df['month'].mode()[0]-1]))

    # TO DO: display the most common day of week
    print("\nThe most common day of week is {0}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("\nThe most common start hour {0}".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# 这个函数的功能是打印站点相关的数据信息
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most common start station {0}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("\nThe most common end station {0}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# 这个函数的功能是打印行程相关的数据信息
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time    
    print("\nThe total travel time {0}".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("\nThe mean travel time {0}".format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# 这个函数的功能是打印用户相关的数据信息
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nThe  counts of user types:\n{0}".format(df["User Type"].value_counts()))

    # TO DO: Display counts of gender
    print("\nThe counts of gender:\n{0}".format(df["Gender"].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nThe most earliest year of birth {0}".format(df["Birth Year"].min()))
    print("\nThe most recent year of birth {0}".format(df["Birth Year"].max()))
    print("\nThe most common year of birth {0}".format(df["Birth Year"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """
    # 程序处理流程
        # 用户输入  --> 校验用户输入 --->获取过滤条件 --> 加载数据 ---> 
         ---> 输出结果
                            -- 时间数据
                            -- 站点数据
                            -- 行程数据
                            -- 用户数据
    """
    while True: # 死循环，让程序一直执行
        city, month, day = get_filters() # 获取用户的输入（过滤条件）

        df = load_data(city, month, day) # 更具用户输入的过滤条件，加载数据
        
        # 如果过滤之后的 df 为空，则重新开始
        if df.empty :
            print("based on the filter, the data is empty.")
        else:
            time_stats(df) # 时间数据
            station_stats(df) #站点数据
            trip_duration_stats(df) #行程数据
            user_stats(df)#用户数据
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes': # 死循环终止条件，用户不输入 yes，则程序停止
            break


# 整个程序的入口，当程序作为脚本执行时，__name__ == "__main__"，if 为真，调用 main 函数
if __name__ == "__main__":
	main()
