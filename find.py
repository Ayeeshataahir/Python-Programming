t2=['a','b','c']
t1=['e','d']
t2.extend(t1)
t2.sort()
print(t2)
#x=t1.pop(0)
#print(x)
t1.remove('d')
print(t1)
del t2[0:5]
print(t2)
