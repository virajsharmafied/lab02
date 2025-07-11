import random
s = set()
while len(s) < 10:
    s.add(random.randint(1, 50))
print("all:", s)
s.remove(min(s))
s.remove(max(s))
print("after:", s)