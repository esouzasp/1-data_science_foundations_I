
elements = {}
elements ['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elements ['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602, 'noble gas': True}

print elements
print elements['H'] #not use upper case generate error
print elements['H']['weight']
#print elements['H']['noble gas'] # error, does not exist
print elements['He']['noble gas']
