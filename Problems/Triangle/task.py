height = int(input())

for i in range(0, height * 2, 2):
    print(("#" * (i + 1)).center(height * 2))
