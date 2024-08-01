#DAY7 算数运算符 +，-，*， /除, //取整取商, %取余取模,**求幂
# != 不等于，==等于，










#DAY8 复杂的多项选择
#if ,elif,else,
# time=13
# num=2
# if time>=9 and time <=23 and num>=2:
#     print('在打折时间内全场八折')
#     if num>=2:
#         print('全场八折')










#Day9 存储多个数据的元组 元组不可更改
#calendar=('1月1日','1月2日','1月3日','1月4日')
#result = '1月1日' in calendar #查询数据
#print(result)
#print(calendar[0])
#print(calendar[2:])
#print(calendar[:3])
#print(calendar[2:3])






#Day10 灵活多变的列表
#friendName=['Max','Jeremy','christina','jomb','bomb']
#print(friendName)
#print(friendName[1:3]) #切片左闭右开 第2到第3个输出
#print(friendName[1:]) #切片 第2个之后
#print(friendName[:3])  #切片 第3个及之前
#print(friendName[0]) #提取 第1个
#print(friendName[3]) #提取 第4个
#friendName[3]='yufang' #直接更改，还有插入insert,排队增加
#friendName.insert(0,'liling') #直接插入元素
#print(friendName[3])
#print(friendName)
#friendName.append('liyao') #排队加元素
#print(friendName)






#Day11 列表的便捷操作 可更改调用
#friendName=['Max','Jeremy','christina']
#friendName.append('vane') #排队加一元素
#print(friendName)
#friendName.insert(1,'May') #插入一元素
#print(friendName)







# Day12  一对一的字典  可更改调用
#products={'口香糖':15,'可乐':5,'薯片':45}
#print(products)
#products['other']='七折'
#print(products)






# Day14 fpr 循环的基础操作
# 复习 三大数据结构 元组()   列表[] 可改 插入 删除   字典{} 插入
# numberlist=[10,20,30,40,50,60]
# for number in numberlist :
#     print(number)
# numberlist=(10,20,30,40,50,60)
# for number in numberlist :
#     print(number)
# numberlist=(10,20,30,40,50,60)
# for number in numberlist :
#     print(number)
# numberlist={'小明':10,'小龙':15,'小兵':16,'小月':17,'小白':19}
# for number in numberlist :
#     print(number)
# numberlist['金波']=21
# print(numberlist)









# Day15 for 循环的复杂应用

# 累加
# jdList=[3,1.5,4,2]
# total=0
# for price in jdList :
#     total=total + price
# print(total)

# 计时器
# names=['Tom','Tim','Amy','Eva']
# count=0
# for name in names :
#   count=count + 1
#   print(f'第{count}名是{name}')
#     print(name)
# 题目 班级排名
# students=['Tom','Blue','Max','Stufen','Joe','Tim']
# count=0
# for student in students :
#     count=count+1
#     print(f'第{count}名是{student}')

# if 语句 求和
# judlist=[3,'-',4,'-',6]
# total=0
# for price in judlist :
#     if price != '-' :
#         total=total + price
# print(total)

#numbers=[2,9,11]
#for num in numbers :
#    if num > 3 :
#        print(num)

# for 循环结构   有天然的边界条件  遍历列表
#numbers=[2,9,6.4,3,5]
# for num in numbers :
#    print(num)
#for num in numbers :
#    if num > 4.9 :
#        print(num)

#numbers=[2,9,6.4,3,5]
#total=0
#for num in numbers :
#    if num>4.9 :
#        total=total +num
#    print(num) #完整循环
#print(total)  #循环结束后计算所有循环的总值

#numbers=[2,9,6.4,3,5]
#total=0
#for num in numbers :
#    if num>4.9 :
#        total=total +num
#print(num)
#print(total)

#numbers=[2,9,6.4,3,5,8]
#total=0
#for num in numbers:
#    if num>4.9 :
#        total=total+num
#print(num)
#print(total) # 和for缩进一样时，循环结束后才输入，即输入循环的最后一环








#Day 16 while 没有边界，触发条件就停，否则一直循环，死循环 
# while 条件循环，设计的边界条件

#tag=True
#while tag==True :
#    print('hello,world')
#    tag=False

