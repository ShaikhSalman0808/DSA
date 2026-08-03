class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans=-1

        while low <= high :
            mid = (low + high) // 2
            sqrt = mid * mid
            
            if sqrt == x:
                return mid
            
            elif sqrt > x:
                high = mid - 1

            else :
                ans = mid
                low = mid + 1

        return ans