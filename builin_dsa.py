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
