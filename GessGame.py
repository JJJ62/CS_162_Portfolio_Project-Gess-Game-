# Author: Jawad Alamgir
# Date: 25th May 2020
# Program: The program let's a player play the board game called Gess


# class Stone:
#     """
#     Class for creating an object for every stone on the board.
#     This class communicates with the Board so it can update it's own location
#     """
#
#     def __init__(self):
#         """
#         The Stone class holds the location of stones on the board as well as their color
#         """
#         self._location = None
#         self._color = str
#
#     def check_color(self):
#         if

class Piece:
    """
    This class represents a 3x3 piece that the player can move and select
    """

    def __init__(self):
        self._stones_columns = []
        self._stones_rows = []

    def add_stone(self, stone_column, stone_row):
        self._stones_columns.append(stone_column)
        self._stones_rows.append(stone_row)


class GessGame:
    """
    This class runs most of the major functionality of the game such as making moves or resigning and as such will be
    communicating with the Board and Player classes. The Player class to create player objects so  they can be
    handled as 2 separate players(having a different count for rings adn number of Stones and such),
    the Board class to get locations of Stones as well as making moves.
    """

    def __init__(self):
        """
        This class stores the game state and a board that has information of where all the stones are and the number
        of rings of each player
        """
        self._board = Board()
        self._game_state = str
        self._player_black = Player("BLACK")
        self._player_white = Player("WHITE")
        self._current_turn = "BLACK"

    def get_current_turn(self):
        return self._current_turn

    def start_game(self):
        """
        Fills the player objects with their stone locations and initializes the board as well as filling ti with the
        appropriate stones in their starting positions.
        :return:
        """
        self._board.create_board()
        self._board.set_pieces()
        # self._player_black.set_stone_locations()
        # self._player_white.set_stone_locations()
        print("You are playing the board game called Gess. The black pieces are represented by 'X' and the white pieces"
              "are represented by 'O'")

    def is_legal_piece(self, centre_of_piece_column, centre_of_piece_row):
        """
        Checks if the players selected piece is legal or not. If it is then it returns True otherwise False
        :param centre_of_piece_column:
        :param centre_of_piece_row:
        :return: True or False
        """
        bool_check = True
        if self._current_turn == "BLACK":
            if self._board.get_stone(centre_of_piece_column, centre_of_piece_row) == "O":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column, centre_of_piece_row + 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column, centre_of_piece_row - 1) == "O":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row) == "O" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row) == "O":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row - 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row + 1) == "O":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row - 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row + 1) == "O":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column, centre_of_piece_row) == "X" or \
                    self._board.get_stone(centre_of_piece_column, centre_of_piece_row + 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column, centre_of_piece_row - 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row) == "X" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row) == "X" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row - 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row + 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row - 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row + 1) == "X":
                bool_check = True
        if self._current_turn == "WHITE":
            if self._board.get_stone(centre_of_piece_column, centre_of_piece_row) == "X":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column, centre_of_piece_row + 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column, centre_of_piece_row - 1) == "X":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row) == "X" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row) == "X":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row - 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row + 1) == "X":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row - 1) == "X" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row + 1) == "X":
                bool_check = False
            if self._board.get_stone(centre_of_piece_column, centre_of_piece_row) == "O" or \
                    self._board.get_stone(centre_of_piece_column, centre_of_piece_row + 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column, centre_of_piece_row - 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row) == "O" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row) == "O" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row - 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column - 1, centre_of_piece_row + 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row - 1) == "O" or \
                    self._board.get_stone(centre_of_piece_column + 1, centre_of_piece_row + 1) == "O":
                bool_check = True
        return bool_check

    def end_turn(self):
        """
        Switches the current turn to the player of the other color
        :return:
        """
        if self._current_turn == "BLACK":
            self._current_turn = "WHITE"
        if self._current_turn == "WHITE":
            self._current_turn = "BLACK"

    def is_legal_movement(self, centre_of_piece_column, centre_of_piece_row, where_it_is_being_moved_column,
                          where_it_is_being_moved_row, movement_length=0):
        """
        Will check if the movement of the piece by the player is legal and return True if it is and False otherwise
        :param movement_length:
        :param centre_of_piece_column:
        :param centre_of_piece_row:
        :param where_it_is_being_moved_column:
        :param where_it_is_being_moved_row:
        :return: True or False
        """
        current_piece = self._board.get_stone(centre_of_piece_column, centre_of_piece_row)
        if self._current_turn == "BLACK":
            if current_piece == "X" and (self._board.get_stone(centre_of_piece_column - 1,
                                                               centre_of_piece_row) == "X" or self._board.get_stone(
                    centre_of_piece_column + 1, centre_of_piece_row) == "X" or self._board.get_stone(
                    centre_of_piece_column, centre_of_piece_row + 1) == "X" or self._board.get_stone(
                    centre_of_piece_column, centre_of_piece_row - 1) == "X" or self._board.get_stone(
                    centre_of_piece_column - 1, centre_of_piece_row + 1) == "X" or self._board.get_stone(
                    centre_of_piece_column - 1, centre_of_piece_row - 1) == "X" or self._board.get_stone(
                    centre_of_piece_column + 1, centre_of_piece_row + 1) == "X" or self._board.get_stone(
                    centre_of_piece_column + 1, centre_of_piece_row - 1) == "X"):
                movement_length = 20
            else:
                movement_length = 3
            # if centre_of_piece_column
        if self._current_turn == "WHITE":
            if (current_piece == "X") and (self._board.get_stone(centre_of_piece_column - 1,
                                                                 centre_of_piece_row) == "O" or self._board.get_stone(
                    centre_of_piece_column + 1, centre_of_piece_row) == "O" or self._board.get_stone(
                    centre_of_piece_column, centre_of_piece_row + 1) == "O" or self._board.get_stone(
                    centre_of_piece_column, centre_of_piece_row - 1) == "O" or self._board.get_stone(
                    centre_of_piece_column - 1, centre_of_piece_row + 1) == "O" or self._board.get_stone(
                    centre_of_piece_column - 1, centre_of_piece_row - 1) == "O" or self._board.get_stone(
                    centre_of_piece_column + 1, centre_of_piece_row + 1) == "O" or self._board.get_stone(
                    centre_of_piece_column + 1, centre_of_piece_row - 1) == "O"):
                movement_length = 20
            else:
                movement_length = 3
        return movement_length

    def is_overlapping(self, centre_of_piece_column, centre_of_piece_row, where_it_is_being_moved_column,
                       where_it_is_being_moved_row):
        """
        Checks if the footprint of the piece being moved overlaps any stones returning True if it does and False
        otherwise
        :param where_it_is_being_moved_column:
        :param centre_of_piece_column:
        :param centre_of_piece_row:
        :param where_it_is_being_moved_row:
        :return: True or False
        """
        if self._current_turn == "BLACK":
            pass
        if self._current_turn == "WHITE":
            pass

    def is_on_board(self, ):
        pass

    def update_board(self, centre_stone_of_piece_moved, desired_location):
        """
        Updates the positions of the stones on the board at the end of every turn removing and changing locations of
        stones as needed
        :param centre_stone_of_piece_moved:
        :param desired_location:
        :return: Board
        """
        pass

    def set_board(self):
        """
        Makes a list which serves as a board and fills it with stones in the starting configuration of the game
        :return:
        """
        pass

    def display_board(self):
        """
        Prints a GUI for the user visualing the current state of the game(displays the board)
        :return:
        """
        # board = ['0 ' for x in range(200)]
        # print("\n".join(" ".join(board[i:i + 20]) for i in range(0, 200, 10)))
        pass

    def get_game_state(self):
        """
        Checks what the state of the game is and returns 'UNFINISHED' if game
        is not over otherwise returns either 'BLACK_WON' or 'WHITE_WON' according
        to who wins.
        """
        pass

    def resign_game(self):
        """
        Allows the player whose turn it currently is to forfeit the game
        """
        pass

    def make_move(self, string_representing_centre_square_of_piece_being_moved, desired_new_location):
        """
        Once the user inputs the piece they want to move and where they want to move it to the function will check if it
        is legal and if it is the function will check if all the stones of the piece are in the 18x18 board if not it
        will remove them and then update the board
        :param string_representing_centre_square_of_piece_being_moved:
        :param desired_new_location:
        :return:
        """
        pass

    def check_rings_black(self):
        pass

    def check_rings_white(self):
        pass


