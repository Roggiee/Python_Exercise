from email import message


stro = ''
strl = input("请输入姓名：")
str3 = "Hello Mike!"
name = 'Mike'
x = len(name)
first_name = 'Mike'
last_name = 'Smith'
full_name = first_name + '' + last_name
print(full_name)
print("He11o," + full_name + "!")
print(full_name + 666)
print("重要的事情说三遍" * 3)

badminton_star = 'Dan Lin'
print('L' in badminton_star)
print('Dan' in badminton_star)
print('lin' in badminton_star)
print('xie' in badminton_star)

message = 'welcome to shenzhen'
char1 = message[0]
char_last = message[-1]
for char in message:
    print(char)

wish = 'healthy,happy'
print(wish[::])
print(wish[:])
print(wish[0:len(wish):1])
print(wish[0:7])
print(wish[-6:-1])
