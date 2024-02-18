#III. a Python program to extract year, month, date and time using Lambda. 
from datetime import datetime
today_date_time=datetime.now()
#print(today_date_time)
year = today_date_time.year
month = today_date_time.month
day = today_date_time.day
hr = today_date_time.hour
min = today_date_time.minute
sec = today_date_time.second
print("The date is:",day,"/",month,"/",year)
print("The time is:",hr,":",min,":",sec)