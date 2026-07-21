n = int(input("Enter the number: "))
num =[]
for i in range(n):
    e = int(input("Enter the element: "))
    num.append(e)
l = 0 
for r in range(len(num)):
    if num[r] != 0:
        num[r],num[l]=num[l],num[r]
        l+=1
print(num)