"""
ライブラリ
"""
import numpy as np

"""
定数宣言
"""
# マスの状態
EMPTY = 0  # 空きマス
WHITE = -1  # 白石
BLACK = 1  # 黒石
WALL = 2  # 壁

# ボードのサイズ
BOARD_SIZE = 8

"""
ボードの表現
"""


class Board:

    def __init__(self):

        # 全マスを空きマスに設定
        self.RawBoard = np.zeros((BOARD_SIZE + 2, BOARD_SIZE + 2), dtype=int)

        # 壁の設定
        self.RawBoard[0, :] = WALL
        self.RawBoard[:, 0] = WALL
        self.RawBoard[BOARD_SIZE + 1, :] = WALL
        self.RawBoard[:, BOARD_SIZE + 1] = WALL

        # 初期配置
        self.RawBoard[4, 4] = WHITE
        self.RawBoard[5, 5] = WHITE
        self.RawBoard[4, 5] = BLACK
        self.RawBoard[5, 4] = BLACK

        # 手番
        self.Turns = 0

        # 現在の手番の色
        self.CurrentColor = BLACK
