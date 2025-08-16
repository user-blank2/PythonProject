import datetime

Target_date=datetime.datetime(2006,7 ,12 ,5, 2, 12)
now=datetime.datetime.now()
print(Target_date)


if now<Target_date:
    print("You stil have time")
else:
    print("You messed up")