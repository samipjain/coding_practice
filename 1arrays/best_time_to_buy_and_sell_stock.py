def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # Return none if prices is empty
    if len(prices) == 0:
        return 0
    # Find the index of minimum element
    min_price = 9999
    max_profit = 0
    
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))
    print(maxProfit([2,4,1]))