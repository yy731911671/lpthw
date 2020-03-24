types_of_people = 10    #定义int型变量
x = f"There are {types_of_people} types of people."    #定义格式化字符串 同时引用变量

binary = "binary"   #定义字符串变量
do_not = "don't"    #同上
y = f"Those who know {binary} and those who {do_not}."  #定义格式化字符串 同时引用变量

print(x)    #输出格式化字符串
print(y)    #输出格式化字符串

print(f"I said: {x}")   #输出格式化字符串 此时第一个f是因为要在字符串中引用x变量
print(f"I also said: '{y}'")    #同上

hilarious = False   #定义bool型变量
joke_evaluation = "Isn't that joke so funny?! {}"   #定义字符串变量 此时中括号在用format函数时可以传入参数

print(joke_evaluation.format(hilarious))    #输出.format（）格式化的字符串 （）里可以传入一到多个变量，决定于引用变量里有几个传参位置

w = "This is the left side of..."   #定义字符串变量
e = "a string with a right side."   #同上

print(w+e)  #输出拼接后的字符串 利用➕相连
