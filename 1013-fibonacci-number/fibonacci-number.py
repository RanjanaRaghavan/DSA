class Solution:
    dp = [-1] * 31

    def fib(self, n: int) -> int:

        #base case
        if n <= 1:
            return n
        
        first = self.dp[n-1] if self.dp[n-1] != -1 else self.fib(n-1)
        second = self.dp[n-2] if self.dp[n-2] != -1 else self.fib(n-2)

        self.dp[n] = first +second
        
        
        return self.dp[n]