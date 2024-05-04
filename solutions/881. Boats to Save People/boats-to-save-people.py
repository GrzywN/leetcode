class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] == limit:
                boats += 1
                l += 1
            elif people[r] == limit:
                boats += 1
                r -= 1
            elif people[l] + people[r] > limit:
                if people[r] <= limit:
                    boats += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 2
                l += 1
                r -= 1

        return boats
