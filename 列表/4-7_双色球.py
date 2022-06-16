from random import randint


mynum = []
lotterynum = []
blackok = 0
whiteok = False
prizerank = ""

x = 0
while(x < 4):
    num = randint(1, 10)
    if num not in mynum:
        mynum.append(num)
        x += 1
mynum.sort()
num = randint(1, 5)
mynum.append(num)

x = 0
while(x < 4):
    num = randint(1, 10)
    if num not in lotterynum:
        lotterynum. append(num)
        x += 1
num = randint(1, 5)
lotterynum.append(num)

blacklotterynum = lotterynum[0:4]
for i in range(len(mynum) - 1):
    x = mynum[i]
    if x in blacklotterynum:
        blackok += 1
if mynum[-1] == lotterynum[-1]:
    whiteok = True

if (blackok == 4 and whiteok):
    prizerank = "一等奖"
elif (blackok == 4):
    prizerank = "二等奖"
elif (blackok == 3 and whiteok):
    prizerank = "三等奖"
elif (blackok == 3):
    prizerank = "四等奖"
elif (blackok == 2 and whiteok == False):
    prizerank = "五等奖"
elif (blackok == 2):
    prizerank = "六等奖"
else:
    prizerank = "未中奖"

print("此次开出的中奖号码为：")
print("\t黑色球:", end="")

for i in range(len(blacklotterynum)):
    print(blacklotterynum[i], end=" ")
print("，白色球：{}".format(lotterynum[-1]))
print("你机选投注号码为：")
print("\t黑色球：", end="")
for i in range(len(mynum) - 1):
    print(mynum[i], end=" ")
print("，白色球:{}".format(mynum[-1]))
if (prizerank == "未中奖"):
    print("很遗憶，你没有中奖，继续努力！")
else:
    print("恭喜你，中奖等级为{}，请及时记奖！".format(prizerank))
