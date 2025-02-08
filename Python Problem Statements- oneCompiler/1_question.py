'''Question 1
Max Score: 2 | Difficulty: Not Specified
Take 10 elements in an array and find the sum of all elements.

Constraints:
0 <= arr[i] <= 1000 ; 0<=i<=9

Input:
An array of 10 integer elements, each in a new line.
Output:
A single integers obtained when all the array elements are added.

Example:

Input:
1
2
3
4
5
1
2
3
4
5
Output
30

'''
#Method 1
arr = []
for _ in range(10):
  arr.append(int(input()))
# print(arr)
# sum = 0
# for i in arr:
#   sum = sum + int(i)
# print(sum)
print(sum(arr))