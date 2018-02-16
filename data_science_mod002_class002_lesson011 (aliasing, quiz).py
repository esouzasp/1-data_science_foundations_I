p = ['J', 'a', 'm', 'e', 's']
q = p
p[2] = 'n'
p = [0,0,7]

print p
print q

#quiz_012
spy = [0, 0, 7]
agent = spy
print spy, agent
spy[2] = agent[2] + 1
print agent[2]

##quiz_013

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]
print spy

def replace_spy(var):
    var[2] = var[2] + 1
    return var

replace_spy(spy)
print spy

# In the test below, the first line calls your
# procedure which will change spy, and the
# second checks you have changed it.
# Uncomment the top two lines below.

#replace_spy(spy)
#print spy
#>>> [0,0,8]
