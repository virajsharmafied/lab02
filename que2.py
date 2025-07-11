a = list(map(int, input("list 1: ").split()))
b = list(map(int, input("list 2: ").split()))
c = []

for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)

print("merged with no common:", c)
