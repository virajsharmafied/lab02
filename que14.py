p = {}
while True:
    x = input("add / upd / rng / q: ")
    if x == "add":
        n = input("name: ")
        v = int(input("price: "))
        p[n] = v
    elif x == "upd":
        n = input("name: ")
        if n in p:
            v = int(input("new price: "))
            p[n] = v
        else:
            print("not found")
    elif x == "rng":
        a = int(input("min: "))
        b = int(input("max: "))
        for k in p:
            if a <= p[k] <= b:
                print(k, p[k])
    elif x == "q":
        break

