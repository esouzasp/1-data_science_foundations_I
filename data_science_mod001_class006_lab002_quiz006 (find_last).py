# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

# my resolutions
def find_last(string, target):
    x = 0
    while string.find(target, x) >= 0:
        x = x + 1
    return x - 1

# udacity code
def find_last(s, t):
    last_pos = -1
    while True
        pos = s.find(t, last_pos + 1)
        if pos == -1
            return last_pos
        last_pos = pos

# ideal_mix
def find_last(string, target):
    last_pos = 0
    while string.find(target, last_pos) >= 0:
        last_pos = last_pos + 1
    return last_pos - 1

print find_last('aaaa', 'a') #>>> 3
print find_last('aaaaa', 'aa') #>>> 3
print find_last('aaaa', 'b') #>>> -1
print find_last("111111111", "1") #>>> 8
print find_last("222222222", "") #>>> 9
print find_last("", "3") #>>> -1
print find_last("", "") #>>> 0
