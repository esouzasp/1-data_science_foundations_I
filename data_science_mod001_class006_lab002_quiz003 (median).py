# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

# solution

def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    if big == c:
        return bigger(a,b)


print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7


# method_TRASH
def median(a, b, c):

    if a > b and a > c:
        Max = a

    if b > a and b > c:
        Max = b

    if c > a and c > b:
        Max = c


    if a < b and a < c:
        Min = a

    if b < a and b < c:
        Min = b

    if c < a and c < b:
        Min = c

    if a == Min or a == Max:
        r = 0
    else:
        return a

    if b == Min or b == Max:
        r = 0
    else:
        return b

    if c == Min or c == Max:
        r = 0
    else:
        return c
