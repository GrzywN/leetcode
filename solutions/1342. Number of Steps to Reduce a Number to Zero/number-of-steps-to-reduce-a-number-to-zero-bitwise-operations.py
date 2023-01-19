class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        currNumber = num

        while currNumber > 0:
            if currNumber & 1 == 0:
                currNumber >>= 1
            else:
                currNumber -= 1
            steps += 1
        
        return steps
