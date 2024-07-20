'''
There are numBottles water bottles that are initially full of water. 
You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
 
Constraints:
1 <= numBottles <= 100
2 <= numExchange <= 100
'''


class Solution(object):
    def numWaterBottles(self, num_bottles, num_exchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty_bottles = 0
        extra_bottles = 0
        counter = num_bottles

        while counter > 0:
            counter -= 1
            empty_bottles += 1
            if empty_bottles == num_exchange:
                extra_bottles += 1
                empty_bottles = 0
                counter += 1

        return num_bottles + extra_bottles


num_bottles = 15
num_exchange = 4
solution = Solution()
print(solution.numWaterBottles(num_bottles, num_exchange))
