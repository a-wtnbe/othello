# 1
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

# 2
    """
    石を置く事による盤面の変化をボードに反映
    """

    def flipDiscs(self, x, y):

        # 石を置く
        self.RawBoard[x, y] = self.CurrentColor

        # 石を裏返す処理がこの下に続く
        # …

    """
    石を置く
    """

    def move(self, x, y):

        # 置く位置が正しいかどうかをチェック
        if x < 1 or BOARD_SIZE < x:
            return False
        if y < 1 or BOARD_SIZE < y:
            return False
        # if self.MovablePos[x, y] == 0:
        # return False

        # 石を裏返す
        self.flipDiscs(x, y)

        # 手番を進める
        self.Turns += 1

        # 手番を交代する
        self.CurrentColor = - self.CurrentColor

        # MovablePosとMovableDirの更新
        # self.initMovable()

        return True


# ボートインスタンスの作成
board = Board()

# move関数の呼び出し
print(board.move(2, 3))

# RawBoardの中身を確認
for y in range(10):
    for x in range(10):
        print('{:^3}'.format(board.RawBoard[x, y]), end='')
    print()
