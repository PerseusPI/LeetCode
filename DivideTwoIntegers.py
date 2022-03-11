"""
Runtime: 28 ms, faster than 97.63% of Python3 online submissions for Divide Two Integers.
Memory Usage: 14 MB, less than 52.25% of Python3 online submissions for Divide Two Integers.
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
            temp = int(f[0]) if [1] else int(f[0])
            return temp
