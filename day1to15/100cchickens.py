"""
《百钱百鸡》问题
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
for x in range(0,20):
    for y in range(0,33):
        if x*5+y*3+(100-x-y)/3 == 100:
            print("公鸡 = %d , 母鸡 = %d , 小鸡 = %d" % (x,y,100-x-y))