import json 

MAP_1_DIMENSIONS = [
    ["d", "c", "a", "i"],
    ["l", "c", "n", "s"],
    ["a", "t", "e", "m"],
    ["o", "e", "h", "o"]
]

MAP_2_DIMENSIONS = [
    ["1", "0", "0", "0", "1"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["1", "0", "0", "0", "1"],
]

MAP_3_DIMENSIONS = [
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["1", "0", "0", "0", "1"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
]

MAP_4_DIMENSIONS = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

#Load word dictionary
f = open('words_dictionary.json') 

words_dictionary = json.load(f) 
made_words = []
MINIMUM_WORD_LENGTH = 5

def load_game(dimensions):
    game_board = dimensions
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            #Ignore blocked spaces
            if game_board[i][j] != "1":
                letter_input = input(f"Input letter {i} {j}: ")
                game_board[i][j] = letter_input

    print(game_board)

    return game_board
    
#For each word in dictionary, see if we can make it (we need to be able to go up down left right)

def play_game():
    game_board = load_game(MAP_1_DIMENSIONS)
    all_words = []
    for word in words_dictionary:
        if len(word) >= MINIMUM_WORD_LENGTH:
            game_board_letters = get_game_board_letters(game_board)
            word_letters = list(word)
            word_letters_exist = all(item in game_board_letters for item in word_letters)
            current_letter = 0
            if word_letters_exist:
                #Check if we can make the word by going up, down, left, or right
                letter = word_letters[current_letter]
                #Get all indexes for the letter
                game_board_letter_positions = game_board_letters[letter]
                #For each index
                for letter_index in game_board_letter_positions:
                    #Starting point
                    position_row = letter_index[0]
                    position_column = letter_index[1]
                    this_word = word
                    moves_list = [[letter_index[0], letter_index[1]]]
                    if find_word(game_board, current_letter, position_row, position_column, word, moves_list):
                        all_words.append(this_word)
    
    print(all_words)

def find_word(game_board, current_letter, position_row, position_column, word, moves_list):

    moved = False

    if current_letter >= len(word) - 1:
        #Word found
        return True

    if (move_up(game_board, position_row, position_column) == word[current_letter + 1]):
        position_row -= 1
        moved = True
    elif (move_down(game_board, position_row, position_column) == word[current_letter + 1]):
        position_row += 1
        moved = True
    elif (move_right(game_board, position_row, position_column) == word[current_letter + 1]):
        position_column += 1
        moved = True
    elif (move_left(game_board, position_row, position_column) == word[current_letter + 1]):
        position_column -= 1
        moved = True
    elif (move_up_left_diag(game_board, position_row, position_column) == word[current_letter + 1]):
        position_column -= 1
        position_row -= 1
        moved = True
    elif (move_up_right_diag(game_board, position_row, position_column) == word[current_letter + 1]):
        position_column += 1
        position_row -= 1
        moved = True
    elif (move_down_left_diag(game_board, position_row, position_column) == word[current_letter + 1]):
        position_column -= 1
        position_row += 1
        moved = True
    elif (move_down_right_diag(game_board, position_row, position_column) == word[current_letter + 1]):
        position_column += 1
        position_row += 1
        moved = True
    
    if (moved) and [position_row, position_column] not in moves_list:
        moves_list.append([position_row, position_column])
        return find_word(game_board, current_letter + 1, position_row, position_column, word, moves_list)
    else:
        return False



def get_game_board_letters(game_board):
    letters = {}
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] != "1":
                letter = game_board[i][j]
                if letter in letters:
                    letters[letter].append([i, j])
                else:
                    letters[letter] = [[i, j]]
    return letters



def move_up(game_board, row, column):
    #Boundaries
    if row <= 0:
        return
    return game_board[row - 1][column]

def move_up_left_diag(game_board, row, column):
    #Boundaries
    if row <= 0 or column <= 0:
        return
    return game_board[row - 1][column - 1]

def move_up_right_diag(game_board, row, column):
    #Boundaries
    if row <= 0 or column >= len(game_board[row]) - 1:
        return
    return game_board[row - 1][column + 1]

def move_down_left_diag(game_board, row, column):
    #Boundaries
    if row >= len(game_board) - 1 or column <= 0:
        return
    return game_board[row + 1][column - 1]

def move_down_right_diag(game_board, row, column):
    #Boundaries
    if row >= len(game_board) - 1 or column >= len(game_board[row]) - 1:
        return
    return game_board[row + 1][column + 1]

def move_down(game_board, row, column):
    if row >= len(game_board) - 1:
        return
    return game_board[row + 1][column]

def move_left(game_board, row, column):
    if column <= 0:
        return
    return game_board[row][column - 1]

def move_right(game_board, row, column):
    if column >= len(game_board[row]) - 1:
        return
    return game_board[row][column + 1]

play_game()