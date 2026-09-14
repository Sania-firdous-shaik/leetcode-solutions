class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        Ax1, Ay1, Ax2, Ay2 = rec1
        Bx1, By1, Bx2, By2 = rec2

        separated_x = Ax2 <= Bx1 or Ax1 >= Bx2
        separated_y = Ay2 <= By1 or Ay1 >= By2
        no_overlap = separated_x or separated_y

        return not no_overlap