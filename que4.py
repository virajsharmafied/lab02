a = []
while True:
    x = input("ps / pp / enq / deq / q: ")
    if x == "ps":
        y = input("val: ")
        a.append(y)
    elif x == "pp":
        if a:
            print("pop:", a.pop())
    elif x == "enq":
        y = input("val: ")
        a.insert(0, y)
    elif x == "deq":
        if a:
            print("deq:", a.pop())
    elif x == "q":
        break
