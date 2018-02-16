
danton = "De l'audace, encore de l'audace, toujours de l'audace"

def find_second(search, target):
    return search.find(target,search.find(target)+1)

print find_second(danton, 'audace')

#---------------------------

twister = "she sells seashells by the seashore"

def find_second(a,b):
    return a.find(b, a.find(b)+1)

print find_second(twister,'she')
