


# quiz_002
# which of the following procedures
# leaves the value passed in as the input unchanged?

# opt_001 (do not keep same value)
def proc1(p):
    p[0] = p[1]

# opt_002 (do not keep same value)
def proc2(p):
    p = p + [1] #concatenating

# opt_003 (keep same value)
def proc3(p):
    q = p
    p.append(3)
    q.pop()

# opt_004 (keep same value)
def proc4(p):
    q = []
    while p:
        q.append(p.pop())
    while q:
        p.append(q.pop())
