class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]

            if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0):
                return False

        return True
