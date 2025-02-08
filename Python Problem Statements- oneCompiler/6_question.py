'''

Question 6
Max Score: 2 | Difficulty: Not Specified
Take two arrays, merger them and store it as a third array. Print it out.

Constraints:
0 <= A[i] <= 1000;
0 <= B[j] <= 1000;
0 < i,j <= 100

Input:
Two integer arrays, each in a new line
Output:
A single array containing all the elements in first array and the second array.

Example:
Input:
1,2
3,4
Output:
1,2,3,4
'''
arr1 = list(map(int,input().split(",")))
arr2 = list(map(int,input().split(",")))

# print(arr1)
# print(arr2)
arr1.extend(arr2)
# print(arr1)
res = ",".join(map(str,arr1))
print(res)