class Player:
    """
    Class for representing each player in the game. This class interacts with the GessGame class to provide information
    of each players Rings and Stones
    """

    def __init__(self, color):
        """
        The data this class holds is the player color, the total number of stones they have and the total number of
        rings they have as well as their location on the board.
        """
        self._color = color
        self._total_stones = 43
        self._rings = 1
        self._stone_locations = [list]
        # if color == "BLACK":
        #     self._stone_locations = [[1][2], [1][4], [1][6], [1][7], [1][8], [1][9], [1][10], [1][11],
        #                              [1][12], [1][13], [1][15], [1][17], [2][1], [2][2], [2][3],
        #                              [2][5], [2][7], [2][8], [2][9], [2][10], [2][12], [2][14],
        #                              [2][16], [2][17], [2][18], [3][2], [3][4], [3][6], [3][7], [3][8],
        #                              [3][9], [3][10], [3][11], [3][12], [3][13], [3][15], [3][17],
        #                              [3][2], [3][5], [3][8], [3][11], [3][14], [3][17], [6][2], [6][5],
        #                              [6][8], [6][11], [6][14], [6][17]]
        # if color == "WHITE":
        #     self._stone_locations = [[18][2], [18][4], [18][6], [18][7], [18][8], [18][9], [18][10], [18][11], [18][12],
        #                              [18][13], [18][15], [18][17], [17][1], [17][2], [17][3], [17][5], [17][7], [17][8],
        #                              [17][9], [17][10], [17][12], [17][14], [17][16], [17][17], [17][18], [16][2],
        #                              [16][4], [16][6], [16][7], [16][8], [16][9], [16][10], [16][11], [16][12], [16][13]
        #         , [16][15], [16][17], [16][2], [16][5], [16][8], [16][11], [16][14], [16][17],
        #                              [13][2], [13][5], [13][8], [13][11], [13][14], [13][17]]

    def has_rings(self):
        """
        Checks if the player has rings returning True if they do and False otherwise
        :return: True or False
        """
        if self._rings > 0:
            return True
        else:
            return False

    def set_stone_locations(self):
        if self._color == "BLACK":
            self._stone_locations = [1][2], [1][4], [1][6], [1][7], [1][8], [1][9], [1][10], [1][11], [1][12], [1][13], \
                                    [1][15], [1][17], [2][1], [2][2], [2][3], [2][5], [2][7], [2][8], [2][9], [2][10], \
                                    [2][12], [2][14], [2][16], [2][17], [2][18], [3][2], [3][4], [3][6], [3][7], [3][8], \
                                    [3][9], [3][10], [3][11], [3][12], [3][13], [3][15], [3][17], [6][2], [6][5], [6][
                                        8], [6][11], [6][14], [6][17]
        if self._color == "WHITE":
            self._stone_locations = [[18][2], [18][4], [18][6], [18][7], [18][8], [18][9], [18][10], [18][11], [18][12],
                                     [18][13], [18][15], [18][17], [17][1], [17][2], [17][3], [17][5], [17][7], [17][8],
                                     [17][9], [17][10], [17][12], [17][14], [17][16], [17][17], [17][18], [16][2],
                                     [16][4], [16][6], [16][7], [16][8], [16][9], [16][10], [16][11], [16][12],
                                     [16][13], [16][15], [16][17], [13][2], [13][5], [13][8], [13][11], [13][14],
                                     [13][17]]


