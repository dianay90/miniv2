import random
import sys
from read import readInput
from write import writeOutput

from host import GO

class DianaPlayer():
    def __init__(self):
        self.type = 'random'

    def get_input(self, go, piece_type):
        '''
        Get one input.

        :param go: Go instance.
        :param piece_type: 1('X') or 2('O').
        :return: (row, column) coordinate of input.
        '''        
        possible_placements = []
        for i in range(go.size): #FOR LOOP FINDS ALL THE POSITIONS THAT"S OPEN
            for j in range(go.size):
                if go.valid_place_check(i, j, piece_type, test_check = True):
                    possible_placements.append((i,j))

        if not possible_placements:
            return "PASS"
        else:
            return random.choice(possible_placements)

if __name__ == "__main__":
    N = 5
    piece_type, previous_board, board = readInput(N)
    go = GO(N)
    go.set_board(piece_type, previous_board, board)
    player = DianaPlayer() #minimpaax player
    action = player.get_input(go, piece_type)
    print(action)
    print("helloworld")
    writeOutput(action)

    #moves to the host

    #host updates state and gives to ME 