#count=0
#while count <50 :
#    count=count + 1
#    print(count)   

#报数
#c=1
#while c <=50 :
#    print(c)
#    c=c+1 
#累加数学题
#c=0
#total=0
#while c<=50 :
#    total=total+c
#    c=c+1
#print(total)

#隔天训练
#c=1
#while c <=5 :
#    if c % 2 != 0 :
#        print(c)
#    c=c+1        
#经典数学题 从1加到100的核
#sum=0
#total=0
#while sum <100 :
#    sum = sum +1
#    print(sum)
#    total=total + sum
#print(total)

# num=0
# total=0
# while num<=100 :
#     total=total+num
#     num=num+1
#     print(num)    
# print(total)

#经典题目 偶数请出列
#counter=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#newlist=[]
#counter=1
#while counter <21 :
#    if counter % 2 == 0:
#        newlist.append(counter) 
#    counter=counter +1
#print(newlist)  










  # Day17  跳出循环的办法
  # break  continue
#numberlist=[10,4,1,20,6]  #break 使用，终止循环
#for i in numberlist :
#    print(i)
#    if i > 15 :
#        break
#print(numberlist)
#print(i)

# drinks=['water','coke','tea','milk']
# for item in drinks :
#    if item == 'coke' :
#        continue # 跳过本次代码中的后面代码，直接进入下一次循环
#    print(item)

#经典题目 买西瓜 难度等级 困难

# weightlist=[4,3.5,2,5,6,3,4.7,5.3]
# n=0
# newlists=[]
# for i in weightlist :
#     if n==3 :
#         break
#     if i >= 4 :
#         newlists.append(i)
#         n=n+1
#         continue
# print(newlists)
    
#题目 找出第一个
# worldlist=['cherry','lemon','apricot','blueberry','durian','grape','apple']
# for world in worldlist :
#     if world[0]=='a':
#        #print(world) 
#        break
# print(world)

#题目 打卡日历
# record=[60,0,73,139,64,48,73,63,0,59,100,121,44,30,0,0,43,67,64,51,106,0,80,0,119,59,0,58,100,90]
# n=0
# h=3
# for i in record:
#     if i == 0:    
#         n=n+1
#         h=h+1
#         break
# print(n+h)
#         n=n+1
#         continue
#     print(n)
# print(f'这个月有{n}天没有背单词')

#题目 抢购牛奶    
# numberlist=[2,4,3,5,2,2,3,5,2,4]
# total=0
# n=0
# for i in numberlist:
#     total=total+i
#     if total>15:
        
#         print(f'有{n}个人可以买到牛奶')
#         break
#     n=n+1
 
 #题目 成绩单
# scores=[87,54,71,88,92,58,79,48]
# A=[]
# B=[]
# C=[]
# for i in scores :
#     if i>=90 :
#         A.append[i]
#     elif i<90 and >= 60 :
#         B.append[i]
#     else :
#         C.append[i]
        









#day 18 循环的综合应用

#给每位姑娘打上名字+节日快乐
# girls=['Max','Sunny','Sissi','May','Ann']
# for names in girls:
#     print(f'{names}节日快乐')

#计算京东账户购物车里的5件商品清空要花多少钱
# jdlist=[2,5,8,9,15]
# total=0
# n=0
# for price in jdlist:
#     total=total+price
# print(total)

#leader提出，如果女生们所选的礼品金额大于200的就可以晋级下一轮的终极PK！
# giftamount=[150,149,155,200,180,250,70,80,200,60,280]
# for numbers in giftamount :
#     if numbers > 170 :
#         print(f'恭喜礼品券为{numbers}的女生们晋级下一轮的终极PK')

#经过一轮PK，本次节日最幸运的女神是Ann~
# brandlist=['Jamer','Cbp','Sk3']
# itemlist=['精华','面露','眼霜','爽肤水']
# for brand in brandlist :
#     for item in brandlist:
#         print(f'恭喜本次节日的幸运女神{brand},她将获得“清空护肤品{item}愿望清单特权”一次')

#嵌套的使用实现
# brandlist=['Jamer','Cbp','Sk3']
# itemlist=['精华','面露','眼霜','爽肤水']
# for brand in brandlist :
#     for item in brandlist:
#         print(f'恭喜本次节日的幸运女神{brand},她将获得“清空护肤品{item}愿望清单特权”一次')

