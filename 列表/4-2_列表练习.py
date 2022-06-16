list0 = [55, 78, 97, 98, 69, 70]
list2 = ['you', 'need', 'python']

list0.sort(reverse=True)
for item in list0:
    print(item)

list1 = []

for item in list0:
    if item % 2 == 1:
        list1.append(item)

numtotal = len(list1)

list2[2] = 'python3'

list3 = list0[3:5]

ls = []
inputer = 0
while inputer != -1:
    inputer = int(input(''))
    ls.append(inputer)

avg = 0
for item in ls:
    avg += item
avg = avg/len(ls)

ls.sort(reverse=True)
for item in ls:
    print(item)
