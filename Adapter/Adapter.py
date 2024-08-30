import math

from Material import RoundPeg,RoundHole,SquarePeg
class SquarePegAdapter(RoundPeg):
    def __init__(self, peg:SquarePeg):
        self.peg = peg

    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2)/2


if __name__ == "__main__":
    hole = RoundHole(5)
    rpeg = RoundPeg(5)
    print(hole.fits(rpeg))

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)

    # 方钉不能直接与圆孔比较，因此下面的代码行是无效的：
    # print(hole.fits(small_sqpeg))  # 这会产生错误，因为类型不匹配

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

    print(hole.fits(small_sqpeg_adapter))
    print(hole.fits(large_sqpeg_adapter))