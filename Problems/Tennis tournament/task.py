winners = [s[0] for s in
           [input().split() for i in range(int(input()))]
           if s[1] == 'win']

print(winners)
print(len(winners))
