y = {'cijo': 40, 'anusha': 2, 'bobins': 1, 'dev': 3}
l = list(y.items())
l.sort()
print('Ascending order is', l)
l = list(y.items())
l.sort(reverse=True)
print('Descending order is', l)

dict = dict(l)

print("Dictionary", dict)