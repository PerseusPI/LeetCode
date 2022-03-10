"""
Runtime: 29 ms, faster than 93.45% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.8 MB, less than 88.20% of Python3 online submissions for Divide Two Integers.
"""
def test(t: int) -> int:
    if t <= -2**31:
        return -(2**31), False
    elif t >= (2**31 - 1):
        return (2**31 - 1), False
    else:
        return t, True


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor != 0:
            res = dividend/divisor
            f = test(res)
            if f[1]:
                return int(f[0])
            else:
                return f[0]
        else:
            return 0
