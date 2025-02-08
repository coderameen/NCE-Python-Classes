'''

Question 2
Max Score: 2 | Difficulty: Not Specified
Take 10 elements in an array (arr) and find the second biggest number.

Constraints:
0 <= arr[i] <= 1000 ; 0<=i<=9

Input:
An array of 10 integers, each in a new line.
Output:
A single integer which is the second maximum number among the array elements

Example:
Input:
1
2
1
3
4
5
2
11
12
2
Output:
11

'''
arr = []
for _ in range(10):
  arr.append(int(input()))


arr.sort()

print(arr[-2])