# a=15
# b=20
# c={4:'s'}
# if a>b:
#     print('计算结果:%d'%a)
# else:
#     print('计算结果:%d'%b)
# print('a''b')
# print(c[4])
# pizza={
#     'crust':['sd','sdad'],
#     'asdf':['sdada','12da']
# }
# for name,languages in pizza.items():
#     print('\n'+name.title()+'\'s faved food')
#     for language in languages:
#         print('\t'+name.title())
# print(type(languages))
# a=[1,2,3,4,5]
# b=a
# a.append(7)
# b.append(6)
# print(f'{a}''\n'f'{b}')
# def b_person(first,last,age=None):
#     person={first:first,last:last}
#     if age:
#         person['age']=age
#         return person
# m=b_person('sddad','hadj',1)
# print(m)
# import copy
# a=['sdad','adsa','1sd5',[12,34]]
# # b=a[:]
# b=copy.deepcopy(a)
# b.append(12)
# a.append(34)
# print(a,id(a),id(a[3]))
# print(b,id(b),id(b[3]))
# a=("'sd'",'sdadd',1,2)
# print(a[0])
# for i in 'sdadad':
#     print(i)
# from test3 import *
# from test2 import *
# print(name)
# funa()
# funb()
# import test3,test2
# from test3 import *
# 斐波那契数列（嵌套函数）:1,1,2,3,5,8,13,21.....n=(n-1)+(n-2)
# def add(n):
#     if n<=1:
#         return n
#     return add(n-1)+add(n-2)
# # print(add(6))
# def test(n):
#     return n
# a=test
# b=test(1)
# print(id(a))
# print(id(1))
# print(id(b))
# 装饰器
# def send():
#     print(1111)
# def outer(fn):
#     def inner():
#         print(2222)
#         fn()
#         return 0
#     return inner
# print(outer(send))
# print('--------------')
# ot=outer(send)
# ot()
# print(ot())
# print('--------------')
# print(outer(send()))
# print('--------------')
# print(outer(send)())
# print('--------------')
# def outer(m):
#     n=10
#     def inner():
#         print(m+n)
#         return 'hbw'
#     return inner()
# ot=outer(20)
# print('----')
# print(outer(20))
# print('------')
# print(ot)
# print('-------')
# def outer():
#     print()
# print(outer())
# def test1(*args):
#     print(args)
# def outer(fn):
#     n=10
#     def inner():
#         print(n)
#         fn()
#     return inner
# ot=outer(test1)
# print(ot)
# # ot()
# def test1(**kwargs):
#     print(kwargs)
# test1(name='sdads',age=125)
# dic={'name':'bingbing','age':125}
# dic['fname']='hbw'
# print(dic)
# class dog:
#     def __init__(self,name,age):
#         self.a=age
#         self.n=name
#         print(self)
# a=dog('hbw',20)
# print(a.n)
# # a=[{'n':'hbw','num':1},{'n':'yjy','num':2}]
# for i in a:
#     print(i['n'])
#     print(i)

# class person:
#     name='hbw'
# pe=person()
# print(pe.name)
# person.name='yjy'
# print(person.name)
# pe2=person()
# print(pe2.name)

# class Man:
#     name='hbw'
#     _age=18
#     __num=2
#     def __play(self):
#         print('玩手机')
#     def funa(self):
#         print('平平无奇')
#         self.__play()
#         Man.__play(self)
#         print(f"{Man.name}      {self.name}")
#     def _funb(self):
#         print('hello')
#         self.__play()
# ma=Man()
# ma.funa()
# ma._funb()
# ma._Man__play()
# ma._age=20
# print(ma._age)
# ma._Man__num=3
# print(ma._Man__num)
# class Person(object):
#     name = "hbw"
#     @staticmethod
#     def study():
#         print(f'{Person.name}在学习')
#     @classmethod
#     def sleep(cls):
#         print('人类在睡觉')
#         print(cls)
# a=Person()
# print(a)
# # Person.study()
# # a.study()
# Person.sleep()
# print(Person)
# print('--------')
# def person():
#     person = Person()
#     person.study()
#     return person
# b=person()
# print('-----')
# print(person())
# print('-----')
# print(b)
# print(person)
#
# 单例方法
# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print('这是new方法')
#         print('返回值：',super().__new__(cls))
#         print(cls)
#         return super().__new__(cls)
#     def __init__(self,name):
#         self.name = name
#         print(self)
#         print('名字是：',self.name)
# pe=Person('hbw')
# print()
# print(pe)
# print(Person)
# print(type(pe))

