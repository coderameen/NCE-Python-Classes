#Fding the give sum in subarray dasf 
def kadane(arr,x):
    n = len(arr)
    pre = arr[0]
    ans = arr[0]
    for i in range(len(arr)):
        curr = max(pre+arr[i],arr[i])
        ans = max(ans,curr)
        pre = curr
    return ans

arr = [2,3,4,-3,5]
x = 1
print(kadane(arr,x))