#题目 Lucky的亮亮
# brandlist=['苹果','华为','小米']
# itemlist=['新款手机','平板电脑','智能手机']
# for brand in brandlist:
#     for item in itemlist:
#         print(f'恭喜亮亮将获得{brand}品牌的{item}一份')

#题目 luky的亮亮，获得了9个奖品 ，打算将列表中的5个礼物送给女朋友

#while 条件循环
# itemlist=['精华','面露','眼霜','爽肤水','玫瑰花','电脑','笔记本','平板','手表']
# n=0
# while n<5 : 
#     print(f'亮亮将{itemlist[n]}送给一直支持他的女朋友')
#     n=n+1

#for 循环
# itemlist=['精华','面露','眼霜','爽肤水','玫瑰花','电脑','笔记本','平板','手表']
# list=[0,1,2,3,4]
# for i in list :
#     print(f'亮亮将{itemlist[i]}送给一直支持他的女朋友')

#遍历整数列表 List Traversal
#range的功能是创建一个整数列表
# itemlist=['精华','面露','眼霜','爽肤水','玫瑰花','电脑','笔记本','平板','手表']
# for i in range(4) :
#     print(f'亮亮将{itemlist[i]}送给一直支持他的女朋友')

#range 范围 
# total=0
# for i in range(50): #默认是从0开始，可省略，
#     total=total+i
#     i=i+1
# print(total)

#经典编程题，使用嵌套和range()功能结合，输出九九乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         if i>=j:
#             print(f'{i}*{j}={i*j}')

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}')

#使用for循环和range()函数，计算50以内，不包括50的整数之和，并输出最终结果
# total=0
# for i in range(50):
#     total=total+i
#     i=i+0
# print(total)










#DAY19 初识函数
# 播放滚动文字
# character='欢迎光临','商品一律九折'
# n=1
# while n>0:
#     print(character)
#     n=n+1

#函数就是封装了特定功能的代码块，是存储代码的“特殊变量”
#像print(),range(),append(),
#定制函数 def
# def saywelcome():
#     print('欢迎光临')
#     print('商品一律九折')

# saywelcome() #调用函数
# saywelcome() #调用函数

#形参和实参 提前挖好的空时形参，用来填空的数据称为实参
# def saywelcome(discount):
#     print('欢迎光临')
#     print(f'商品一律{discount}') #格式化输入 含有变量+字符串

# saywelcome('5折')
# saywelcome('9折')

#题目 定义有参函数
# def sayHi(name,discount):
#     print(f'尊敬的会员{name}!')
#     print(f'欢迎进入我的网站享受{discount}')
# sayHi('吴金波','八折')
      
#题目 计算BMI指数
# def getBMI(height,weight):
#     BMI=weight/(height*height)
#     print(BMI)

# getBMI(1.83,60)
# getBMI(1.60,50)

#题目 通过if语句判断number中的数字是否为奇数，并用print输出结果
# def isodd(number):
#     if number % 2 != 0 :
#         print('奇数')
#     else:
#         print('偶数')

# isodd(25)
# isodd(10)












# DAY20 函数结构
# def getArea(length):
#     area=length*length
#     print(area)

# getArea(2)
# getArea(15)

# def getArea(length):
#     area=length*length
#     return area

#result=getArea(13)
#print(result)
#if result>160:
# if getArea(13)>160:
#     print('就用来种瓜')
      
# def getcalculate(numlist):
#     total=0
#     for i in numlist:
#         total=total+i
        #return total
# number=getcalculate([1,3,4,7,9,10]) 
# print(number)

#题目 定义了一个叫做 "getSize"的函数，该函数包含一个参数length
#该函数功能是计算正方形周长和面积，并将有两个结果作为函数的返回值返回
#现在分两次调用这个函数，第一次传入参数6并输出结果
#第二次传入参数8并输出结果
#正方形周长=4*边长
#正方形面积=边长*边长
# def getSize(length):
#     area=length*length
#     long=4*length
#     print((area,long))
#     return area,long
    
# result=getSize(6)
# print(result)

