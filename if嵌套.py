print("公司奖励")
age=int(input("请输入您的年龄："))
year=int(input("请输入您的工龄："))
level=int(input("请输入您的等级："))
if age>=18 and age<30:
    print("您年龄合格.")
    if year>2:
        print("工龄合格，可以领物品.")
    elif level>3:
        print("等级合格，可以领物品.")
    else: print("您工龄和等级都不合格")
else: print("您年龄不合格")