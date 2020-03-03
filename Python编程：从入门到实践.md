# Python编程：从入门到实践

Python官方网站：

https://www.python.org/

Python官方下载链接：

https://www.python.org/downloads/

3.x文档链接：

https://docs.python.org/3/

## 1 起步

### 1.1 搭建环境

#### Python版本

当前笔者使用版本是3.7.4

#### Hello World

```python
print("Hello World!")
```

### 1.2 不同的操作系统

#### Linux

在命令行输入python并敲下回车即可判断是否安装python，如果版本是2.x的版本，输入python3来检测是否安装了python3.x的版本

#### OS X

pass

#### Windows

Win+R打开运行窗口，输入cmd敲下回车，在命令行输入python查看python是否安装以及其版本

关闭终端，可按Ctrl+Z按回车键，或者执行命令exit()

## 2 变量和简单数据类型

### 2.1 在命令行运行py文件

运行文件时发生了什么？

通过.py判断出来是python文件，使用Python解释器来运行它，解释器读取整个程序，确定每个单词的含义。

### 2.2 变量

```python
message = "Hello World"
print(message)
```

message就是一个变量

#### 2.2.1 变量的命名和使用

- 变量名只能包含字母、数字和下划线，变量名可以使用字母和下划线开头，但是不能使用数字打头。
- 变量名不能包含空格
- 不能将Python关键字和函数名用作变量名
- 变量名应该简短并且具备描述性
- 慎用小写字母l和大写的O，防止和数字10想混

#### 2.2.2 使用变量时避免命名错误

出现错误以及bug并不可怕，根据bug的信息去定位bug的位置，再去解决

### 2.3 字符串

字符串就是一系列字符。单引号双引号都行。

#### 2.3.1 修改字符串的大小写

```python
# 将字符串的首字母大写
name = "ada lovelace"
print(name.title())

# 将字符串全部改写为大写upper()或者小写lower()
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

#### 2.3.2 合并（拼接）字符串

Python使用加号（+）来合并字符串

```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
```

#### 2.3.3 使用制表符或换行符来添加空白

在编程中，空白泛指任何非打印字符，如空格、制表符（\t）、换行符（\n）。

#### 2.3.4 删除空白

在程序里，空白并不是表面意义上的空白，空白也是有其存在的位置的，通常使用开头lstrip()，末尾rstrip()，同时两端strip()方法去掉空白。l

```python
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
```

### 2.4 数字

#### 2.4.1 整数

整数常用的运算符

- +
- -
- *
- /
- **

#### 2.4.2 浮点数

带小数点的数字

#### 2.4.3 使用函数str()避免类型错误

字符串拼接或者数字运算时，需要保证前后的变量类型一致，不能出现整型(int)+字符串的情况，否则会报错

### 2.5 注释

#

## 3 列表

### 3.1 列表是什么

列表是由一系列按特定顺序排列的元素组成。用方括号[]来表示列表。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

#### 3.1.1 访问列表元素

列表是**有序**集合

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

#### 3.1.2 索引从0而不是1开始

列表中的第一个元素的位置是0

访问最后一个元素可以通过索引-1

即：正数是从前向后，负数是从后向前

### 3.2 修改、添加和删除元素

大多数列表都将是**动态**的，意味着可以对列表的元素进行**增删改**

#### 3.2.1 修改列表元素

要修改列表元素，可指定列表名和要修改的元素索引，再指定该元素的新值。

list[1] = 'new elem'

#### 3.2.2 在列表中添加元素

- 在**列表末尾**添加元素 **append()**

  ```python
  motocycles = ['honda', 'yamaha', 'suzuki']
  print(motocycles)
  
  motocycles.append('ducati')
  print(motocycles)
  ```

- 在**列表中**插入元素 **insert()**

  ```python
  motocycles = ['honda', 'yamaha', 'suzuki']
  motocycles.insert(0, 'ducati')
  print(motocycles)
  ```

- 从列表中删除元素 
  - :one:**del**

  ```python
  motocycles = ['honda', 'yamaha', 'suzuki']
  print(motocycles)
  del motocycles[0]
  print(motocycles)
  ```

  

  - :two:**pop()**删除**列表末尾**的元素

  ```python
  motocycles = ['honda', 'yamaha', 'suzuki']
  print(motocycles)
  
  popped_motocycle = motocycles.pop()
  print(motocycles)
  print(popped_motocycle)
  ```

  

  - :three:**pop(index)**删除任何位置的元素

  ```python
  motocycles = ['honda', 'yamaha', 'suzuki']
  first_owned = motocycles.pop(0)
  print('The first motocycle I owned was a ' + first_owned.title() + '.')
  ```

  

  - :four:**remove()**根据值删除元素

  ```python
  motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
  print(motocycles)
  motocycles.remove('ducati')
  print(motocycles)
  ```

  

### 3.3 组织列表

#### 3.3.1 使用sort()对列表进行永久性排序

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

car.sort(reverse=True)
```

