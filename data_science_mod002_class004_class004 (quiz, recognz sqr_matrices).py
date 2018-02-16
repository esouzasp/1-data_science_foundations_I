# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def is_identity_matrix(matrix):

    x = 0
    z = []
    y = []

    if matrix != []:

        if len(matrix) == len(matrix[x]): #check square axis_x == axis_y

            while x < len(matrix): # loop until the max rows/elements

                z.append(matrix[x][x] == 1) # check diagonal is = 1

                for i in matrix[x]:
                    if i != 0:
                        y.append(i)

                x = x + 1

            if len(y) != len(matrix):
                z.append(False)

            if False in z: # check False in list 'z'
                return False
            else:
                return True

        else:
            return False

    return True


# Test Cases:
matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]


print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]

print is_identity_matrix(matrix7)
#>>>False

#T
#F
#F
#F
#F
#F
#F
