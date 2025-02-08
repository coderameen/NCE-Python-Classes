'''


Question 7
Max Score: 2 | Difficulty: Not Specified
Take an array with several 0s in it, push all the 0s to the start of the array and print the array.

Constraints:
0 <= arr[i] <= 1000 ; 0<=i<=100

Input:
First line contains n, the size of array
Next n lines contain the elements of the array, each in a new line.
Output:
Input array, with all the 0s moved to the start, without changing the relative positions of other non-zero elements.

Example:
Input:
10
1
0
2
0
3
0
4
0
5
6
Output:
0
0
0
0
1
2
3
4
5
6

Explanation:
All the 0s have been moved to the start but the relative positions of other elements has not changed.
1 was positioned 2,3,4,5 and it is the same in the output.
'''
size = int(input())
arr = []
for _ in range(size):
  arr.append(int(input()))
  
zero = []
nonzero = []

for i in arr:
  if i==0:
    zero.append(i)
  else:
    nonzero.append(i)
    
# print(zero)
# print(nonzero)

zero.extend(nonzero)
# print(zero)

for i in zero:
  print(i)