l = [1, [2, 3], 4]
print('List:', l, '\nLength:', len(l))
print('Concat:', l + [5, 6])
print('3 in list:', 3 in l)
for i in l: print('Iter:', i)
print('Index 1:', l[1], '\nSlice:', l[1:])

l.append(5)
l.extend([6, 7])
l.insert(1, 'a')
del l[2]
print('Modified List:', l)

