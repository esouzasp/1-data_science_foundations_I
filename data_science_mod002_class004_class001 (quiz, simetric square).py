# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(sy):

    x = 0
    y = 0
    z = []

    if sy != []:

        if len(sy) == len(sy[x]):

            while y < len(sy):

                z.append(sy[y][x] == sy[x][y])

                x = x + 1

                if x == len(sy):
                    x = 0
                    y = y + 1

            if False in z:
                return False
            else:
                return True

        else:
            return False

    return True





## Exercicio quad_sim

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]])
#>>> False


print symmetric([[1, 2],
               [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
               [2, 3, 4, 5],
               [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                [2,3,1]])
#>>> False
