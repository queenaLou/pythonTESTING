#!/usr/bin/python
import datetime,time

username = " \n \t elBert einstein  \n    "
message1 = "{} once said,'A person who never made a mistake never tried anything new.'".format(' '.join([i.capitalize() for i in username.rstrip().lstrip().split()]))
message2 = "{} once said,'A person who never made a mistake never tried anything new.'".format(username.lstrip().rstrip().title())
print(message1) # Elbert Einstein once said,'A person who never made a mistake never tried anything new.'
print(message2) # Elbert Einstein once said,'A person who never made a mistake never tried anything new.'

# print(username.title())

names = ['queena','lily','cristin']
public_hello = "{},glad to see U!"
for name in names:
    print(public_hello.format(name.title()))

#邀请晚餐练习
want_dinner_names = ['queena','lily','jack']
message = '我想邀请3个人吃晚饭:'
for i in want_dinner_names:
    print("{}你好，我想请你今晚来吃饭".format(i.title()))

print('然后我在网上订了一个超大的餐桌，可以再多邀请三个人了')
want_dinner_names.insert(0,'lucy')
want_dinner_names.insert(2,'kevin')
want_dinner_names.append('lisa')

message_6 = '我想邀请6个人吃晚饭:'
for i in want_dinner_names:
    print("{}你好，我想请你今晚来吃饭".format(i.title()))

print("但今天淘宝店主突然告诉我不能如期将餐桌发货，所以我只能邀请两个人来吃饭了")
init_len = len(want_dinner_names)
for i in range(init_len - 2):
    delete_name = want_dinner_names.pop()
    print("很抱歉不能邀请{}你来吃饭了".format(delete_name.title()))

for i in want_dinner_names:
    print("{}你好，请今晚准时来吃饭哦~".format(i.title()))
print('我一共邀请了{}个人来吃晚饭'.format(len(want_dinner_names)))
del want_dinner_names[1]
del want_dinner_names[0]
print(want_dinner_names)
print('Look,names are empty.')

#旅游地方练习
# want_travel = ['sanya','dalian','jiuzhaigou','lasa','wulumuqi']
want_travel = ['三亚','大连','九寨沟','拉萨','乌鲁木齐']
print(want_travel)
print(sorted(want_travel))
print(sorted(want_travel,reverse=True))
print(want_travel)
print('用sorted不会改变原列表，以下方法会改变，如reverse和sort')
want_travel.reverse()
print(want_travel)
want_travel.reverse()
print(want_travel)
want_travel.sort()
print(want_travel)
want_travel.sort(reverse=True)
print(want_travel)

#披萨
pizzas = ['榴莲','蓝莓','培根']
for pizza in pizzas:
    print('我喜欢{}披萨.'.format(pizza))
print('我真的很喜欢披萨!')

#宠物
pets = ['猫','狗','兔子']
for pet in pets:
    print('{}会是一个很好的宠物！'.format(pet))
print('这些动物都将会是很好的宠物！')

for i in range(5):
    print(i)
print(list(range(1,5,3)))
numbers = [1,2,4,6,7,9]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#循环
for i in range(1,21):
    print('当前数字：%d' % i)
to1baiwan = []
for i in range(1,1000001):
    to1baiwan.append(i)
# for i in to1baiwan:
#     print('当前数字：%d' % i)
print('此列表最小数值为：%d' % min(to1baiwan))
print('此列表最大数值为：%d' % max(to1baiwan))
starttime = datetime.datetime.now()
ss = time.time()
print(starttime)
print('此列表所有项的和为：%d' % sum(to1baiwan))
endtime = datetime.datetime.now()
ee = time.time()
print(endtime)
print((endtime - starttime).seconds)
print(ee - ss)

number_odd = range(1,20,2)
for odd in number_odd:
    print("奇数：%d" % odd)

number_3 = [i for i in range(1,31) if i % 3 == 0]
for i in number_3:
    print("能被3整除的数：%d" % i)

number_cube = [i ** 3 for i in range(1,11)]
for i in number_cube:
    print("前10的立方：%d" % i)

#坑
a = [1,2,3,4,5]
b = a[1:3].append(666)
print(a) #[1,2,3,4,5]
print(b) #None
a = [1,2,3,4,5]
a[1:3] = [666]
print(a) #[1,666,4,5]

#切片
my_foods = ['pizza','noodle','rice','photo','corn']

#多谢俩字