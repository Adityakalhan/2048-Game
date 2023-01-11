import random
def start_game() :
    mat = [[0]*4 for i in range(4)] #initially there is a 4x4 matrix filled with 0
    return mat

def add_new_2(mat) :
    #generate random column and row in range(0-3)
    #if that place is empty then add a new random 2 in that grid place
    row = random.randint(0,3)
    column = random.randint(0,3)
    while mat[row][column] != 0 : #if the place isn't empty then we cannot add a new 2 there
        row = random.randint(0,3)
        column = random.randint(0,3)
    mat[row][column] = 2 #when finally we  get an empty position

def get_current_state(mat) : #3 states of game -i)won ,ii)lost,iii) on going

    for i in range(4) : #winning condition
        for j in range(4) :
            if mat[i][j] == 2048 :
                return "Won"
    
    # for ongoing, two conditions :
    #either there is a 0 present or a valid move

    for i in range(4) :
        for j in range(4) :
            if mat[i][j] == 0 :
                return "Game Not Over"
    
    for i in range(3) : #remaining last row and last column
        for j in range(3) :
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1] :
                return "Game Not Over"
    # i is fixed for last row       
    for j in range(3) :
        if mat[3][j] == mat[3][j+1] :
            return "Game Not Over"
    #j is fixed for last column 
    for i in range(3) :
        if mat[i][3] == mat[i+1][3] :
            return "Game Not Over"
    
    #since nothing else is possible, therefore we will return lost
    return "Lost"


#need to compress ie if the user does a left operation
#everything will move towards the left
def compress(mat) :
    changed = False
    new_mat = [[0]*4 for i in range(4)]
    for i in range(4) :
        pos = 0 
        for j in range(4) :
            if mat[i][j] != 0 :
                new_mat[i][pos] = mat[i][j]
                if j != pos :
                    changed = True
                pos += 1
    return new_mat,changed #all the 0s are on the right side, all the non zeros are on the left side of the row

def merge(mat) : #adding like numbers together
    changed = False
    for i in range(4) :
        for j in range(3) :
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0 :
                mat[i][j] *= 2
                mat[i][j+1] = 0
                changed = True
                
    return mat,changed

def reverse_mat(mat) :
    new_mat = []
    for i in range(4) :
        new_mat.append([])
        for j in range(4) :
            new_mat[i].append(mat[i][3-j])

    return new_mat

def transpose_mat(mat) :
    new_mat = []
    for i in range(4) :
        new_mat.append([])
        for j in range(4) :
            new_mat[i].append(mat[j][i])
    return new_mat

#we will use the same logic as left move for 
# compress, merge then again compress
#we can generalise this 

#for right
# reverse the matrix, then do the left operation
#then again reverse it

#for top
# transpose, then left operation
#transpose again

#for down moment
#transpose, then reverse, then left operation
#again reverse then transpose


def left_move(grid) :

    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    return new_grid,changed
def right_move(grid) :
    reverse_grid = reverse_mat(grid)
    
    new_grid,changed1 = compress(reverse_grid)
    new_grid,changed2 = merge(new_grid)
    new_grid,temp = compress(new_grid)
    
    changed = changed1 or changed2
    new_grid = reverse_mat(new_grid)
    return new_grid,changed

def up_move(grid) : 
    transposed_mat = transpose_mat(grid) 
    
    new_grid,changed1 = compress(transposed_mat)
    new_grid,changed2 = merge(new_grid)
    new_grid,temp = compress(new_grid)
    
    changed = changed1 or changed2
    new_grid = transpose_mat(new_grid)
    return new_grid,changed

def down_move(grid) :
    transposed_mat = transpose_mat(grid)
    reversed_mat = reverse_mat(transposed_mat)
    
    new_grid,changed1 = compress(reversed_mat)
    new_grid,changed2 = merge(new_grid)
    new_grid,temp= compress(new_grid)
    
    changed = changed1 or changed2
    new_grid = reverse_mat(new_grid)
    new_grid = transpose_mat(new_grid)
    return new_grid,changed