#题目 定义了一个叫做 "getVolume"的函数，该函数包涵了3个参数length,width,height
#功能是计算长方体体积，并将结果作为函数的返回值返回
# def getVolume(length,width,height):
#     volume=length*width*height
#     return volume

# print(getVolume(4,5,6))
# result=getVolume(7,8,9)
# print(result)

#内置函数 range()生成一个有数字组成的列表,append()向列表追加元素,print()输出数据到屏幕
#内置函数 insert(),pop(),len()
# range(0,5) #数字组成的列表
# for i in range(0,5):
#     if i >1 :
#        print(i)

# data=len(['a','b','c','d','e'])
# print(data)

# 题目 计算BMI指数
# def getBMI(height,weight):
#     BMI=weight/(height*height)
#     #print(BMI)
#     return BMI
# print(getBMI(1.83,60))
# print(getBMI(1.6,50))

#题目 不好意思，12寸的没了，换个6寸的可以吗
# def getArea(R):
#     area=3.14*R*R
#     return area
# bigSize=getArea(6)
# smallSize=getArea(3)
# if bigSize>smallSize*2:
#     print('我们不吃了')
# else:
#     print('可以换')














# DAY21 函数的参数 必选参数 默认参数
# def setATM(card):
#     return f'您的账户为{card}元'
#     #msg=f'您的账户为{card}元'
#     #return msg

# ret1=setATM(123456)
# ret2=setATM(778866)
# print(ret1)
# print(ret2)

#必选参数
# 题目 新增一个存款参数
# def setATM(card,money):
#     msg=f'账户:{card},存款的金额为：{money}元'    
#     #return f'您的账户为{card}元'
#     #msg=f'您的账户为{card}元'
#     return msg

# ret1=setATM(123456,200)
# ret2=setATM(778866,9999)
# print(ret1)
# print(ret2)

# def area(radius,pi=3.14): #必选参数定义在默认参数之前
#     return radius*radius*pi
# sum=area(3,3.145)
# print(sum)
# sum1=area(3)
# print(sum1)

#题目 调用带有默认值参数的函数
# def welcome(name='会员'):
#   msg=(f'尊敬的{name}早上好')
#   return msg
# list=welcome('Gary')
# print(list)
# list=welcome()
# print(list)  


# 题目 欢迎您
# def sayWelcome(name,language):
#   if language=='ZH':
#     list1=f'欢迎你，{name}'
#     return list1
#   elif language=='EN':
#     list2=f'{name},欢迎你'
#     return list2
# sum1=sayWelcome('jack','EN')
# print(sum1)

#题目 欢迎2.0
# def sayWelcome(name,language):
#   if language=='ZH':
#     list1=f'欢迎你，{name}'
#     return list1
#   elif language=='EN':
#     list2=f'{name},欢迎你'
#     return list2
# sum1=sayWelcome('jack','EN')
# print(sum1)
# sum1=sayWelcome('Gray','ZH')
# print(sum1)
# sum1=sayWelcome('jack','EN')
# print(sum1)










 # Day 22 递归和匿名函数 处理复杂的函数建议用def
#square=lambda x:x*x #匿名函数 不需要使用return关键词，冒号后面是函数返回值
#result=square(9)
#print(result)
#print(square(9))

# multiply=lambda x,y :x*y
# result=multiply(9,10)
# print(result)
# print(multiply(9,10))

# power= lambda x,y,z:x*y*z
# result=power(10,8,6)
# print(result)

# def sum(numberlist):
#     total=0
#     for number in numberlist:
#         total=total+number
#     return total

# result=sum([1,3,5,7,9,1])
# print(result)

#递归函数 调用自身的过程叫做递归，
# def sum(n):
#     if n <=0:
#         return 0
#     return n +  sum(n-1)

# print(sum(5))

#计算100以内的整数和
# def sum(n):
#     if n<=0:
#         return 0
#     return n +sum(n-1)
# print(sum(200))

#题目 计算BMI
# BMI=lambda weight,height:weight/height/height
# if BMI(50,1.65)<18.5:
#     print(f'你的BMI为{BMI(50,1.65)},体重过轻')
# #print(BMI(50,1.65))

# def healthy(weight,height):
#     BMI=weight/height/height
#     return BMI

