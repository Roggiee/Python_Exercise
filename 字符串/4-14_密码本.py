# 初始化密码本
code_book = '''    我和莫绍谦手拉着手回到了老房子，我们已经像最平凡的恋人一
样手拉着手，一点也不会感到别扭，心里充满了快乐。
    转头看见莫绍谦好笑地看着我，眼睛里都是宠溺。
    他带我去了阁楼，那间阁楼我从未进去过，搬来的第一天，我便
看到了那上面红色的大锁。结果莫绍谦连钥匙都没用就打开了锁，他
举着那把锁对我说：“如果你多点好奇心，你早就会发现，我也会暴
出更多秘密。”
    阁楼古老陈旧，木质的地板散发着琥珀色的沉香。莫绍谦移出角
落里的一个纸箱，我好奇地凑上去。   我打开一本相册，看到了童
年的莫绍谦。他的脸白白净净，发型古怪，还露出缺了大门牙的牙齿。
我笑得肚子疼，笑得流眼泪了。
'''
code = "0022,0529, 0920, 0121, 0204, 0729"
information = ''
list = code_book.split("\n")
i = 0
for item in list:
    print("密码本第1行是:<{}>".format(i, item))
    i += 1

code_list = code.split(", ")
for item_c in code_list:
    row = int(item_c[0:2])
    column = int(item_c[2:])

information += list[row][column]
print("最终情报是：{}".format(information))
