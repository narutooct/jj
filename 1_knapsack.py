def knapsack01():
    n = int(input("Enter the number of items: "))

    items = []
    for i in range(n):
        value = int(input(f"Enter the value of item {i+1}: "))
        weight = int(input(f"Enter the weight of item {i+1}: "))
        items.append((value, weight))

    max_weight = int(input("Enter the maximum weight of the knapsack: "))
    # Create a 2D array to store the maximum value for each weight
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]
    
    keep = [[False for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]


    for i in range(1, len(items) + 1):
        for w in range(1, max_weight + 1):
            if items[i-1][1] > w:
                
                dp[i][w] = dp[i-1][w]
                
            else:
                # Choose the maximum value between including the item or not
                if dp[i-1][w] > dp[i-1][w-items[i-1][1]] + items[i-1][0]:
                    dp[i][w] = dp[i-1][w]
                    
                else:
                    dp[i][w] = dp[i-1][w-items[i-1][1]] + items[i-1][0]
                    keep[i][w] = True



    included = []
    i = len(items)
    w = max_weight
    while i > 0 and w > 0:
        if keep[i][w]:
            included.append(i)
            w -= items[i-1][1]
            
        i -= 1
    included.reverse()
    return dp[len(items)][max_weight],included


print(knapsack01())


#Enter the number of items: 4
#Enter the value of item 1: 10
#Enter the weight of item 1: 5
#Enter the value of item 2: 40
#Enter the weight of item 2: 4
#Enter the value of item 3: 30
#Enter the weight of item 3: 6
#Enter the value of item 4: 50
#Enter the weight of item 4: 3
#Enter the maximum weight of the knapsack: 10