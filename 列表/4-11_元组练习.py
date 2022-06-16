# 0 to 10 English words tuple
x = ('zroe', 'one', 'two', 'three', 'four', 'five',
     'six', 'seven', 'eight', 'nine', 'ten')
# wordList
wordList = []
# input int
num = int(input("Enter a number: "))
temp = num

for item in range(len(str(num))):
    # 求个位数
    n = temp % 10
    wordList.append(x[int(n)])
    temp = temp / 10
    wordList.reverse()

print("{} is {}". format(num, ' '.join(wordList)))
