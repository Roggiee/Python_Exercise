def gusers(names):
    '''向列表中的每位用户都发出简单的问候'''
    for name in names:
        msg="你好,"+name.title()+",欢迎光临！"
        print(msg)
username=['小燕','昭文','梓桓','宏泰','文龙','林江']
gusers(username)