class Board:
    """
    This class represents the board the game will be played on and will communicate with the GessGame class providing a
    board for the game to be played on
    """

    def __init__(self):
        """
        The data it hold is the board which has all the empty spaces and stones as a list
        """
        self._board = []

    def get_stone(self, column, row):
        return self._board[column][row]

    def create_board(self):
        """
        Function creates a board by making lists inside of lists and filling them with empty spaces to represent empty
        squares on the board
        :return:
        """
        for i in range(20):  # create a list with nested lists
            self._board.append([])
            for n in range(20):
                self._board[i].append(" ")

    def set_pieces(self):
        """
        Fills the board with white and black pieces in their starting positions
        :return:
        """
        self.set_pieces_black()
        self.set_pieces_white()

    def set_pieces_black(self):
        """
        Fills the board with black pieces in their starting position. Helps set_pieces function
        :return:
        """
        self._board[1][2] = "X"
        self._board[1][4] = "X"
        self._board[1][6] = "X"
        self._board[1][7] = "X"
        self._board[1][8] = "X"
        self._board[1][9] = "X"
        self._board[1][10] = "X"
        self._board[1][11] = "X"
        self._board[1][12] = "X"
        self._board[1][13] = "X"
        self._board[1][15] = "X"
        self._board[1][17] = "X"
        self._board[2][1] = "X"
        self._board[2][2] = "X"
        self._board[2][3] = "X"
        self._board[2][5] = "X"
        self._board[2][7] = "X"
        self._board[2][8] = "X"
        self._board[2][9] = "X"
        self._board[2][10] = "X"
        self._board[2][12] = "X"
        self._board[2][14] = "X"
        self._board[2][16] = "X"
        self._board[2][17] = "X"
        self._board[2][18] = "X"
        self._board[3][2] = "X"
        self._board[3][4] = "X"
        self._board[3][6] = "X"
        self._board[3][7] = "X"
        self._board[3][8] = "X"
        self._board[3][9] = "X"
        self._board[3][10] = "X"
        self._board[3][11] = "X"
        self._board[3][12] = "X"
        self._board[3][13] = "X"
        self._board[3][15] = "X"
        self._board[3][17] = "X"
        self._board[6][2] = "X"
        self._board[6][5] = "X"
        self._board[6][8] = "X"
        self._board[6][11] = "X"
        self._board[6][14] = "X"
        self._board[6][17] = "X"

    def set_pieces_white(self):
        """
        Fills the board with black pieces in their starting position. Helps set_pieces function
        :return:
        """
        self._board[18][2] = "O"
        self._board[18][4] = "O"
        self._board[18][6] = "O"
        self._board[18][7] = "O"
        self._board[18][8] = "O"
        self._board[18][9] = "O"
        self._board[18][10] = "O"
        self._board[18][11] = "O"
        self._board[18][12] = "O"
        self._board[18][13] = "O"
        self._board[18][15] = "O"
        self._board[18][17] = "O"
        self._board[17][1] = "O"
        self._board[17][2] = "O"
        self._board[17][3] = "O"
        self._board[17][5] = "O"
        self._board[17][7] = "O"
        self._board[17][8] = "O"
        self._board[17][9] = "O"
        self._board[17][10] = "O"
        self._board[17][12] = "O"
        self._board[17][14] = "O"
        self._board[17][16] = "O"
        self._board[17][17] = "O"
        self._board[17][18] = "O"
        self._board[16][2] = "O"
        self._board[16][4] = "O"
        self._board[16][6] = "O"
        self._board[16][7] = "O"
        self._board[16][8] = "O"
        self._board[16][9] = "O"
        self._board[16][10] = "O"
        self._board[16][11] = "O"
        self._board[16][12] = "O"
        self._board[16][13] = "O"
        self._board[16][15] = "O"
        self._board[16][17] = "O"
        self._board[16][2] = "O"
        self._board[16][5] = "O"
        self._board[16][8] = "O"
        self._board[16][11] = "O"
        self._board[16][14] = "O"
        self._board[16][17] = "O"
        self._board[13][2] = "O"
        self._board[13][5] = "O"
        self._board[13][8] = "O"
        self._board[13][11] = "O"
        self._board[13][14] = "O"
        self._board[13][17] = "O"


class Ring:
    """
    This class represents a ring (a 3x3 block of tiles with stones everywhere other than the centre). This class
    communicates with the Player class to provide information of how many rings there are and takes the stone_location
    information from the PLayer class
    """

    def __init__(self):
        """
        The data this class holds is the stones that make up the ring
        """
        self._made_of_stones = [Stone]


alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
g = GessGame()
# b = Board()
# b.create_board()
# b.set_pieces()
# print(b.get_stone(2,1))
g.start_game()
g.is_legal_movement(1, 1, 2, 3)