# 单例模式
# class Singleton:
#     obj=None
#     def __new__(cls,*args,**kwargs):
#         print('这是__new__方法')
#         if cls.obj is None:
#             cls.obj=super().__new__(cls)
#         return cls.obj
#     def __init__(self,name):
#         self.name=name
#         print(f'我是{self.name}')
#         print('我是__init__方法')
# s=Singleton('hbw')
# print(s)
# # print()
# # print(s.obj)
# print('----------')
# s2=Singleton('yjy')
# print(s2)
# print()
# print(s2.obj)

# class test(object):
#     point=None
#     c=0
#     def test1(self,age):   # 使用对象访问类属性，它会先去对象的内存空间里面找c属性，如果没有，就向上找对象所属类的内存空间。
#         if self.c is 0:    # 要记住一点，只要给对象有了赋值操作，那么就相当于给对象的内存空间中动态创建了一个属性，所以这里此时a对象的内存空间中有了一个c属性了，是属于这个对象的属性，也就是我们所说的实例属性。
#             self.c=age     # 网址https://blog.csdn.net/windyJ809/article/details/118197946?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522d96bfca0f0f0fe22335fdd3d8fe80930%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=d96bfca0f0f0fe22335fdd3d8fe80930&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-118197946-null-null.142^v102^pc_search_result_base7&utm_term=python%E7%B1%BB%E5%B1%9E%E6%80%A7%E5%92%8C%E5%AE%9E%E4%BE%8B%E5%B1%9E%E6%80%A7&spm=1018.2226.3001.4187
#         print(self.c)
#         print(test.c)
#     def __new__(cls,*args,**kwargs):
#         if cls.point is None:
#             cls.point=super().__new__(cls)
#         print(cls.point)
#         return cls.point
#     def __init__(self,name):
#         self.name = name
#         print(f"我是{self.name}")
# a=test('hbw')
# d=a.test1(2)
# print(d)
# print(a.c)
# print()
# b=test('yjy')
# e=b.test1(1)

#通过导入模块实现单例模式
#使用其他模块导入是，同一模块下的类均是同一地址，因为一个模块就是天然的单例模式

#应用场景：回收站对象，音乐播放器，开发游戏软件，数据库

#魔法方法&魔法属性:__new__()、init、doc、module、class、str、del、call、dict、
#doc 返回类&函数的描述信息，只可多行注释，不可单反注释
# module：表示当前操作对象所在模块
# class：表示当前操作对象所在类
#str()：对象的描述信息,如果类中定义了此方法，那么在打印对象时，默认输出该方法的返回值，也就是打印方法中的return的数据
#注意：str必须返回一个字符串
#del()：析构函数，程序结束和删除某个对象时都会被调用
#call()：使用一个实例对象成为一个可调用对象，就像函数那样可调用
#可调用对象：函数\内置函数和类都是可调用对象，凡是可以把一对()应用到某个对象身上都可以称之为可调用对象
#callable()：判断一个对象是否是可调用对象
# def func():
#     print('hhh')
# func()
# print(callable(func)) #True
# class A:
#     def __call__(self):
#         print('这是__call__')
#     pass
# a = A()
# a()   #调用一个可调用的实例对象，其实就是在调用他的__call__()方法
# print(callable(a))

