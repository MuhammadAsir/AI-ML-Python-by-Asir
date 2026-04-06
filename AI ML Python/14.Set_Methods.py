#Union and Intersection of Sets

a={1,2,3,4,5}
b={6,7,8}
print((a|b),'\n')#union of sets
#or print(a.union(b),'\n')

c={100,200,500,700,900}
d={400,600,800,100,200,300,500}
print((c&d),'\n') #intersection of sets
#or print(c.intersection(d),'\n')

e={1,2,3,4}
f={6,7,8}
print(e.isdisjoint(f),'\n') #disjoint of sets

print(e.issubset(a),'\n') #subset of sets

