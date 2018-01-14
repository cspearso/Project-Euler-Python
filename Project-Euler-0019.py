#python has very useful date time data for this
import datetime
year = 1900
month = 1
day = 1
#using this we can have info a specific day
#we have the date, and the weekday; 0 corresponds to monday, 6 corresponds to sunday
date_0 = datetime.date(year,month,day)
day_0 = date_0.weekday()
#we can just loop over the years, checking the first of every month if it is a sunday
#for fun we can store the dates when they occur too
dates = []
for year in range(1901,2001):
    for month in range(1,13):
        if datetime.date(year,month,1).weekday() == 6:
            dates.append([year,month])

print (len(dates))
#expected value:171    