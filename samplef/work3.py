def twosum(arr,sum_target):
    seen = set()
    for i in arr:
        if i not in seen:
            composite = sum_target - i
        else:
            seen.add(i)
    
arr = [2,5,7,10,15]
sum_target = 9
print(twosum(arr))