#### 3.3.2 使用函数sorted()对列表进行临时排序

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)
```

#### 3.3.3 倒着打印列表

```python
cars = ['bmw', 'toyota', 'audi', 'subaru']
print(cars)
cars.reverse()
print(cars)
```

:heavy_exclamation_mark:反转列表元素的顺序

#### 3.3.4 确定列表的长度

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
```

## 4 操作列表

### 4.1 遍历整个列表

for循环

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```



#### 4.1.1 深入地研究循环

for……

#### 4.1.2 在for循环中执行更多的操作

#### 4.1.3 在for循环结束后执行一些操作

### 4.2 避免缩进错误

#### 4.2.1 忘记缩进

#### 4.2.2 忘记缩进额外的代码行

#### 4.2.3 不必要的缩进

#### 4.2.4 循环后不必要的缩进

#### 4.2.5 遗漏了冒号

### 4.3 创建数值列表

#### 4.3.1 使用函数range()

```python
for value in range(1, 5):
    print(value)

# output: 
# 1
# 2
# 3
# 4
```

#### 4.3.2 使用range()创建数字列表

```python
numbers = list(range(1, 6))
print(numbers)

# output: [1, 2, 3, 4, 5]
```

```python
even_numbers = list[range(2, 11, 2)]
print(even_numbers)

# output: [2, 4, 6, 8, 10]
```

```python
# 将前10个整数的平方加入到一个列表中
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    print(squares)

# output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

#### 4.3.3 对数字列表执行简单的统计计算

- min()
- max()
- sum()

#### 4.3.4 列表解析

列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。

```python
squares = [value**2 for value in range(1, 11)]
print(squares)
```

### 4.4 使用列表的一部分

#### 4.4.1 切片

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# output: ['charles', 'martina', 'michael']
print(players[1:4])
# output: ['martina', 'michael', 'florence']
print(players[:4])
# output: ['charles', 'martina', 'michael', 'florence']
print(player[2:])
# output: ['michael', 'florence', 'eli']
print(players[-3:])
# output: ['michael', 'florence', 'eli']
```

#### 4.4.2 遍历切片

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three player on my team: ")
for player in players[:3]:
    print(player.title())
```

#### 4.4.3 复制列表

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods = my_foods
# 二者不一样
```

### 4.5 元组

需要创建一系列不可修改的元素时，元组可以满足。即将不可变的列表称为元组。

#### 4.5.1 定义元组

元组使用圆括号()而不是方括号

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```

当你试图去修改元组中的数据时，会报错

#### 4.5.2 遍历元组中的所有值

```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```

#### 4.5.3 修改元组变量

虽然不能修改元组的元素，但是可以给存储元组的变量赋值。

```python
dimensions = (200, 50)

dimensions = (400, 100)
```

## 5 if语句

### 5.1 一个简单示例

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# output: 
# Audi
# BMW
# Subaru
# Toyota
```

### 5.2 条件测试

### 5.3 if语句

:one: 简单的if语句

```python
if conditional_test:
	do something
