Hobbies={'跑步:','篮球:','跳绳:','羽毛球:'}
student={'李丽珊':('19960725','跑步'),'张晓明':('19170512','篮球'),'杨虎跃':('1990505','乒乓球')}


for i in Hobbies:
    print(i,end=":")
    flag=False
    for j in student:
        if i in student[j]:
            print("{},{}".format(j,student[j][0]),end='')
            flag=True



    if flag:
        print("无")
