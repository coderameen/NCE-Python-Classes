''''

Question 4
Max Score: 2 | Difficulty: Not Specified
Take n elements into an array and print the odd numbers and even numbers seperately in two lines.

Constraints:
0 <= arr[i] <= 1000 ; 0<=i<=9

Input:
First line of input contains n, the number of elements in the input array
Next n lines contain elements of the array of n integers, each in a new line.
Output:
First line of output contains all the odd numbers in the input array, seperated by a comma
Second line of output contains all the even numbers in the input array, seperated by a comma

Example:
Input:
11
23
233
212
250
590
231
553
678
900
100
101

Output:
23,233,231,553,101
212,250,590,678,900,100

'''
size = int(input())
arr =[]
for _ in range(size):
  arr.append(int(input()))
  
odd = []
even = []

for i in arr:
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)

# print(odd)
# print(even)

# #ip: [10,20,30,40,50]
# #op 10,20,30,40,50

odd_res = ",".join(map(str,odd))
print(odd_res)
even_res = ",".join(map(str,even))
print(even_res)