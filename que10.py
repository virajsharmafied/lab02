def f(s):
    v = "aeiou"
    r = set()
    for i in s.lower():
        if i in v:
            r.add(i)
    return r
x = input()
print(f(x))
