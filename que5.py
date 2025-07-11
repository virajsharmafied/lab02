a = list(map(int, input().split()))
r = []

for i in range(len(a)):
    x = a[i]
    p = 1
    if x < 2:
        p = 0
    else:
        for j in range(2, x):
            if x % j == 0:
                p = 0
                break
    if i % 2 == 0 or p == 1:
        r.append(x)
print(r)
