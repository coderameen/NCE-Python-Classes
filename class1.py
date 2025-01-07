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
n1 = input("enter n1: ")
n2 = input("enter n2: ")
print(int(n1) + int(n2))