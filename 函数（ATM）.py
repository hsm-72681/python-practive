
print("1:查询余额")
print("2：存款")
print("3:取款")
print("4:退出")
money =50000
def a(money):
    print(f"您的余额为{money}")

def b(add):
    global money
    money+=add
    

def c(de):
     global money
     money_=de
while True:
    n=int(input("请选择服务"))
    match n:
        case 1:
            a(money)
        case 2:
            b(int(input("您要存多少钱")))
            a(money)
        case 3:
            c(int(input("您要取多少钱")))
            a(money)
        case 4:
            a(money)
            print("再见")
            break
