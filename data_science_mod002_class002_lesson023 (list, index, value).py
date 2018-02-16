p = [0,1,2,76,4,7,6,454,657]

print p.index(76) #return the position
#print p.index(3) #generate an error

print 3 in p
print 1 in p
print 3 not in p
print 1 not in p

print '### string ###'
p = ['alpha','beta','gamma']
print 'beta' in p


#quiz
# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

## method_001
def find_element(p, q):
        if q in p:
            return p.index(q)
        else:
            return -1

## method_002
def find_element(p, q):
        if q not in p:
            return -1
        return p.index(q)

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
