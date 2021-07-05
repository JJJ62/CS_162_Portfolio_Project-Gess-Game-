# CS_162_Portfolio_Project-Gess-Game-

Write a class named GessGame for playing an abstract board game called Gess. You can see the rules here. Note that when a piece's move causes it to overlap stones, any stones covered by the footprint get removed, not just those covered by one of the piece's stones. It is not legal to make a move that leaves you without a ring. It's possible for a player to have more than one ring. A player doesn't lose until they have no remaining rings.

Locations on the board will be specified using columns labeled a-t and rows labeled 1-20, with row 1 being the Black side and row 20 the White side. The actual board is only columns b-s and rows 2-19. The center of the piece being moved must stay within those boundaries. An edge of the piece may go into columns a or t, or rows 1 or 20, but any pieces there are removed at the end of the move. Black goes first.

Your GessGame class must include the following:

An init method that initializes any data members.
A method called get_game_state that takes no parameters and returns 'UNFINISHED', 'BLACK_WON' or 'WHITE_WON'.
A method called resign_game that lets the current player concede the game, giving the other player the win.
A method called make_move that takes two parameters - strings that represent the center square of the piece being moved and the desired new location of the center square. For example, make_move('b6', 'e9'). If the indicated move is not legal for the current player, or if the game has already been won, then it should just return False. Otherwise it should make the indicated move, remove any captured stones, update the game state if necessary, update whose turn it is, and return True.
Feel free to add whatever other classes, methods, or data members you want. All data members must be private

Rules:
  Gess is played on a grid of 18 × 18 squares.
  
  Two players, "Black" and "White", each have 43 stones of their colour on the board in the starting configuration.
  
  Starting with Black, players take turns moving a piece on the board. A move must always change the stone configuration on the board. There is no passing.
  
  A piece consists of a 3 × 3 grid of squares, at least one of which must exist on the board. Only stones of one colour may be in the grid. There must be at least one stone on     the eight squares around the central square.
  
  A piece can only be moved by the player whose stones are inside the grid.
  
  The 3 × 3 grid is termed the footprint of the piece. Each piece can move as determined by the stones in its footprint:
    The central square determines the extent of the piece's movement. If the square is unoccupied, it may move up to three spaces; if it is occupied by a stone, it may move any     number of spaces.
    
    Each of the eight surrounding squares determines the directions the piece can move. If a square has a stone, the piece can move in the direction indicated by the square's       location relative to the central square; if a square is unoccupied, the piece cannot move in that direction.
    
    As a piece moves, all of the stones in its footprint move in unison.
    
    When the footprint of a piece coincides with any other stones on the board, those stones are removed from the board and the move ends.
    
    If the footprint moves partially out of the board, the move ends. The stones of the piece which are on a square that has moved out of the board are removed.
    
    A move also may end before any stone is removed.
    
    A ring is any piece consisting of eight stones around an empty central square.
    
    The game object is to be the only player with a ring piece on the board: when, at the end of any turn, a player has no ring pieces on the board, that player loses the game.     If neither player has a ring piece, the player who has just moved loses.