#文件
# f=open('C:\\Users\\35270\\Desktop\\file.txt')
# print(f.name)
# print(f.mode)
# while True:
#     text=f.readline()
#     if not text:
#         break
#     print(text)
# f.close()
#r+：可读写文件，文件不存在就报错
#w+：先读再写，文件存在就重新编辑文件，文件不存在就创建新文件
#文件光标
# f=open('C:\\Users\\35270\\Desktop\\file.txt')
# print(f.read())
# f.close()
#文件定位操作
#tell()：显示文件当前指针所在位置
#seek(offset，whence)   seek(0，0）就是回到开头
#offset：偏移量
#whence：起始位置，默认是文件开头（0）
# f=open('C:\\Users\\35270\\Desktop\\file.txt','w+')
# f.write('hello world')
#
# print(type(f.read()))
# print(f.read())
# print(type(f.readline()))
# print(type(f.readlines()))
# f.seek(0,0)
# print(f.read())
# f.close()
# while True:
#     firstnum = input("Enter your first num: ")
#     if firstnum == "q":
#         break
#     lastnum = input("Enter your last num: ")
#     if lastnum == "q":
#         break
#     try:
#         answer = int(firstnum) / int(lastnum)
#     except ZeroDivisionError:
#         print("Please enter not 0")
#     else:
#         print(answer)
#split函数
# a=input().split(',')
# print(a)
# for i in a:
#     print(i)

#读取图片：图片是一个二进制文件，想要写入必须先要拿到
#写入图片
# with open('C:\\Users\\35270\\Desktop\\图片.jpg','rb') as f:
#     img = f.read()
#     print(type(img))
#     print(img)
# with open('E:\\python xm\\图片.jpg','wb') as f:
#     f.write(img)
#文件目录命令：import os
# 文件重命名：os.rename(旧名字，新名字)
# 删除文件：os.remove()
# 创建文件夹：os.mkdir()
# 删除文件夹：os.rmdir()
# 获取当前目录：os.getcwd()
# 获取目录列表：os.listdir()   os.listdir('../')   ../获取上一级目录列表

#可迭代对象(Iterable):能被for循环遍历的对象
#遍历（迭代）：依次从对象中把一个个元素取出来的过程
#数据类型：str、list、tuple、dict、set等
#可迭代对象的条件：对象实现了__iter__()方法，__iter__()方法返回了迭代器对象
#for循环工作原理
# 1.先通过_iter_()获取可迭代对象的迭代器
# 2.对获取到的迭代器不断调用__next __ ()方法来获取下一个值并将其赋值给临时变量i
# isinstance():判断一个对象是否是可迭代对象或者是一个已知的数据类型
# 导入模块
# from collections.abc import Iterable
# #isinstance(o,t) o:对象 t:类型  可以是直接或者间接类名、基本类型或者元组
# st='123'
# print(isinstance(st,Iterable))
# print(isinstance(st,(int,str)))
# print(isinstance(st,(int,dict)))
# 迭代器 Iterator
#是一个可以记住遍历位置的对象;在上次停留的位置继续去做一些事情
# 1i = [1,2, 3, 4, 5]
# for i in li:
# print (i)
# iter():获取可迭代对象的迭代器
# next():一个个去取元素,取完元素后会引发一个异常
# li = [1, 2, 3, 4, 5]
# 创建迭代器对象
# li2 = iter(li)
# print(li2)
# 获取下一条数据
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
#取完元素后，再使用next()会引发StopIteration异常
# 第二种方法
# li2=li.__iter__()
# print(li2)
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(dir(li2))
# #步骤：
#1.iter()调用对象的_iter_(),并把_iter_()方法的返回结果作为自己的返回值
#2.next()调用对象的_next_(),一个个取元素
#3.所有元素都取完了,_next_()将引发StopIteration异常
# 总结
# 可迭代对象可以通过iter()转换成迭代器对象
# 如果一个对象拥有_iter_(),是可迭代对象,如果一个对象拥有_next_()和_iter_()方法,是迭代器对象
# dir():查看对象中的属性和方法

# 迭代器协议
# 对象必须提供一个next方法,执行该方法要么就返回迭代中的下一项,要么就引发StopIteration异常,来终止迭代
# 自定义迭代器类
# 两个特性:__iter__()和__next__()

#自定义可迭代对象
class MyIterable:
    def __init__(self):
        self.data = [1,2,3,4,5]
    def __iter__(self):
        return MyIterator(self.data)
