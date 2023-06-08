lst = [2, 3, 4, 1, 6, 7, 9, 3, 4]
print(lst)
minidx, maxidx = lst.index(min(lst)), lst.index(max(lst))
lst[maxidx], lst[minidx] = lst[minidx], lst[maxidx]
print(lst)