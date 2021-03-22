import datetime

todayWithTime = datetime.datetime.today()
todayWithoutTime = datetime.date.today()

print(todayWithTime)
print(todayWithoutTime)
print("The current date is ", datetime.datetime.strftime(todayWithoutTime, "%m/%d/%Y"))
print("The current date is ", datetime.datetime.strftime(todayWithTime, "%H:%M:%S"))
