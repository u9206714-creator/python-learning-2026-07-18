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
#1）.format
for name1, gpa1 in gpa_dict.items():
    print('{0}你好，你当前绩点为：{1:.2f}'.format(name1,gpa1))
#2) f-str
for name2, gpa2 in gpa_dict.items():
    print(f'{name2}你好，你当前绩点为：{gpa2:.2f}')
'''



#三、while函数巩固










