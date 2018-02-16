s = 'hello'
s = 'yello'
s = s + 'w'

p = ['h', 'e', 'l', 'l', 'o'] #each letter is a element
print p
p[0] = 'Y'
print p
p[4] = '!'
print p

# QUIZ
# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:
#['Moe','Larry','Shemp']

stooges[2] = 'Shemp'
print stooges

# but does not create a new List
# object.

#different
p = ['h', 'e', 'l', 'l', 'o']
p[0] = 'Y'
q = p #q refer the same object "p"
q[4] = '!'
print p
print q

#comparing stings and lists
s = 'Hello'
s[0] = 'Y' #TypeError: 'str' object does not support item assignment
