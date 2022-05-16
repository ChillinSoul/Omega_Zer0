import unittest


import NodeAI
from easyAI import Negamax,AI_Player
import numpy as np
from copy import deepcopy


center_pos = [(3,3),(3,4),(4,3),(4,4)]
buffer_pos = [[(0,1),(1,0),(1,1)],[(0,6),(1,6),(1,7)],[(6,0),(6,1),(7,1)],[(6,6),(6,7),(7,6)]]
corner_pos = [(0,0),(0,7),(7,0),(7,7)]
edge_pos   = [[(0,x)for x in range(1,7)],[(7,x)for x in range(1,7)],[(x,0)for x in range(1,7)],[(x,7)for x in range(1,7)]]
diag_pos   = [[(i,i)for i in range(2,6)],[(i,7-i)for i in range(2,6)]]

#premade boards
chicken_diner=[
            [20, 2, 4, 4, 4, 4, 2, 20],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [9, 2, 4, 4, 4, 4, 4, 9]
        ]
chicken_lunch=[
            [20, 4, 4, 4, 4, 4, 2, 20],
            [2, 0, 1, 1, 1, 1, 0, 2],
            [4, 1, 2, 2, 2, 2, 1, 4],
            [4, 1, 2, 3, 3, 2, 1, 4],
            [4, 1, 2, 3, 3, 2, 1, 4],
            [4, 1, 2, 2, 2, 2, 1, 4],
            [2, 0, 1, 1, 1, 1, 0, 2],
            [20, 2, 4, 4, 4, 4, 4, 20]
        ]
chicken_starter=[
            [9, 4, 4, 4, 4, 4, 2, 9],
            [2, -1, 2, 1, 1, 1, -1, 2],
            [4, 2, 2, 1, 1, 1, 1, 4],
            [4, 1, 1, 5, 5, 1, 1, 4],
            [4, 1, 1, 5, 5, 1, 1, 4],
            [4, 2, 2, 1, 1, 2, 2, 4],
            [2, -1, 2, 1, 1, 2, -1, 2],
            [9, 2, 4, 4, 4, 4, 4, 9]
        ]

class TestNodeAI(unittest.TestCase):

    def setUp(self) -> None:
        state = {'players': ['OmegaZero', 'OmegaZero1'], 'current': 0, 'board': [[28, 35], [27, 36]]}
        self.game = NodeAI.omegaZer0AI([AI_Player(Negamax(4)),AI_Player(Negamax(4))],state)


    #-----------outside the class
    def test_extract_disks(self):
        self.assertEqual(NodeAI.extract_disks(self.game.board),([(3, 4), (4, 3)], [(3, 3), (4, 4)]))

    def test_get_futures_diff(self):
        self.assertEqual(NodeAI.get_futures_dif(self.game),0)
        self.game.play_move([2, 3])
        self.assertEqual(NodeAI.get_futures_dif(self.game),0)

    def test_give_point(self):
        score_board = [[1 for _ in range(8)] for _ in range(8)]
        NodeAI.give_point(score_board,center_pos,5)
        self.assertEqual(score_board,[[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 6, 6, 1, 1, 1], [1, 1, 1, 6, 6, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]])

    def test_give_points(self):
        score_board = [[1 for _ in range(8)] for _ in range(8)]
        NodeAI.give_points(score_board,[1,2,3,4,5])
        self.assertEqual(score_board,[[6, 6, 4, 4, 4, 4, 6, 6], [6, 3, 1, 1, 1, 1, 3, 6], [4, 1, 5, 1, 1, 5, 1, 4], [4, 1, 1, 6, 6, 1, 1, 4], [4, 1, 1, 6, 6, 1, 1, 4], [4, 1, 5, 1, 1, 5, 1, 4], [6, 3, 1, 1, 1, 1, 3, 6], [6, 6, 4, 4, 4, 4, 6, 6]])


    def test_make_scoreboard(self):
        self.assertEqual(NodeAI.make_scoreboard(self.game),[[9, 4, 4, 4, 4, 4, 2, 9], [2, -1, 2, 1, 1, 1, -1, 2], [4, 2, 2, 1, 1, 1, 1, 4], [4, 1, 1, 5, 5, 1, 1, 4], [4, 1, 1, 5, 5, 1, 1, 4], [4, 2, 2, 1, 1, 2, 2, 4], [2, -1, 2, 1, 1, 2, -1, 2], [9, 2, 4, 4, 4, 4, 4, 9]])
        bestmove=self.game.get_move()
        self.game.make_move(bestmove)
        self.assertEqual(NodeAI.make_scoreboard(self.game),[[9, 4, 4, 4, 4, 4, 2, 9], [2, -1, 2, 1, 1, 1, -1, 2], [4, 2, 2, 1, 1, 1, 1, 4], [4, 1, 1, 5, 5, 1, 1, 4], [4, 1, 1, 5, 5, 1, 1, 4], [4, 2, 2, 1, 1, 2, 2, 4], [2, -1, 2, 1, 1, 2, -1, 2], [9, 2, 4, 4, 4, 4, 4, 9]])

    def test_get_score(self):
        self.assertEqual(NodeAI.get_score(self.game),0)
        bestmove=self.game.get_move()
        self.game.make_move(bestmove)
        self.assertEqual(NodeAI.get_score(self.game),11)

    #-----------inside the class
    def test_possible_moves(self):
        self.assertEqual(self.game.possible_moves(),[[2, 3], [3, 2], [4, 5], [5, 4]])
        self.assertEqual(self.game.possible_moves(True),[[2, 4], [3, 5], [4, 2], [5, 3]])


    def test_legal(self):
        self.assertTrue(self.game.legal([2, 3],False))
        self.assertFalse(self.game.legal([2, 3],True))
        self.assertFalse(self.game.legal([2, 5],False))


    def test_make_move(self):
        test_board = deepcopy(self.game.board)
        self.game.make_move((2,4))
        self.assertNotEqual(self.game.board.all,test_board.all)
        self.assertEqual(self.game.board[2][4],1)
        self.assertEqual(self.game.board[3][4],1)

    def test_set_disk(self):
        self.game.set_disk([(2,4),(0,1)])
        self.assertEqual(self.game.board[2][4],1)
        self.assertEqual(self.game.board[0][1],1)

    def test_make_board(self):
        test_board = np.zeros((8,8),dtype=int)
        test_board[28//8,28%8] = 1
        test_board[35//8,35%8] = 1
        test_board[27//8,27%8] = 2
        test_board[36//8,36%8] = 2
        for l in range(8):
            for c in range(8):
                self.assertEqual(self.game.make_board([[28, 35], [27, 36]])[l][c],test_board[l][c])

    def test_count(self):
        
        self.game.board[28//8,28%8] = 1
        self.game.board[35//8,35%8] = 1
        self.game.board[27//8,27%8] = 1
        self.game.board[36//8,36%8] = 2
        self.assertEqual(self.game.count(),2)

    def test_win(self):
        self.assertFalse(self.game.win())
        self.game.board = np.ones((8,8))
        self.assertTrue(self.game.win())


if __name__ == "__main__":
    unittest.main()