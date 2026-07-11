class solution:
    def ClimbStairs(self,n: int) -> int:
        if n<=2:
            return n
        ob = 2
        tb = 1
        for i in range(3,n+1):
            c = ob + tb
            tb, ob = ob, c
        return ob
    