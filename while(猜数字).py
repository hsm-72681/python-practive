import random
num = random.randint(1,100)
i=7
guess_num=int(input("请在7次内猜一个1到100的数字"))
while num!=guess_num:
    if guess_num>num:
        i -= 1
        guess_num=int(input(f"你猜大了，还有{i}次机会"))
    elif guess_num<num:
        i -= 1
        guess_num=int(input(f"你猜小了，还有{i}次机会"))
    if i==0:
        print(f"你没有机会了，正确答案是{num}")
        break
print(f"恭喜你猜对了，正确答案是{num},你用了{7-i}次机会")