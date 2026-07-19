def twosum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
def main():
    n = int(input("Enter the number of elements: "))
    lst = []
    for j in range(n):
        x = int(input(f"Enter element {j+1} :"))
        lst.append(x)
    t = int(input("Enter the target element: "))
    r = twosum(lst,t)
    print("Required index: ",r)

k = 'y'
while k == 'y' or k == 'Y':
    if __name__ == "__main__":
        main()
    k = input("Do you want to continue?(y/n): ")
