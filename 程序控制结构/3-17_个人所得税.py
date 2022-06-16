a = int(input("input your money (w):")) - 6

if (a < 0):
    print("not")
elif(a <= 3.6):
    print("rel:{}".format(a*0.03))
elif(a <= 14.4):
    print("rel:{}".format(a*0.1))
elif(a <= 30):
    print("rel:{}".format(a*0.2))
elif(a <= 42):
    print("rel:{}".format(a*0.25))
elif(a <= 66):
    print("rel:{}".format(a*0.3))
elif(a <= 96):
    print("rel:{}".format(a*0.35))
else:
    print("rel:{}".format(a*0.45))
