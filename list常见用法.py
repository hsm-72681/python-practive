a=[10,20,30,40,50]
#创建列表
b=[]
#创建空列表
c=list(range(5))
#0--4的列表
d=[0]*3
#[0,0,0]
e=[1,"张三",3.14,True]
#可混放不同类型
print(a[0])
#取下标，从0开始，输出10
print(a[-1])
#负下表从末尾数，输出50，等同于a[4]
print(len(a))
#输出元素个数，5
print(30 in a)
#判断是否存在，输出True
print(a[1:3])
#切片左闭右开，输出第2，3个数，为20，30
print(a[:3])
#输出从头到a[2],为10，20，30
print(a[2:])
#输出从a[2]到末尾，为30，40，50
print(a[::2])
#从头开始，步长为2，输出10，30，50
a.append(60)
#末尾追加一个元素为60
a.insert(0,5)
#在下标0出插入一个元素5
a.extend([70,80])
#把另一个列表并入本列表，默认按序加到后面
a[0]=99
#修改列表某个元素
a[1:3]=[7,8]
#修改一段元素
a.remove(30)
#删除第一个值为30的，不存在会报错，直接删除其元素位置
x=a.pop()
#删除并返回最后一个元素
y=a.pop(0)
#删除并返回下标为一的元素
del a[1]
#按下标清除
a.clear()
#清除列表，变为空列表
a=[10,20,30,40,50]
#重新创建列表
for x in a:
    print(x)
#遍历列表
for i,x in enumerate(a):
    print(i,x)
#同时拿到下标和值，下标从0开始
for i,x in enumerate(a,1):
    print(i,x)
#同时拿到下标和值，下标从1开始
for x in reversed(a):
    print(x)
#倒序遍历
a.sort()
#原地升序排列，返回None
a.sort(reverse=True)
#原地降序排列
b=sorted(a)
#返回升序之后的列表，原列表不变
a.reverse()
#原地反转元素顺序
print(min(a),max(a),sum(a))
#输出列表最大值，最小值，和
print(a.count(30))
#统计30出现的次数
print(a.index(30))
#返回30首次出现的下标，找不到会报错
sq=[x*x for x in range(5)]
#输出0，1，4，9，16
ev=[x for x in range(10) if x%2==0]
#条件推导式，输出偶数
b=a.copy()
#创建一个内容相同的新列表