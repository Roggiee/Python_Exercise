ls0 = []
ls1 = [90, 93, 85, 96]
ls3 = [["李明", 93, 85, 96], ["王军", 83, 95, 91]]

ls2 = [90, 93, 85, 96]
a = ls2[0]
b = ls2[1]
C = ls2[-1]
d = ls2[-2]
sum = ls2[0] + ls2[1] + ls2[2]
sumtotal1 = 0
for x in ls2:
    sumtotal1 += x
sumtotal2 = 0
for i in range(len(ls2)-1):
    sumtotal2 += ls2[i]
ls2 = [90, 93, 85, 96]
ls2[1] = 95
ls2.append(88)

ls2 = [190, 93, 85, 96]
x = 95 in ls2
y = 95 not in ls2
ls2 = [90, 93, 85, 96]
ls2.sort()
ls2.sort(reverse=True)
ls2 = [90, 93, 85, 96, 97, 91, 92]
ls3 = ls2[1: 4]
