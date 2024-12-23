# create a function that takes the players INPUT with the correct coordinates of an array and 
# if there's already a value in the specified coordinates
def playerMove(player, board):
    
    row = int(input("Enter row:"))
    column = int(input("Enter column:"))
    if((row < 0 or row > 3) and (column < 0 or column > 3)):
        while((row < 0 or row > 3) and (column < 0 or column > 3)):
            print(f"Invalid row and/or column, {player}'s turn again...")
            row = int(input("Enter row:"))
            column = int(input("Enter column:"))
    
    board[row][column] = player
    
    return board
    
# this function prints the board
def dispBoard(board):
    print("      | col 1 | col 2 | col3")
    for x in range(len(board)):
        print(f"row {x} |   {board[x][0]}   |   {board[x][1]}   |   {board[x][2]}  ")

# create a function checker of the CURRENT STATE of the game
# return player 1 wins IF the array has THREE matching X's in the board
# return player 2 wins IF the array has THREE matching O's in the board
# return draw nobody wins IF the array has full values AND no possible moves left
def checkState():
    pass

# main program to perform TIC TAC TOE
def main():
    player1, player2 = "X","O"
    board = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
    flag = False
    
    while(not flag):
        # print the board
        dispBoard(board)
        
        playerMove(player1, board)
        
        dispBoard(board)
        
        playerMove(player2, board)

main()