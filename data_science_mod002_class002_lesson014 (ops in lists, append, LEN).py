# <list>.append(<element>)
# add a new element
stooges = ['Moe','Larry','Curly']
stooges.append('Shemp')
print stooges
print len(stooges)

# plus "+", is similar to concatenation
# <list> + <list>

# len(<list>) number of elements (lists, strings)

list001 = [0,1] + [2,3]
print list001
print len(list001) # elements = lists

print len (stooges[0]) # elements = letters
print len (stooges[1])
print len ('udacity')

#quiz_016
p = [1, 2]
p.append(3)
p = p + [4, 5]
len(p)

#quiz_017
p = [1,2]
q = [3,4]
p.append(q)
print len(p)
# p = [1,2,[3,2]]
# len = 4
