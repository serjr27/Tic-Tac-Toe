# put your python code here
numbers = input().split()
num = input()
positions = [str(i) for i in range(len(numbers)) if numbers[i] == num]
if len(positions) != 0:
    print(" ".join(positions))
else:
    print("not found")
