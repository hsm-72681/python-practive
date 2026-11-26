money=10000
for people in range(1,21):
    j=int(input("请告知绩点"))
    if(j<5):
        print(f"{people}号员工绩点不足，不发")
        continue
    else:
        print(f"{people}号员工绩点达标，发放1000元。")
        money-=1000
    if(money==0):
        print("没钱了")
        break