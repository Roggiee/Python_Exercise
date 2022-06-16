price = 1
while (price != 0):
    price = input("请输入一个数")
    amount = input("请输入一个数")
    money = amount+price

if (money <= 1000):
    cash1 = money*0.92
elif(money <= 3000):
    cash1 = money*0.85
elif (money <= 5000):
    cash1 = money*0.78
else:
    cashl = money*0.7

if (money >= 2000):
    cash2 = (money-2000)*0.7+2000
else:
    money = price
    cash3 = money-int(money/500)*70

if (cash1 < cash2):
    if (cash1 < cash3):
        print("请选择天虹")
    else:
        print("请选择大力发")
else:
    if(cash2 < cash3):
        print("请选择友谊天地")
    else:
        print("请选择大力发商城")
