a = [0.56,0.71,0.48,0.56]
counts=[]
for i in a:
	counts.append(a.count(i))
print(counts)
print(counts.index(max(counts)))
print(a[counts.index(max(counts))])

