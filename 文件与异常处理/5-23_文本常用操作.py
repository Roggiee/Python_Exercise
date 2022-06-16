#文件的打开
f=open("D:/教学任务/21-22第二学期/myfile.txt","r")
f=open(r"D:\教学任务/21-22第二学期\myfile.txt","r")
f=open("D:\\教学任务\\21-22学期\\myfile.txt","r")



#文件读和写
f=open("mytest.txt",'w')
f.write("Hello World")
f.close()
#打开文件写入"Hello World"

f=open("myfile.txt")
print(f.read(5))
print(f.read())
f.close()
#将上述文件打开，先读取5个字符，在读取剩余字符

#with语句
#利用with语句打开文件，一次读入，分行打印
fn=input("请输入文件名:")
with open(fn,"r")as fo:
    for line in fo.readlines():
        print(line)

for line in fn:
    print(line)