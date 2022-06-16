# 已知3个孩子的年龄均不超过18岁，其年龄乘积是36，其和是偶数，请推算这3个孩子的年龄？
# （1）完全遍历：3层循环
# (2） 优化：设3个孩子的年龄由小到大，可缩短遍历范围？

for kid1 in range(0, 19):
    for kid2 in range(kid1, 19):
        for kid3 in range(kid2, 19):
            if(kid1 * kid2 * kid3 == 36 and (kid1 + kid2 + kid3) % 2 == 0):
                print(kid1, kid2, kid3)
