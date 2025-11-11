def fractional_knapsack(weights, profits, capacity):
    ratio = [(profits[i]/weights[i], weights[i], profits[i]) for i in range(len(weights))]
    ratio.sort(reverse=True)
    
    total_profit = 0
    for r, w, p in ratio:
        if capacity == 0:
            break
        take = min(w, capacity)
        total_profit += r * take
        capacity -= take
    return total_profit

# Input
n = int(input("Enter number of parcels: "))
weights = [float(input(f"Weight {i+1}: ")) for i in range(n)]
profits = [float(input(f"Profit {i+1}: ")) for i in range(n)]
capacity = float(input("Enter capacity: "))

# Result
max_profit = fractional_knapsack(weights, profits, capacity)
print("Maximum Profit:", max_profit)
