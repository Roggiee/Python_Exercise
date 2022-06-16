import math

for item in range(100, 1000):
    if math.pow(int(item % 10), 3)+math.pow(int(item % 100 / 10), 3)+math.pow(int(item / 100), 3) == item:
        print(item)
