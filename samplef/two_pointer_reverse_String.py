s = "ameen"
s = list(s)

st = 0
end = len(s) - 1
while st <= end:
    s[st],s[end] = s[end],s[st]
    st += 1
    end -= 1

print(s)
res = ''.join(s)  
print(res)#
#EOP