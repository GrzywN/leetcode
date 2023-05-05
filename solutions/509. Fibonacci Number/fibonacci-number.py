cache = {
  0: 0,
  1: 1
}


class Solution:
    def fib(self, n: int) -> int:
        if n not in cache:
            cache[n] = self.fib(n - 2) + self.fib(n - 1)

        return cache[n]
