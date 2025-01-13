#Data structures: "efficient way of storing data in repective memory location"
'''
1. List or Dynamic Array: [10,20,30,40]
2. Tuple: (10,20,30,40)
3. Set: {10,20,40}
4. Dictionary: {'Apple':10,'Banana':3,'Orange':2}
'''

#List/Dynamic Array: "Sequence collection of mix data/item within the Square brackets"


#Emplty list
l = []
print(type(l))#<class 'list'>
l = list()
print(type(l))#<class 'list'>


#collection of mixed data
l = [10,20,30]
print(l)#[10, 20, 30]
l = [10,'a','alen',5.34,[11,22,33],(10,20,30),{10,20}]
print(type(l))#<class 'list'>
print(l)


#concatination('+')
l1 = [10,20,30]
l2 = [40,50]
print(l1+l2)#[10, 20, 30, 40, 50]


#length of list(len() method)
l = [1,2,3,4,5]
print(len(l))


#Replication ('*')
l = [10,20,30]
print(l*3)#[10, 20, 30, 10, 20, 30, 10, 20, 30]

#membership('in' and 'not in')
#binary search
arr = [10,20,30,40]
print(55 in arr)#False
print(20 in arr)#True

print(55 not in arr)#True
print(20 not in arr)#False



#Index('[]')
arr = [11,22,33,44,55]
print(arr[2])#33
print(arr[-1])#55


#slicing[start:end-1]
arr = [10,20,30,40,50]
print(arr[0:3])#[10, 20, 30]
print(arr[1:3])#[20,30]
print(arr[0:-1])#[10, 20, 30, 40]
#special case: reverse the array
print(arr[::-1])#[50, 40, 30, 20, 10]


#iteration of list/array
arr = [100,200,300,400,500]
for i in arr:
    print(i)
'''
output:
100
200
300
400
500
'''
print("---")
for i in range(0,len(arr)):
    print(arr[i])
    
#-----
for i in arr:
    print(i, end=" ")
print("----")
arr2 = ['Apple','Mango','banana','grapes']
print(type(arr2))
print(len(arr2))#4
for i in arr2:
    print(i, end=" ")
print()
#Ways to insert/Adding items into the array/list
'''
1. append
2. insert
3.extend
'''
#1.append: adding/inserting element at the end
l = [10,20,30,40]
l.append(50)
print(l)#[10, 20, 30, 40, 50]
l.append(5)
print(l)#[10, 20, 30, 40, 50, 5]


#2.insert(pos,ele)
l = [10,20,30,40]
l.insert(1,15)
print(l)#[10, 15, 20, 30, 40]
l.insert(0,5)
print(l)#[5, 10, 15, 20, 30, 40]


#3.extend: ita an extendtion or concatination of array
l = [10,20,30]
l2 = [11,22]
l.extend(l2)
print(l)#[10, 20, 30, 11, 22]
# print(l+l2)

#Deleting/Removing the array item 
'''
1.pop()
1.1 pop(index_number)
2.remove(ele)
3.clear
4. del
'''
l = [11,22,33,44,55]
#1.pop(): remove the last element/item
l.pop()
print(l)#[11, 22, 33, 44]


#2.remove(ele)
l = [11,22,33,44,55]
l.remove(33)
print(l)#[11, 22, 44, 55]
#remove fist item
l.pop(0)
print(l)#[22, 44, 55]

l.pop(1)
print(l)

#3.clear

l = [1,2,3,4,5]
l.clear()
print(l)#[]

#4. del
l = [10,20,30]
# del l
# print(l)



#Sorting: arranging elment/item in ascending or decending order
l = [3,9,6,3,1,2]
l.sort()
print(l)#[1, 2, 3, 3, 6, 9]
l.sort(reverse=True)
print(l)#[9, 6, 3, 3, 2, 1]



#reverse
arr = [1,2,3,4]
print(arr[::-1])#[4, 3, 2, 1]
arr.reverse()
print(arr)#[4, 3, 2, 1]


#copy

l1 =[1,2,3]
l2 = l1.copy()
print(l2)#[1, 2, 3]

#count: to check frequency/occurence of the item
l = [10,20,20,20,30]
print(l.count(20))

#list comprehension(**)

arr = [10,20,30,40]
for i in arr:
    print(i)
    
ans = [i for i in arr]
print(ans)#[10, 20, 30, 40]



#1 to 10
ans = [i for i in range(1,11)]
print(ans)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print 3 table from 1 to 10
ans = [i*3 for i in range(1,11)]
print(ans)


#print all even number from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i,end=" ")
print()
#or
ans = [i for i in range(1,11) if i%2==0]
print(ans)

#sum()
arr = [100,1,2,3,4,5]
print(sum(arr))#115

print(min(arr))#1
print(max(arr))#100

print("---------------------TUPLE-------------------")
#Tuples: "sequencial collection of mix data/item within the ()"
#empty Tuple
t =()
print(type(t))#<class 'tuple'>
t = tuple()
print(type(t))


t = (10,20,30,"saniya","gulfam","5.19",[11,22])
print(type(t))#<class 'tuple'>


#NOTE: List are mutable(can change/modify)
l = [10,20,30,40]
l[1] = 200
print(l)#[10, 200, 30, 40], here we can able to change the item=> mutable


#Note: Tuple is immutable(can't be chnaged/modify)
t = (11,22,33,44)
print(t[1])
# t[1] = 2000
# print(t)#Immutable, Note: we can't change item