# result=healthy(50,1.65)
# if result <18.5:
#     print(f'你的BMI为{healthy(50,1.65)},体重过轻')



# def healthy(weight,height):
#     BMI=weight/height/height
#     if BMI<18.5:
#         return f'你的BMI为{BMI},体重过轻'
# print(healthy(50,1.65))


#题目 计算10的阶乘
# def factorial(num):
#      if num<=0:
#            return 1
#      return num*factorial(num-1) #递归函数
# list=factorial(10)
# print(list) 

#题目 拓展 
# list= lambda num:num*(num-1)
# total=lambda num:num*(num-1)













#day 23 类与对象 人是类，小明是对象
#属性和方法  品牌序号内存容量等具体限定的的参数的是手机的属性  拍照打电话发短信等功能是所有手机的方法
# class Phone():#为了区分类与函数，建议首字母大写
#     def makecall(self,who):  #成员函数第一个参数为self 定义实例方法的固定写法
#         return f'正在电话给{who}' 
#     def sendMsg(self,who,txt):  #成员函数第一个参数为self 定义实例方法的固定写法
#         return f'正在发信息给{who},内容为{txt}'
    
# myphone=Phone()
# yourphone=Phone()
# ret=myphone.makecall('tony')
# print(ret)
# ret=yourphone.sendMsg('jeremy','中午吃啥')
# print(ret)

#类的属性和初始化 
# class Phone(): 
#     def __init__(self,bd,clr):  #__init__是个特殊的方法
#         print('创建实例对象时，自动调用此方法')
#         self.brand=bd
#         self.color=clr

# myPhone=Phone('华为','黑色')
# yourPhone=Phone('苹果','白色')

# print(f'我有一个{myPhone.color}的{myPhone.brand}手机')
# print(f'我有一个{yourPhone.color}的{yourPhone.brand}手机')  

# 题目 属性的应用
# class Cat():
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#     def talk(self):
#         print('喵喵喵')
# myCat=Cat('大黄','橘猫')
# yourCat=Cat('土豆','布偶猫')
# print(f'我有一只{myCat.breed}叫做{myCat.name}')
# print(f'我有一只{yourCat.breed}叫做{yourCat.name}')

#题目 判断用户是否为会员
# class user():
#     def __init__(self,name,isVIP):
#         self.name=name
#         self.isVIP=isVIP
#     def sayHi(self):
#         if self.isVIP:
#             print(f'尊敬的会员{self.name},欢迎您！')
#         else:
#             print(f'尊敬的{self.name},欢迎您')
# tony=user('Tony',True)
# jeremyy=user('Jeremy',False)

# tony.sayHi()
# jeremyy.sayHi()

#题目 计算学生的平均成绩
# class MathScore():
#     def __init__(self,className,scoreList):
#         self.className=className
#         self.scoreList=scoreList
#         self.studentNums=len(self.scoreList)

#     def getSum(self):
#         s=0
#         for score in self.scoreList:
#             s += score
#         return s
#     def mean(self):
#         return self.getSum()/self.studentNums
#     def showMsg(self):
#         print(f'{self.className}共有{self.studentNums}人，数学平均成绩为{self.mean()}')
# class32=MathScore('三年二班',[78,99,88,87,67])
# class32.showMsg()
                      











#day 25 使用别人代码模块机制
# import random
# randomnum=random.random() #random() 该函数用于生产1个0-1的随机浮点数
# print(randomnum)

# import random
# randomnum=random.randint(1,7)
# print(randomnum)

# import datetime
# todaydate=datetime.date.today()
# print(todaydate)

#题目 获取今日的年份，并判断是否和今年的年份2022相等，相等输出true,不相等输入False
# import datetime
# today=datetime.date.today()
# year=today.year
# print(year==2022)

#导入模块
# from datetime import date
# todaydate=date.today()
# print(todaydate)

#题目 
# from datetime import date
# today=date.today()
# year=today.year
# print(year==2021) 

#内置模块，非内置模块要先进行安装
#使用pip工具安装第三方模块，需要在Windows的命令符里进行  WIN+R 打开cmd
# pip3 install pyecharts==1.8.1
#pip3 install pyecharts==1.8.1-i https://pypi.tuna.tsinghua.cn/simple/

