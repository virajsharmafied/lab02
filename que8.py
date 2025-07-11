c = set(map(int, input("cricket: ").split()))
f = set(map(int, input("football: ").split()))
a = set(map(int, input("all: ").split()))

print("both:", c & f)
print("only one:", c ^ f)
print("neither:", a - (c | f))
