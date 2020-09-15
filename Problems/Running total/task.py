numbers = [int(n) for n in input()]
s = 0
new_list = []
for n in enumerate(numbers):
    s += n[1]
    new_list.append(s)
print(new_list)
