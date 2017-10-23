#!/usr/bin/python
import datetime,time

username = " \n \t elBert einstein  \n    "
message1 = "{} once said,'A person who never made a mistake " \
           "never tried anything new.'".format(' '
            .join([i.capitalize() for i in username.rstrip().lstrip().split()]))
message2 = "{} once said,'A person who never made a mistake " \
           "never tried anything new.'".format(username.lstrip().rstrip().title())
print(message1)
# Elbert Einstein once said,'A person who never made a mistake never tried anything new.'
print(message2)
# Elbert Einstein once said,'A person who never made a mistake never tried anything new.'

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
friend_foods = my_foods[:]
friend_foods.append('pear')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

#元祖
restaurant_foods = ('noodle','pizza')
print(restaurant_foods)
restaurant_foods = ('rice','pizza')
print("Modified foods:")
print(restaurant_foods)

#if
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#游乐场价格
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is ${}.".format(price))
#顾客要求配料
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperonis','pineapples','extra cheese']
requested_toppings = ['mushrooms','extra cheese','green peppers','french fries']
if 'mushrooms' in requested_toppings:
    print('Ading mushrooms!')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni!')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese!')
print('Finished making your pizza!')
if requested_toppings :
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('Sorry,we are out of green peppers right now!')
        elif requested_topping in available_toppings:
            print('Adding {}!'.format(requested_topping))
        else:
            print("Sorry,we don't have {}.".format(requested_topping))
    print('Finished making your pizza!')
else:
    print('Are you sure you want a plain pizza!')

#alien外星人
alien_color = ['green','yellow','red']
died_aliens = ['green','red','yellow']
for died_alien in died_aliens:
    if died_alien == 'green':
        print('{}:恭喜你获得了5个点！'.format(died_alien.title()))
    elif died_alien == 'yellow':
        print("{}:恭喜你获得了10个点！".format(died_alien.title()))
    elif died_alien == 'red':
        print("{}:恭喜你获得了15个点！".format(died_alien.title()))
# if died_alien1 == 'green':
#     print('恭喜你获得了5个点！')
# died_alien2 = 'red'
# if died_alien2 == 'green':
#     print('恭喜你获得了5个点！')

#用户
login_users = ['lisa','david','admin','sophia','queena']
if login_users:
    for login_user in login_users:
        if login_user.lower() == 'admin':
            print("Hello {},would you like to see a status report?".format(
                login_user))
        else:
            print("Hello {},thank you for logging in again.".format(
                login_user.title()))
else:
    print('We need to find some users!')

current_users = ['lisa','queena','lily','lucy','jack']
new_users = ['lily','david','queena','sophia','tang']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("此用户名{}已经被使用！".format(new_user))
    else:
        print("此用户名{}未被使用！".format(new_user))

#序数
ordinals = range(1,10)
for ordinal in ordinals:
    if ordinal == 1:
        print('{}st'.format(ordinal))
    elif ordinal == 2:
        print('{}nd'.format(ordinal))
    elif ordinal == 3:
        print('{}rd'.format(ordinal))
    else:
        print('{}th'.format(ordinal))

#字典
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
def get_x_increment(x_speed):
    if x_speed == 'slow':
        x_increment = 1
    elif x_speed == 'medium':
        x_increment = 2
    else:
        x_increment = 3
    return x_increment
alien_0['speed'] = 'medium'
alien_0['x_position'] += get_x_increment(alien_0['speed'])
print(alien_0)
alien_0['speed'] = 'fast'
alien_0['x_position'] += get_x_increment(alien_0['speed'])
print(alien_0)

polls = {
    'ervin':['python','c'],
    'david':['c'],
    'lucy' : ['ruby','go'],
    'lisa' : ['java','php'],
    'queena' : ['python'],
}
friends = ['david','lisa','ervin']
for poll_key in sorted(polls.keys()):
    if poll_key.lower() in friends:
        if len(polls[poll_key]) > 1:
            print('Hi {},I see your favorite languages are:'
                  .format(poll_key.title()))
            for language in polls[poll_key]:
                print(language.title())
        elif len(polls[poll_key]) == 1:
            print("Hi {},I see your favorite language is {}."
                  .format(poll_key.title(),polls[poll_key][0].title()))
print("以下是每位调查者的回答。")
for language in polls.values():
    print(language)

#嵌套
alien_1 = {'color':'green','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#初始化创建多个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color':'red','points':15,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['points'] = 5
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
print('...')
print("共创建了{}个外星人.".format(len(aliens)))

#存储客户点的披萨
pizza = {
    'crust':'thick',
    'topping':['mushrooms','green peppers','extra cheese'],
}
print("You ordered a {}-crust pizza with the following toppings:".format(pizza['crust']))
for topping in set(pizza['topping']):
    print(topping)

#input
prompt = 'hello'
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)