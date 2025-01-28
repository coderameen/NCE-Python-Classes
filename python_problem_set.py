#sum of n natural number:
#method 1
#WAP to find sum on n number:
'''
ip: n=10
op: 55
'''
# n = 10
# sm = 0
# for i in range(1,n+1):
#     sm += i#sm = sm + i #136......
# print("the tolal sum is: ",sm)


#method 2:(direct) n(n+1)/2
# def mysum(n):
#     return n*(n+1)/2
# n = int(input("Enter the number: "))
# res = mysum(n)
# print(int(res))


#Q2: Count Digits
'''
ip: x = 9253
op:4

ip: x = 38
op: 2


ip:7
op:1

idea: divide given no. by 10 until no. becomes 0

'''
# print(9253//10)#925
# print(925//10)#92
# print(92//10)#9
# print(9//10)#0

# x = int(input())
# cnt = 0
# while x>0:
#     x = x//10
#     cnt += 1
# print("The count of digits is: ",cnt)


#Q3: Palindrome of string:
name = "malayalam"
if name == name[::-1]:
    print(True)
else:
    print(False)
    
def panlindromeString(name):
    if name == name[::-1]:
        return True
    else:
        return False
 
name = "malayalam"
print(panlindromeString(name))#True

#Palindrome Number: given number is same, when we read left to right and right to left
'''
ip: n = 78987
op: True

ip:21
op:False

idea:
1. lastdigit = n%10,#take last digit from n
2.rev = rev * 10 + lastdigit
3.n = n//10
'''
# n = 12345
# rev = 0
# origin_n = n
# while n>0:
#     lastdigit = n%10
#     rev = rev * 10 + lastdigit
#     n = n // 10
    
# if rev == origin_n:
#     print("True")
# else:
#     print("False")


#Q4: Factorial of a number
'''
ip: n=4
op: 24

ip:n =5
op: 120


idea: traverse from 1 to n
2.fact = fact * i (fact *= i)
'''
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    
    return fact

n = 5
print(fact(n))#120
print(fact(4))#24

#Q5: Check Prime number or not
#Prime Number: A nubmer which is divisiable only by 1 and number itself, then it is know as prime number
'''
ip: n= 13
op: True

ip:14
op: False

ip: 101
op: True

'''


def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
    
    
print(isPrime(5))#True


#Q6: Finde the OCccurance of the number/element
arr = [10,20,30,30,30,40,40]
#Given an array. find the occurance/frequency of number
'''
n = 30
op: 3

n = 40
op: 2

n = 11
op: 0

'''
def freq(n,arr):
    if n in arr:
        res = arr.count(n)
        return res
    else:
        return 0


arr = [10,20,30,30,30,40,40]
print(freq(30,arr))

#method 2

arr = [10,20,30,30,30,40,40]
n = 40
cnt = 0
for i in range(len(arr)):
    if arr[i] == n:
        cnt += 1
print(f"The total occurance of number is: ",cnt)


#Q6: Seperate even and odd
#Given a array, we need to write a function and return two array, 1st array contain all even items and 2nd array should contains all odd items
'''
ip:arr = [10,41,30,15,80]
op: even = [10,30,80]
    odd = [41,15]


ip: arr = [10,30,40]
op: even = [10,30,40]
    odd = []
'''

def getEvenOdd(arr):
    even = []
    odd = []
    for i in range(len(arr)):
        if arr[i]%2 ==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    return even,odd

arr = [10,41,30,15,80]
even,odd = getEvenOdd(arr)
print(even)
print(odd)


#Q7: Find the largest item from the array, without using builtin methods
arr = [10,30,50,60,25,15,1]
# print(max(arr))#60
# print(min(arr))#1


def largeEle(arr):
    lg = 0
    for i in range(len(arr)):
        if arr[i] > lg:
            lg = max(lg,arr[i])
    return lg


arr = [10,30,50,60,25,15,1]
print(largeEle(arr))#60


def smallEle(arr):
    lg = float('inf')#infinite
    for i in range(len(arr)):
        if arr[i] < lg:
            lg = min(lg,arr[i])
    return lg


arr = [10,30,50,60,2,25,15,11,36]
print(smallEle(arr))#


#Q8: return the list of vowels from given string
'''
Vowels: 'a','e','i','o','u'
ip: s= "saniyasyeda"
op: ['a',i,a,e,a]

'''
def myvowels(s):
    arr = []
    for i in s:
        if i in ['a', 'e','i','o','u']:
            arr.append(i)
    return arr     

s = "saniyasyeda"
print(myvowels(s))