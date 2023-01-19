class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
      customers = []

      for i in range(len(accounts)):
        customers.append(sum(accounts[i]))

      return max(customers)
