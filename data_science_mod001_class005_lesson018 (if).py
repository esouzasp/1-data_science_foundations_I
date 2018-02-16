#execute: CTRL + SHIFT + P

#method_001
def bigger(x, y):
	if x < y:
		x = y
	return x

#method_002
def bigger(x, y):
	if x > y:
	return x
	return y

#method_003
def bigger(x, y):
	if x > y:
		return x
	else:
		return y

#method_004
def bigger(x, y):
	if x > y:
		r = x
	else:
		r = y
	return r

# exercise -----

print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3
