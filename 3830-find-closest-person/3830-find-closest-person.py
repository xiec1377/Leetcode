class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        y_dist = abs(z - y)
        x_dist = abs(z - x)
        if y_dist > x_dist:
            return 1
        elif x_dist > y_dist:
            return 2
        else:
            return 0
        