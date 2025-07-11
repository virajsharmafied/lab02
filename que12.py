d = {
    'a': [70, 80, 90],
    'b': [60, 75, 85],
    'c': [90, 88, 92]
}
for k in d:
    m = d[k]
    s = sum(m)
    print(k, "avg:", s / 3)
top = ''
high = 0
for k in d:
    s = sum(d[k])
    if s > high:
        high = s
        top = k
print("topper:", top)
x = input("name to update: ")
i = int(input("index to change (0/1/2): "))
v = int(input("new val: "))
d[x][i] = v
print("new marks for", x, ":", d[x])
