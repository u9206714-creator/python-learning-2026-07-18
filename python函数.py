#I have learnt some functions before
#一、for in函数巩固
#1、打印一到十的所有数字
'''
for i in range(1,11):
    print(i)
'''
    
#2、计算1到100的总和
'''
total = 0
for i in range(1,101):
    total = i + total
print(total)
'''

#3、打印列表中所有大于60的成绩
'''
student_score = [1,3,47,56,67,79,85,92]
for score in student_score:
    if score > 60:
        print(score)
'''

#4、遍历一个字典，打印所有key和value
'''
dict = {'student_A':'01','student_B':'02','student_C':'03','student_D':'04'}
for student, code in dict.items():
    print(student,code)
'''



#二、f-str练习巩固
#1、同时获取一个函数的索引和值
'''
fruits = ['apple','banana','orange']
for index, fruit in enumerate(fruits) :
    index = index + 1    
    print(f'第{index}个水果是：{fruit}')
'''
    
#2、圆的面积公式
'''
different_radius = range(1,6)
pi = 3.14
for radius in different_radius:
    area = pi*(radius**2)
    print(f'the area of the circle is {area}')
'''

#3、分别用f-str和.format的方法表示同一项数据
'''
gpa_dict = {'小明':3.251,'小花':3.869,'小李':2.683,'小张':3.685}
'''
#1）.format
'''
for name1, gpa1 in gpa_dict.items():
    print('{0}你好，你当前绩点为：{1:.2f}'.format(name1,gpa1))
'''
#2) f-str
'''
for name2, gpa2 in gpa_dict.items():
    print(f'{name2}你好，你当前绩点为：{gpa2:.2f}')
'''



#三、while函数巩固
#1、打印表格中的字符串（与for in函数比较）
'''
list1 = ['H','e','l','l','o']
for char in list1:
    print(char)

i = 0
while i < len(list1):
    print(list1[i])
    i += 1
'''

#2、写一个对用户输入数字求平均值的计算器
'''
user_input = input('请输入数字,输完记得按q:')
total = 0
count = 0
while user_input != 'q':
    num = float(user_input)
    total += num
    count += 1
    user_input = input('请输入数字,输完记得按q:')
if count == 0:  #== is to compare ; = is to assign a value to a valuable
    result = 0
else :
    result = total / count
print(f'你输入的值为：{result}')
'''

#3、使用 while 循环打印数字 1 到 20，每行打印一个数字。
'''
i = 1
while i <= 20:
    print(i)
    i += 1
'''

#4、使用 while 循环计算 1 + 2 + 3 + ... + 100 的总和，并打印结果。
'''
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)
'''

#5、让用户输入一个正整数。如果输入的数字<=0, /
   #就一直提示“请输入一个正整数：”重新输入，直到用户输入正确的正整数为止。最后打印“你输入的数字是：xxx”
'''
user_input = int(input('请输入一个正整数:'))
while user_input <= 0 :
    print('请输入一个正整数,重新输入:')
    user_input = int(input('请输入一个正整数:'))
print(f'你输入的数字为：{user_input}')
'''


















