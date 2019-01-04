
# 這個game.py 作為物件 給別的 .py import

import random
class PwdMachine:
    # 設計圖建構
    def __init__(self, l = 1, h = 100):
        self.low = l
        self.high = h
        self.ans = random.randint(l , h)
        self.times = 0
    # 建構專屬技能 猜測
    def guess(self, g):
        if g == self.ans:
            self.times = self.times + 1
            return True
        elif g > self.ans:
            self.times = self.times + 1
            self.high = g
            return False
        else:
            self.times = self.times + 1
            self.low = g
            return False