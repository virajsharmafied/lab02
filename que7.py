n = int(input("how many points? "))
p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))
x0, y0 = p[0]
x1, y1 = p[1]
dx = x1 - x0
dy = y1 - y0
ok = True
for i in range(2, n):
    xi, yi = p[i]
    dx2 = xi - x0
    dy2 = yi - y0
    if dx * dy2 != dy * dx2:
        ok = False
        break
if ok:
    print("yes")
else:
    print("no")