```

:two: if-else语句

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registred to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

:three: if-elif-else结构

```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
```

### 5.4 使用if语句处理列表

#### 5.4.1 检查特殊元素

#### 5.4.2 确定列表不是空的

#### 5.4.3 使用多个列表

## 6 字典

字典是一系列**键值对**，每个键都与一个值相关联，值可以是数字、字符串、列表、字典。事实上，可以将任何Python对象用作字典中的值。

字典是一种动态结构，可对字典中的数据进行操作。

### 6.1 一个简单的字典

```python
alien_0 = {'color': 'green', 'points': 5}
```

### 6.2 使用字典

#### 6.2.1 访问字典中的值

```python
print(alien_0['color'])
# output: green
```

#### 6.2.2 添加键值对

#### 6.2.3 创建一个空的字典

#### 6.2.4 修改字典中的值

#### 6.2.5 删除键值对

### 6.3 遍历字典

#### 6.3.1 遍历所有的键值对

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.item():
    print("\nKey: " + key)
    print("Value: " + value)
```

#### 6.3.2 遍历字典中的所有键

dict.keys()

#### 6.3.3 按顺序遍历字典中的所有键

sort(dict.keys())

#### 6.3.4 遍历字典中的所有值

dict.values()

#### 6.3.5 集合

集合类似于列表，但是每个元素都是独一无二的，即没有重复的元素。

set()

{}

### 6.4 嵌套

#### 6.4.1 字典列表

[{k: v, k: v}, {k: v, k: v}, {k: v, k: v}]

#### 6.4.2 在字典中存储列表

{k: v, k: []}

#### 6.4.3 在字典中存储字典

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
```



## 7 用户输入和while循环

### 7.1 函数input()的工作原理

函数input()接受一个参数：即要向用户显示的提示或说明。

#### 7.1.1 编写清晰的程序

指明input的内容是什么

#### 7.1.2 使用int()来获取数值输入

使用函数input()时，Python将用户输入解读为字符串。

#### 7.1.3 求模运算符

9 % 4

9 % (-4)

(-9) % 4

(-9) % (-4)

### 7.2 while循环

#### 7.2.1 使用while循环

直到不满足while条件时，结束循环

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

#### 7.2.2 pass

#### 7.2.3 pass

#### 7.2.4 使用break退出循环

```python
while True:
    city = input()
    if city == 'quit':
        break
    else:
        print(city.title())
```

#### 7.2.5 在循环中使用continue

不执行后面的代码，进入下一次循环

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

#### 7.2.6 避免无限循环

### 7.3 使用while循环来处理列表和字典

#### 7.3.1 在列表之间移动元素

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

#### 7.3.2 删除包含特定值的所有列表元素

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

#### 7.3.3 使用用户输入来填充字典

```python
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
```



## 8 函数

### 8.1 定义函数

```python
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()
```

#### 8.1.1 向函数传递信息

```python
def greet_user(username):
    print("Hello, " + username.title() + "!")
greet_user('jesse')
```

#### 8.1.2 实参和形参

变量username是一个形参

值 'jesse' 是一个实参

### 8.2 传递实参

位置实参：要求实参的位置与形参的顺序相同

关键字实参：每个实参都由变量名和值组成

列表和字典

#### 8.2.1 位置实参

```python
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
```

:arrow_right:位置实参的顺序很重要

#### 8.2.2 关键字实参

```python
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
```

#### 8.2.3 默认值

形参带有默认值

#### 8.2.4 等效的函数调用

位置实参和关键字实参，根据实参的传递不同，分情况处理

#### 8.2.5 避免实参错误

例如：忘记传递实参，少传递实参，多传递实参

### 8.3 返回值

#### 8.3.1 返回简单值

```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' +last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# output: Jimi Hendrix
```

#### 8.3.2 让实参变成可选的

```python
def get_formatted_name(first_name, middle_name='', last_name):
    pass
```

#### 8.3.3 返回字典

```python
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_persion('jimi', 'handrix')
print(musician)
```

#### 8.3.4 结合使用函数和while循环

```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    formatted_name = get_formatted_name('a', 'b')
    pass
```

### 8.4 传递列表

```

```



