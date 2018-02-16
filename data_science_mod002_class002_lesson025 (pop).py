# mutates the list, removing the last element,
# also returning this value to the new variable

a = [1,2,3]
b = a
print a
print b

x = a.pop()
print a
print b
print x

# quiz
print '### codes tests ###'
# 'p' original
p = [1,2]
print p
print '-------------------'

# code_001
p = [1,2]
p.append(3)
p.pop() # just remove
print p

# code_002
p = [1,2]
x = p.pop()
y = p.pop()
p.append(x)
p.append(y)
print p

# code_003
p = [1,2]
x = p.pop()
p.append(x)
print p

# code_004
x = p.pop()
y = p.pop()
p.append(y)
p.append (x)
print p
