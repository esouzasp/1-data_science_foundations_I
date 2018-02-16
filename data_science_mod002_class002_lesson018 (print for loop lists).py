p = [1,2,3,4,5,6,7,8,9,1,2,2,3,4,5,[67,4,33],56,6,43]

def print_all_elements(p):
    i = 0
    while i < len(p):
        print p[i]
        i = i + 1

print print_all_elements(p)

# for loop
# for <name> im <list>:
#   <block>

print '### second code ###'

def print_all_elements(p):
    for e in p: # each cycle 'e' assumes the current value element
        print e

print print_all_elements(p)

# e = name of the element in the list (changing)

# ------------------------
# quiz_020
print '### quiz code ###'

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

# my resolution
def sum_list(p):
    i = 0
    for e in p:
        i = i + e
    return i

print sum_list([1, 7, 4])
#>>> 12

#print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134
