# 购买0只公鸡，25只母鸡，75只小鸡正好100钱
# 购买4只公鸡，18只母鸡，78只小鸡正好100钱
# 购买8只公鸡，11只母鸡，81只小鸡正好100钱
# 购买12只公鸡，4只母鸡，84只小鸡正好100钱
for gong in range(20 + 1):
    for mu in range(33 + 1 - gong):
        xiao = 100-gong-mu

        if gong * 5+mu*3+xiao/3 == 100 and gong + mu + xiao == 100:
            print("公鸡：{}，母鸡：{}，小鸡：{}". format(gong, mu, xiao))
