astr = input()
astr = set(astr)
print(tuple(sorted(list(map(int, astr)))))
print(tuple(sorted(list(map(int, astr)), reverse=True)))