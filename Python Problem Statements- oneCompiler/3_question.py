'''



Question 3
Max Score: 2 | Difficulty: Not Specified
Take an array of 10 integers, print the number of array elements that are divisible by 5

Constraints:
0 <= arr[i] <= 1000 ; 0<=i<=9

Input:
An array of 10 integers, each separated by a comma.
Output:
An integer - denoting the count of elements in the array that are divisible by 5

Example:
Input:
1
2
3
4
5
6
7
8
9
10
Ouput:
2
'''
arr = []
for _ in range(10):
  arr.append(int(input()))

cnt = 0 
for i in arr:
  if i%5==0:
    cnt += 1 
    
print(cnt)