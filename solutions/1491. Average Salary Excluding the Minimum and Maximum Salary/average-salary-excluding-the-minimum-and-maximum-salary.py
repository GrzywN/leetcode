class Solution:
    def average(self, salary: list[int]) -> float:
        sum = 0
        sorted_salary = sorted(salary)
        length_without_min_and_max = len(salary) - 2

        for i in range(1, len(sorted_salary) - 1):
            sum += sorted_salary[i]

        return sum / length_without_min_and_max
