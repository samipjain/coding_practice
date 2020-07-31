lookup = {0: 0, 1: 1, 2: 1}
def tribonacci(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n in self.lookup:
        return self.lookup[n]
    else:
        value = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.lookup[n] = value
        return value


print(tribonacci(29))
