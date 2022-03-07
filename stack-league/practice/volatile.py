def volatile(prices):
#        unfair_counter = 0
#        my_price = prices[len(prices) - 1]
#        for i in range (len(prices) - 1):
#                if prices[i] > my_price:
#                        unfair_counter += 1
#        return unfair_counter

    return len([1 for c in prices if c > prices[len(prices) - 1]])
    
n = [8,8,8,8,1]
print(volatile(n))