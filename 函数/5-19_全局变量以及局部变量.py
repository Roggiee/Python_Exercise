def func(a,b):
    n=a+b
n=1
func(3,4)
print("n={}".format(n))


def func(a,b):
    global n
    n=a+b
n=1
func(3,4)
print("n={}".format(n))