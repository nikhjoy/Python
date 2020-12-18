import datetime

now = datetime.datetime.now()

print(datetime.date.today())

print(datetime.date.today().month)

print(now.strftime("%d:%m:%Y"))

x = datetime.datetime(2020, 6, 12)

print(x)

y = datetime.datetime(2018,4,5)

dif = x-y
print(dif)

end = datetime.datetime.now()

difference = end-now

print(difference)
