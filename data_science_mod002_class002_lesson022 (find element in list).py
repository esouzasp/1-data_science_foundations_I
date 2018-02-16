# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# method_001
def find_element(p, q):
    count = -1
    for e in p:
        count = count + 1
        if e == q:
            return count
    return -1

# method_002
def find_element(p, q):
    count = 0
    for e in p:
        if e == q:
            return count
    count = count + 1
    return -1

#tests

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

print find_element(['flower', 'petal', 'tree', 'grass'], 'flower')
#>>> 0
