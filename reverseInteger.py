"""
Runtime: 31 ms, faster than 91.91% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 79.27% of Python3 online submissions for Reverse Integer.
"""

def test(t :int) -> int:
    if t <= -2**31:
        return 0
    elif t >= (2**31 - 1):
        return 0
    else:
        return t


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        l = [i for i in reversed(x) if i != '0' or i.isdigit()]
        v = [j for j in reversed(l)]
        if '-' in v:
            j = [v[i] for i in reversed(range(1,len(v)))]
            j = ['-'] + j
            return test(int("".join(j)))

        else:
            return test(int("".join(l)))
