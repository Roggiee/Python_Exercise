city = "Beijing"
print(len(city))
# 把教宇转换为宇符串
print("pi is "+str(3.1415))
# 输出 Unicode 码为10005 对应的字符
print("10005 对应的字符是：" + chr(10005))
# 输出26个英文字母的 Unicode 编码
for char in "abcdefghijklmnoparstuvwxyz":
    print("{}的 Unicode 编码是:{} \n".format(char, ord(char)))
# 榆出菜个整数对应的十六进制和八进制数的小写形式字符串
    n = 10000
print("{}的十六进制是{},八进制是{}.".format(n, hex(n), oct(n)))

# 使用center0方法让maytthon”在宽度为20的区城居中显示。两侧医城塘点。基
print("Python".center(20, "4"))
# 使用 find()方法在宇待串。的查找子串”"第一次出現的位量
S = "Hello, world!"
print(S.find("o"))
# 使用tind0方法在宇村串。的素引为5的位置开始查我手串“”"第一浓地
print(S.find('o'))
# 使用join()方法把列表中各元素用退号分隔并组成新宇行串。榆出此新子
course_list = ["语文", "数学", "物理", "化学"]
print("&".join(course_list))
# 使用 split(方法特一个以退号分隔的手行事桥成一个序列
print("北京，上海, 广州, 深期".split(","))
print("c:\\user\\administrator".split("\\"))
print(" I will come back soon".split())
print("I 11ke dancing. ".replace("'dancing", "g16g45gmy"))
