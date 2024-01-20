class Solution:

    # Need DP for optimality. At first Greedy looks tempting, but consider coins = [1, 3, 4], target = 6
    #   Greedy would return 3 (4, 1, 1) when the optimal solution is 2 (3, 3). 
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP table as hashmap for quick lookups. 
        #   Base Case: Each coin value can be made in 1 coin, and 0 can be made in 0 coins
        dp = {coin: 1 for coin in coins}
        dp[0] = 0
        
        # Need to check every amount from 0 to amount
        for i in range(amount + 1):
            # Skips amounts in coins
            if i in dp: continue
            # placeholder, the most coins possible to make any 'amount' is just 'amount'. Pick 'amount' 1s. 
            minimum = amount + 1

            # Now for each amount, we need to see which coin would give us the least number of coins needed to make amount
            for coin in coins:
                # If we already know how to make target - coin
                if i - coin in dp:
                    minimum = min(minimum, dp[i - coin] + 1)

            # If we beat the placeholder, add it to the hashmap
            if minimum != amount + 1:
                dp[i] = minimum
        
        # If we can make the amount, return the min coins to do so
        return dp[amount] if amount in dp else -1