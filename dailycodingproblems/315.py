# Verify if the given matrix is a 
# Toeiplitx Matrix or not.

# Create a squared matrix and validate


def validate_matrix(matrix):
    #1. Calculate the breadth of matrix
    #2. Calculate the length of matrix
    #3. see which one is greater start with that value
    
    r = len(matrix)
    c = len(matrix[0])
    lr , tb = 0,0
    s = 0
    
    if c > r:
	    lr = c-r
	    s = r
    else:
        tb = r-c
        s = c

    for 


def check_matrix(mtx):
    l = len(mtx)
    val = mtx[0][0]
    for i in range(l-1):
        if val != mtx[i][i]:
            return False
    return True

def main():
    mtx = [[1,2,3], [3,1,2], [2,3,1], [1,2,3]]
    assert(check_matrix(mtx)==True)
    pass


if __name__ == "__main__":
    main()
