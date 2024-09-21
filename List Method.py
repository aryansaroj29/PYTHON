l = [112, 445, 1, 2, 1, 4, 6, 1]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(112))
print(l.count(1))
m = l.copy()
m [0] = 0
l.insert(2, 3456)
m = [1000, 2000, 3000]
k = l + m
print(k)
l.extend(m)
print(l)
