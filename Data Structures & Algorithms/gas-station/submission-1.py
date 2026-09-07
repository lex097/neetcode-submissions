# gas: [4, 1, 2, 3]
#cost: [1, 2, 2, 4]
# gasTank: -2
# check max > min
# [1,2,3]
# [1,3,2]
# gasTank: 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        maxIndex = - float('inf')
        maxGas = - float('inf')
        gasTank = 0

        for i in range(len(gas) - 1, -1, -1):
            gasTank = gasTank + gas[i] - cost[i]

            if gasTank > maxGas:
                maxGas = gasTank
                maxIndex = i
            
        if gasTank < 0:
            return -1
        
        return maxIndex