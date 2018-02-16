# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

## method_001
def is_friend(name):
	return name[0] == 'D' or name[0] == 'F'

## method_002
def is_friend(name):
	if name[0] == 'D':
		return True
	else:
	if name[0] == 'N':
		return True
	else:
		return False

## method_003
def is_friend(name):
	if name[0] == 'D' or name[0] == 'N':
		return True
	else:
		return False

## exercise
print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False
