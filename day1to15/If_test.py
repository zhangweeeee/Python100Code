username  = input("输入姓名:")
passwd = input("输入密码:")

if username == "admin" and passwd == "123456":
    print("Access")
else:
    print("Wrong password")