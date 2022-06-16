def cheng(n=9):
    if n>9 or n<1:
        n=9
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=1:
                print("{}*{}={}".format(i,j,i*j),end=" ")
        print()
cheng(5)
cheng(12)
cheng()