# 自定义迭代器类
# class MyIterator(object):
#     def __init__(self,data):
#         self.datas = data
#         self.index = 0
#     def __iter__(self):   #返回的是当前迭代器类的实例对象
#         return self
#     def __next__(self):
#         if self.index< len(self.datas):
#             result=self.datas[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration('终止迭代，数据已经被取完了')
# mi=MyIterator([1,2,3,4,5])
# mi2=MyIterable()
# print(mi)
# print(mi2)
# print(mi.__next__())
# print()
# for i in mi:
#     print(i)
# print()
# for i in mi2:
#     print(i)
# print(MyIterator)
# print(mi)
# print(mi.__iter__())
# print()
# print(mi.__next__())
# print()
# for i in mi:
#     print(i)
#生成器
# Python中一边循环一边计算的机制,叫做生成器
#表达式：将列表推导式的[]改为()
# li=[i*5 for i in range(5)]
# gen=(i*5 for i in range(5))
# print(li)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#生成器函数：Python中,使用了yield关键字的函数就称之为生成器函数
# yield的作用:
# 1.类似return,将指定值或者多个值返回给调用者
# 2.yield语句一次返回一个结果,在每个结果中间,挂起函数,执行next(),再重新从挂起点继续往下执行
#  是函数中断,并保存中断的状态
# li=[]
# def test():
#     print('True')
#     li.append('a')
#     print('li=',li)
# test()
# test()
# def gen () :
#     print('开始了')
#     yield 'a'
#     yield 'b'
#     yield 'c'
# gen_01 = gen()
# print(gen_01)
# print(next(gen_01))
# print(next(gen_01))

# def test_a():
#     yield 1
#     yield 2
#     yield 3
# print(test_a)
# print(test_a())
# ta=test_a()
# print(ta)
# print(next(ta)) #从对象中取值
# print(next(ta))
# print(next(ta))
# print(next(test_a())) #加括号是调用函数
# print(next(test_a()))

#print(函数名/类名/....)返回的是该类型和该类型存在的地址
#而如果令一个变量i=函数名()/类名()/.... 则print(i)返回的就是以该类型或该类创建的变量及该变量所在位置
#加括号可以理解为引用，与c语言中的指针差不多


#  三者关系
#可迭代对象:指实现了python迭代协议,可以通过for .. in .. 循环遍历的对象,比如1ist、dict、str ... 、迭代器、生成器
#迭代器:可以记住自己遍历位置的对象,直观体现就是可以使用next()函数返回值,迭代器只能往前,不能往后,当遍历完毕之后,next()会抛出异常
#生成器:是特殊的迭代器,需要注意迭代器并不一定是生成器,它是python提供的通过简便的方法写出迭代器的一种手段
#包含关系:可迭代对象>迭代器>生成器

#字符串操作以及列表转字符串 网址：https://zhuanlan.zhihu.com/p/474884078 ， https://blog.csdn.net/weixin_55144746/article/details/140447421?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522b987579e0100baf8eadc8da074d47bb4%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=b987579e0100baf8eadc8da074d47bb4&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-140447421-null-null.142^v102^pc_search_result_base7&utm_term=%E5%A6%82%E4%BD%95%E5%B0%86%E5%88%97%E8%A1%A8%E6%94%B9%E4%B8%BA%E5%AD%97%E7%AC%A6%E4%B8%B2&spm=1018.2226.3001.4187
# a=str('abc')
# print(a)
# b="'sda'"
# print(type(a))
# print(b)
# print(a+b)
# print(type(b))
# a=['sda',123,'sdad',"'sdaf'"]
# c=" ".join(map(str,a))
# print(c)
# list1=['a','b','c',123]
# list2=[str(i) for i in list1]
# str1=' '.join(list2)
# print(str1)
#  map函数：map(function, iterable)  网址：https://blog.csdn.net/u012856866/article/details/131660354?ops_request_misc=%257B%2522request%255Fid%2522%253A%252285de0aa14c74f4b1c10ff8d4b1f5467c%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=85de0aa14c74f4b1c10ff8d4b1f5467c&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-131660354-null-null.142^v102^pc_search_result_base7&utm_term=map%E5%87%BD%E6%95%B0&spm=1018.2226.3001.4187
# function：一个函数或方法
# iterable：一个或多个序列（可迭代对象）
# map() 函数的作用是：对序列 iterable 中每一个元素调用 function 函数，返回一个map对象实例。这个map对象本质上来讲是一个迭代器。
















