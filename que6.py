a = tuple(map(int, input().split()))
s = sum(a)
print("avg:", s / len(a))
b = sorted(a)
n = len(b)
if n % 2 == 1:
    print("med:", b[n//2])
else:
    print("med:", (b[n//2 - 1] + b[n//2]) / 2)
m = 0
v = 0
for i in b:
    if b.count(i) > m:
        m = b.count(i)
        v = i
print("mode:", v)