#from pyecharts.charts import Bar
# from pyecharts import options as opts   # import   as ,,导入一个模块的同时取一个别名

#题目3 绘制出一个可交互的柱状图了  此代码失败，日后需重新研究
# from pyecharts.charts import Bar
# from pyecharts import options as opts

# bar=Bar()

# bar.add_xaxis(['衬衫','毛衣','领带','裤子','风衣','高跟鞋','袜子'])
# bar.add_yaxis('商家A',[114,55,27,101,125,27,105])
# bar.add_yaxis('商家B',[57,134,137,129,145,60,49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title='某商场销售情况'))
# bar.render('bar.html')


#题目 引入math模块
# import math
# print(math.sqrt(99))
# print(math.fabs(-0.03))











#day 26 文件操作的入门
# sender='526103916@qq.com'
# reseiverDict={'wujinbo':'wujinbo1117@gmail.com'}
# path='/Users/Administrator/Desktop/bczl'
# for reseiver in reseiverDict:
#     filepath=path+'/'+reseiver+'.jpg'
#     with open(filepath,'rb') as imagefile:      
#         filecontent=imagefile.read()
#         print(filecontent)

# studentAge={'Gary':14,'Adam':13,'jack':15}
# for key in studentAge:
#     print(key)

# path='C:/Users/Administrator/Desktop/bczl/wujinbo.jpg'
# with open(path,'rb') as imagefile:
#     print(imagefile)












#day27 开源模块的应用  
#在代码中登入和发送邮件是由 smtplib 模块负责 该模块是内置模块，直接导入即可
# import smtplib
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# mailUser='526103916@qq.com'
# mailPass='jpkmnjchgjymbjjj'
# smtp0bj=smtplib.SMTP_SSL('smtp.qq.com',465)
# smtp0bj.login(mailUser,mailPass)
# sender='526103916@qq.com'
# receiverDict={'wujinbo':'wujinbo1117@gmail.com','wuxin':'15000867319@qq.com'}
# for receiver in receiverDict:
#     message=MIMEMultipart()
#     message['From']=Header(f'<{sender}>')
#     message['To']=Header(f'{receiver}<{receiverDict[receiver]}>')
#     message['Subject']=Header(f'{receiver}一年会邀请函')
#     smtp0bj.sendmail(sender,receiverDict[receiver],message.as_string())
#     print('发送成功')
   

# Header负责编辑邮件内容 
# message['From']=Header('wujinbo<526103916@qq.com')

#发送一封简单的邮件
#发件人邮箱 sender,,收件人邮箱 reververDict[receiver],邮件内容 message.as_string()
# as_string()方法将message设置为文本格式


#计算一篇英语文章中的词频前10
# import string
# from collections import Counter

# def analyze_text(filename):
#     with open(filename, 'r') as file:
#         text = file.read()
#         words = text.split()
#         word_counts = Counter(words)
#         top_10 = word_counts.most_common(10)
#         return top_10

# # 使用示例：
# top_10 = analyze_text('C:/Users/Administrator/Desktop/2024pythonstudy/readme2025.txt')
# print('Top 10 words by frequency:')
# for word, count in top_10:
#     print(f'{word}: {count}')


#分析一篇中文词频前10并去除数字标点符号
import os
from collections import Counter
from pdfminer.high_level import extract_text
from jieba import lcut, add_word
import re

def analyze_pdf(filename):
    # 提取PDF文本内容
    text = extract_text(filename)

    # 使用jieba分词处理中文文本
    words = lcut(text)

    # 去除数字、标点符号和冒号
    words = [word for word in words if not re.search(r'\d+', word)]
    words = [word for word in words if not re.search(r'[^\w\s]', word)]
    words = [word for word in words if ':' not in word]

    # 统计词频
    word_counts = Counter(words)

    # 获取出现次数最多的前50个单词
    top_50 = word_counts.most_common(50)

    return top_50

# 使用示例：
top_50 = analyze_pdf('C:/Users/Administrator/Desktop/2024pythonstudy/zxgblqj.pdf')
print('Top 50 words by frequency:')
for word, count in top_50:
    print(f'{word}: {count}')


