# 1 'always finishes'
# 2 'sometimes runs forever'
# 3 'unknown (to anyone)

# LOOP 001
    n = qualquer número inteiro
    i = 0
    while i <= n:
        i = i + 1

# LOOP 002
    n = qualquer número inteiro
    i = 1
    while True:
        i = i * 2
        n = n + 1
        if i > n:
            break

# LOOP 003
    n = qualquer número inteiro
    while n != 1:
        if n % 2 == 0: #n is even
            n = n/2
        else:
            n = 3 * n + 1

#answer:
# Loop 001: 1 'always finishes'
# Loop 002: 1 'always finishes' (i=exponentail, n=linear)
# Loop 003: 3 'unknown (to anyone)
