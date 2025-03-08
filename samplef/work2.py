Next Greater and Next Smaller Element using Stack
Question: https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1

Question: https://www.naukri.com/code360/problems/next-smaller-element_1112581


In this chapter, we will explore the concepts of the Next Greater Element (NGE) and Next Smaller Element (NSE) using a stack. We will learn how to efficiently find the next greater or smaller element for each element in an array, both from the left and right directions. Additionally, we will also determine the indexes and values of these elements.

Understanding these concepts is crucial for solving a wide variety of algorithmic problems, such as those involving stock span, temperature trends, and more.

Key Concepts:
- Next Greater Element (NGE): For each element in the array, the next greater element is the first element to the right that is greater than the current element.
- Next Smaller Element (NSE): For each element, the next smaller element is the first element to the right that is smaller than the current element.

The same logic applies for finding the Next Greater/Smaller Element from the left.

We will use a stack to efficiently track the elements and their indices while iterating through the array. The stack helps to maintain the order of elements and allows us to quickly find the next greater or smaller element in linear time.

Code Examples:
# code
1. Next Greater Element (NGE) from Right:
def next_greater_element(arr):
    stack = []
    nge = [-1] * len(arr)  # Initialize with -1 (indicating no NGE by default)
    
    for i in range(len(arr)-1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] <= arr[i]:
            stack.pop()  # Remove elements that are less than or equal to arr[i]
        
        if stack:
            nge[i] = stack[-1]  # The next greater element is at the top of the stack
        
        stack.append(arr[i])  # Push current element onto the stack
    
    return nge

arr = [4, 5, 2, 10, 8]
print("Next Greater Element (Right):", next_greater_element(arr))
# Next Greater Element (Right): [5, 10, 10, -1, -1]


2. Next Smaller Element (NSE) from Right:
def next_smaller_element(arr):
    stack = []
    nse = [-1] * len(arr)  # Initialize with -1 (indicating no NSE by default)
    
    for i in range(len(arr)-1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] >= arr[i]:
            stack.pop()  # Remove elements that are greater than or equal to arr[i]
        
        if stack:
            nse[i] = stack[-1]  # The next smaller element is at the top of the stack
        
        stack.append(arr[i])  # Push current element onto the stack
    
    return nse

arr = [4, 5, 2, 10, 8]
print("Next Smaller Element (Right):", next_smaller_element(arr))
# Next Smaller Element (Right): [2, 2, -1, 8, -1]


3. Next Greater Element (NGE) from Left:
def next_greater_element_left(arr):
    stack = []
    nge_left = [-1] * len(arr)  # Initialize with -1 (indicating no NGE by default)
    
    for i in range(len(arr)):  # Traverse from left to right
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()  # Remove elements that are less than or equal to arr[i]
        
        if stack:
            nge_left[i] = arr[stack[-1]]  # The next greater element is at the top of the stack
        
        stack.append(i)  # Push current index onto the stack
    
    return nge_left

arr = [4, 5, 2, 10, 8]
print("Next Greater Element (Left):", next_greater_element_left(arr))
# Next Greater Element (Left): [5, 10, 10, -1, -1]


4. Next Smaller Element (NSE) from Left:
def next_smaller_element_left(arr):
    stack = []
    nse_left = [-1] * len(arr)  # Initialize with -1 (indicating no NSE by default)
    
    for i in range(len(arr)):  # Traverse from left to right
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()  # Remove elements that are greater than or equal to arr[i]
        
        if stack:
            nse_left[i] = arr[stack[-1]]  # The next smaller element is at the top of the stack
        
        stack.append(i)  # Push current index onto the stack
    
    return nse_left

arr = [4, 5, 2, 10, 8]
print("Next Smaller Element (Left):", next_smaller_element_left(arr))
# Next Smaller Element (Left): [-1, 4, -1, 2, 2]


Key Points:
- By using stacks, the time complexity for finding the next greater or smaller element is reduced to O(n) from the brute-force O(n^2).
- The stack helps maintain an efficient lookup for the next element while traversing the array.

You can also return the indexes of the next greater or smaller elements by modifying the code to store indices in the stack rather than the elements themselves.