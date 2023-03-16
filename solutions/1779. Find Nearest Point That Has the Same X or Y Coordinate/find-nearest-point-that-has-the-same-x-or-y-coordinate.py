class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        nearest_distance = float("+inf")
        nearest_distance_index = -1

        for i, point in enumerate(points):
            if not (x == point[0] or y == point[1]):
                continue

            x_2 = point[0]
            y_2 = point[1]
            distance = abs(x - x_2) + abs(y - y_2)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_distance_index = i

        return nearest_distance_index
