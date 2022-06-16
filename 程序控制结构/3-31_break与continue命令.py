# 从键盘输入一串字符，将其中的数宇部分去掉，输出处理后的字符串。

str = input("input:")

for i in str:
    if i.isdigit():
        continue
    print(i, end="")
