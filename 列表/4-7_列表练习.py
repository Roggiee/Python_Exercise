from random import randint
from turtle import position


list1 = ['pvthon 3', '软件技术', 2019, 95]
list2 = [93]
list2.append("kevin")
list2.insert(1, 'lewis')
list1.extend(list2)

list1 = ['python 3', 95, '软件技术', 2019, 95, 96, 95]
list1.remove(95)

x = list1.pop()
x = list1.pop(-2)
del list1[0]
del list1

ls2 = [90, 93, 85, 96]
ls2.reverse()

ls1 = [11, 2, 3, 4, 5, 6]
ls2 = ls1[:]
ls2 = ls1[1 - 1: 1]
ls2 = ls1[:3]
ls2 = ls1[0: -1: 3]
ls2 = ls1[:: -1]
ls2 = ls1[4: 1: -1]

list1 = [34, 67, 98, 88, 78, 99, 21, 39]
x = len(list1)
maxlist = max(list1)
minilist = min(list1)

list1 = [34, 67, 98, 88, 78, 99, 21, 39]
counts = list1.count(88)
position = list1.index(88)

x = randint(0, 100)
x = randint(60, 99)
