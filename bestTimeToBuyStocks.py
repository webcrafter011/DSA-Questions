def bestTime(array):
    if not array:
        return 0
    
    min_price = float("inf")
    max_profit = 0

    for price in array:
        if price < min_price:
            min_price = price
        
        current_profit = price - min_price
        max_profit = max(current_profit, max_profit)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(bestTime(prices))