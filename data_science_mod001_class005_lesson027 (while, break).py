# break


i = 1
while i <= n:
    if i > n:
        break
    print i
    i = i + 1

#exercise -----
## option_001 (CORRECT)
def test001 (x):
    while x < 10:
        if False:
            break
        print x
        x = x + 1

## option_002 (ERROR)
def test001 (x):
    while x < 10:
        print x
        x = x + 1
        break

## option_003(ERROR)
def test001 (x):
    while True:
        if x < 10:
            break
        print x
        x = x + 1


## option_004(CORRECT)
def test001 (x):
    while True:
        if x < 10:
            break
        print x
        x = x + 1

#---------------------
print test001(1)
