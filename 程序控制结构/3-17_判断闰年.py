year = int(input("input year:"))

if (year % 400 == 0):
    print("%s是闰年" % year)
else:
    print("%s不是闰年" % year)
