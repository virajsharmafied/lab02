d = {}
while True:
    print("\n1 add")
    print("2 view")
    print("3 topper")
    print("4 search")
    print("5 failed")
    print("6 update")
    print("7 quit")
    
    x = input("opt: ")
    
    if x == "1":
        r = input("roll: ")
        n = input("name: ")
        s = list(map(int, input("marks: ").split()))
        d[r] = [n, s]
    
    elif x == "2":
        for r in d:
            print("roll:", r)
            print("name:", d[r][0])
            print("marks:", d[r][1])
            print("avg:", sum(d[r][1]) / len(d[r][1]))
            print()
    
    elif x == "3":
        m = 0
        t = []
        for r in d:
            a = sum(d[r][1]) / len(d[r][1])
            if a > m:
                m = a
                t = [r]
            elif a == m:
                t.append(r)
        for r in t:
            print("topper:", d[r][0], "| roll:", r, "| avg:", m)
    
    elif x == "4":
        r = input("roll to find: ")
        if r in d:
            print("name:", d[r][0])
            print("marks:", d[r][1])
        else:
            print("not found")
    
    elif x == "5":
        for r in d:
            f = False
            for m in d[r][1]:
                if m < 40:
                    f = True
            if f:
                print("failed:", d[r][0], "| roll:", r)
    
    elif x == "6":
        r = input("roll to update: ")
        if r in d:
            print("old marks:", d[r][1])
            i = int(input("sub idx: "))
            v = int(input("new mark: "))
            d[r][1][i] = v
            print("updated:", d[r][1])
        else:
            print("not found")
    elif x == "7":
        break
