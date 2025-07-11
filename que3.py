s = input("enter text: ").split()
w = []
c = []
for i in s:
    if i not in w:
        w.append(i)
        c.append(s.count(i))
for i in range(len(w)):
    print(w[i], "-", c[i])
