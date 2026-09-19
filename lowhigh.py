class Solution:
    def forLoop(self, low : int, high : int) -> int:

     sum = 0

     for i in range(low, high + 1):
        sum = sum + i
     return sum