#concatination
t1= (1,2,3)
t2 = (4,5,6)
print(t1+t2)#(1, 2, 3, 4, 5, 6)

#replitation
print(t1*2)#(1, 2, 3, 1, 2, 3)

#lenght
print(len(t1))#3

#membership: (in, not in)
t = (10,20,30)
print(50 in t)#False
print(20 not in t)#False
print(20 in t)#True

#NOTE: accessing item(indexing, slicing), sorting, reverse are also same in tuple similar to list

t = (10,20,30)
print(len(t))


#count: frequency of item
t = (10,20,30,20,20,20,20,30)
print(t.count(20))#5


#set: "its an unorder unique collection of mixed item enclosed within the {}"

s = {10,20,30,40,50,60,70}
print(type(s))#<class 'set'>

print(s)#{50, 20, 70, 40, 10, 60, 30}

s = {10,20,20,20,30,30,100}
print(s)#{10, 100, 20, 30}

print(type(s))

#add an item
s = {1,2,3,4}
s.add(100)
print(s)#{1, 2, 3, 100, 4}
# print(s[1])#No indexing in set


s.remove(2)
print(s)#{1, 3, 100, 4}


s1  = {1,2,3}
s2 = {2,3,5,6}

res = s1.union(s2)
print(res)#{1, 2, 3, 4, 5, 6}

#intersection
print(s1.intersection(s2))#{2, 3}

#diffrence
print(s1.difference(s2))#{1}

# #del
# del s1


print(len(s1))#3

s4 = {1,1,1,1,2,2}
print(len(s4))#2

#dictionary: collection of key and value pair item within the {}
d = {"Apple":10,"mango":5}
print(type(d))#<class 'dict'>


a ={}
print(type(a))#<class 'dict'>
#how to create emplty set
s = set()
print(type(s))

#empty dictionary
d = {}
d = dict()


d = {"Apple":10,"mango":5}
print(len(d))
print(d['mango'])#5
print(d['Apple'])

#add pairs
d['orange'] = 10

print(d)
#to print keys
print(d.keys())
#values
print(d.values())
#comlete items
print(d.items())

#Inteview

d = {"Apple":10,"mango":5}
print(d['mango'])#5
print(d.get('mango'))#5

# print(d['grapes'])#Error
# print(d.get('grapes'))#None

print(d.get('grapes',0))


#to delete item(pair) from dictionary
d = {"Apple":10,"mango":5,'grapes':80}
# del d['mango']
# print(d)#{'Apple': 10, 'grapes': 80}

d2 = {'orange':11}
d.update(d2)
print(d)#{'Apple': 10, 'mango': 5, 'grapes': 80, 'orange': 11}

#iteration/looping

d = {"Apple":10,"mango":5,'grapes':80}
for kgulam,valen in d.items():
    print(kgulam, end=" ")
print()
for k,v in d.items():
    print(k,v)

#iterating keys
for i in d:
    print(i)
#iterate values
for i in d:
    print(d[i])
    
    
    
#OOPS(100% iterview question)
#"Implementation of program is done using class and objects."
'''
1.class and object
2.constructors
3.scope of variables
4.inheritence
5.polymorphism
6.Encapsulation
7.Abstraction
'''
#1.class and object
#class: "class are nothing but templates/blue print by which object followes"
#"it a collection of attritube/instance variable and method"
'''
syntax of class

class ClassName:
    #instance variable
    #methods(self)

'''

def myfunc():
    print(10+100)
myfunc()#110

class Student:
    #instantance variable
    name = "saniya"
    classs = "MCA"
    marks = 95
    #method
    def student_details(self):
        print(f"Name of student: {self.name} and class is {self.classs} and marks is: {self.marks}%")

#Object:  "its an instance of class"
#NOTE: selt: it is an argument that class itself
obj = Student()
print(obj.name)#saniya
print(obj.marks)#95
obj.student_details()

class StudentGulfam:
    #instantance variable
    name = "gulfam"
    classs = "BE"
    marks = 95
    #method
    def student_details(self):
        print(f"Name of student: {self.name} and class is {self.classs} and marks is: {self.marks}%")
obj_g = StudentGulfam()
obj_g.student_details()


#2.constructors: "it is used to initialize the instance variables"

class AllStudents:
    #constructor
    def __init__(self,name,marks,usn):
        self.name = name
        self.marks = marks
        self.usn = usn
        
    def student_details(self):
        print(f"Student Name: {self.name} | Marks: {self.marks} | Usn: {self.usn}")

s1 = AllStudents("Alen",90,"MSR02CS01")
s1.student_details()

s2 = AllStudents("Gulfam",98,"CS02")
s2.student_details()
#note: I can create n- object for single class


class MyStudent:
    def student_d(self,name,usn):
        print(f"name: {name} and usn:{usn}")
obj = MyStudent()
obj.student_d("Aleen","CS01")
obj.student_d("bob","cs02")


#Scope of Variable
'''
1. Global variable
2. Local variable
3. Instance variable
'''
#global variable
n = 100000
class DemoClass:
    #instance variable
    n = 100
    def myfunc(self):
        #local variable
        n = 1000
        print(n)
print(n)#100000
obj = DemoClass()
print(obj.n)#100
obj.myfunc()#1000



#global variable
n = 100000
class DemoClass:
    #instance variable
    n = 100
    def myfunc(self):
        #local variable
        n = 1000
        print(n)
        print(f"instance variable: {self.n}")
obj = DemoClass()
obj.myfunc()