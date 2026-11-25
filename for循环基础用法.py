for i in range(5):
    print(i)
#从0到4
for m in range(1,5):
    print(m)
#从1到4
for j in range(1,10,2):
    print(j)
#步长为二，输出1，3，5，7，9
for h in range(5,0,-1):
    print(h)
#从5到1，到着输出
for g in "Python":
    print(g)
#一个一个输出字符，一个字符一换行
for name in ["张三","李四","王五"]:
    print(name)
#遍历列表
for w in range(1,10):
    for q in range(1,w+1):
        print(f"{w}x{q}={w*q}\t",end='')
    print()
#for循环九九乘法表
for x in range(1,10):
    if x==5:
        break
    print(x)
#for循环里使用break
for x in range(1,10):
    if x==5:
        continue
    print(x)
#for循环里使用continue
for x in range(1,10):
    if x==15:
        break
    print(x)
else:print("未被打断")
#for else用法