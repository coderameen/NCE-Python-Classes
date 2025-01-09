#Variable: it is a container that stores the data in respective memory loaction
name = "saniya"
age  = 20
#type of ways to print
print("helloolll")
print("The Student name is: ",name, " and the age is: ",age)
print(f"The Student name is: {name} and age is {age}")
print("The student name is {1} and age is {0}".format(age,name))
print("the sudent is: {} and age is {}".format(name,age))


#to check type of data
name = "gulfam"
print(type(name))#<class 'str'>
age = 24
print(type(age))#<class 'int'>
height = 5.10
print(type(height))#<class 'float'>
mybool = True
print(type(mybool))#<class 'bool'>


#add two number
num1 = 10
num2 = 40
# print(num1 + num2)
result = num1 + num2
print(result)
print(f"The total sum is {result}")

#add the two number taking user input
#input()
n1 =20
n2 =50
# n1 = int(input("enter first number"))
# n2 = int(input("enter second number"))
print(n1 + n2)#2040 #it is concatinating
print(type(n1))#<class 'str'>
print(type(n2))#<class 'str'>

print("hi  " + "alen")#hialen
# n1 = input("enter n1: ")
# n2 = input("enter n2: ")
# print(int(n1) + int(n2))


#Operators:
#single line command
'''
multi 
line 
command
'''
#Operators in python
'''
1.Arthematic operat5or
2.Relational operator
3.Logical operator
4.Assignment operator
5.Swift operator
'''
#1.Arth operator: +, -, *,/,//,%

print(10+50)#60
print(10*2)#20
print(10-5)#5
print(10/2)#5
print(10//2)#5
print(10%2)#0

#2.relational operator: >,<,>=,<=,==,!=
n1 = 10
n2 = 30
n3 = 20
n4 = 20
print(n1 > n2)#False

print(n2 > n3)#True
print(n3 >= n4)#True
n3 = 20
n4 = 20
print(n3 == n4)#True
print(n3 != n4)#False

#3.Logical operator: and, or,not, in
a = 10
b = 30
c=  40
print(a==10 and b == 30 and c==40)
print(a==100 or b == 300 or c==4000)


#4.Assignment operator, = , +=, -=,*=,/=,%=
alen_marks = 98
print(alen_marks)

summ = 2
n = 10
# summ = summ + n#summ+=n
# print(summ)
# summ+=n# summ = summ + n
# print(summ)
summ = 2
n = 10
summ *= n#summ = summ * n
print(summ)#summ = 20


summ += 5
print(summ)#25

summ -= 10
print(summ)

#***5.Swift operator: >>(right swift), <<(left swift)
print(32>>3)#4
print(16<<1)#32


#Statements in python
'''
1.Conditional statement
2.unconditional statement
3.iterative/looping statement
'''

#1.Conditinal statement: if, elif, else
'''
syntax
if condition:
    stement execution
'''
age = 25
if age >= 18:
    print("he will get DL")
    
    
#if else
age = 25
if age >=18:
    print("He will get the DL")
else:
    print("He don't get the DL")
    
#elif
a = 10
b = 20
c = 30
#Program to check greater of 3 number
if a>b and a>c:
    print(f"{a} is greater")
elif b>a and b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
    
    
#2.unconditional statement: continue, break
#continue:(skipping)
#1 to 10 except 5
for i in range(1,11):
    # print(i)
    if i == 5:
        continue
    print(i)
print("----")
#5 to 10 except 7
for i in range(5,11):
    if i == 7:
        continue
    print(i)
    
print("---break----")
#break(termination/Stop/end)
#1 - 10 if 5 encounter terminate iteration
for i in range(1,11):
    if i == 5:
        break
    print(i)





#3.iterative statement(looping statement): for, while
#NOTE: We don't have 'do while' loop in python***

#WAP to print 1 to 10
'''
for variable in range(start_variable, end_variable - 1, steps):
    print(variable)
'''

for i in range(1, 11):
    print(i)
print("-----")

for i in range(11):
    print(i)
print("-----")
#5 - 10
for saniya in range(5,11):
    print(saniya)
print("--------")
#1-10(step: jump)
for i in range(1,10,3):
    print(i)
    
#1 to 10 using while loop
'''
initialization
while condition:
    statement execution
    increment
'''
print("----while loop---")
#5- 10
i = 5
while i<= 10:
    print(i)
    i+= 1



#Function in python: "it a block of code used to avoid dedundency/duplicacy of the code(we can reuse the code)"
'''
syntax:
def function_name():
    stement execution

'''
def func1():
    n1 = 10
    n2 = 20
    print(n1 + n2)
func1()
func1()
'''
4 type of function:
1.non parameterized non return function
2. parameterized return function
'''
#1.non parameterized non return function
def mysum():
    n1 = 10
    n2 = 100
    result = n1 + n2
    print(result)
mysum()   

#parameterized return function
def mysum2(a, b):
    n1 = a
    n2 = b
    result = n1 + n2
    return result
ans = mysum2(100,200)
print(ans)

def fun(a,b):
    return a+b

print(fun(10,900))

#defult argument
def fun(a,b=1000):
    return a+b

print(fun(10))

def fun(a,b=1000):
    return a+b

print(fun(10,50))#60


def fun(a=1000,b=1000):
    return a+b

print(fun())#2000


#Print all even number from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i)

#Print all odd number from 1 to 10
for i in range(1,11):
    if i%2!=0:
        print(i)