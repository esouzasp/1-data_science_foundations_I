elements = {'hydrogen': 1,
            'helium': 2,
            'carbon': 6}

print elements
print elements['hydrogen']
print elements['carbon']
#print elements['lithium'] #keyError
print 'lithium' in elements
elements['lithium'] = 3 #add new+value
elements['nitrogen'] = 8 #add new+value
print elements
elements['nitrogen'] = 7
print elements
print elements['nitrogen']
