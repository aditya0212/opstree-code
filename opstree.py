num = []

n = int(input())

for i in range(0, n):
    nus = int(input())
    num.append(nus)
print (num)
    
last = num[::-1]
print (last)
    
for i in range(0, n):
    for j in range(i+1, n):
        if num[i] >= num[j]:
            num[i], num[j] = num[j], num[i]
print (num)

for i in range(0, n):
    for j in range(i+1, n):
        if num[i] <= num[j]:
            num[i], num[j] = num[j], num[i]
print (num)

search = int(input())
if search in num:
    print ("searched number is in list")
else:
    print ("searched number is not in list")
