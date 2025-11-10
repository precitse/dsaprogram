# Program: Fractional Knapsack Problem

def fractional_knapsack(weights, profits, capacity):
    """Calculate maximum profit using Fractional Knapsack logic."""
    
    #Calculate profit/weight ratio for each parcel
    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(len(weights))]
    
    #Sort parcels by ratio (highest profit per weight first)
    ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_profit = 0       # To store total profit
    selected_items = []    # To store selected parcels (weight, profit, fraction)
    
    #Pick parcels one by one
    for r, w, p in ratio:
        if capacity <= 0:  # Truck is full
            break
        
        if w <= capacity:
            # Take the full parcel
            capacity -= w
            total_profit += p
            selected_items.append((w, p, 1.0))  # 100% taken
        else:
            # Take fractional part
            fraction = capacity / w
            total_profit += p * fraction
            selected_items.append((w, p, fraction))
            capacity = 0  # Truck is now full
    
    return total_profit, selected_items


def input_data():
    """Take input for weights, profits, and capacity."""
    n = int(input("Enter number of parcels: "))
    weights = []
    profits = []

    for i in range(n):
        w = float(input(f"Enter weight of parcel {i+1}: "))
        p = float(input(f"Enter profit of parcel {i+1}: "))
        weights.append(w)
        profits.append(p)
    
    capacity = float(input("Enter truck capacity: "))
    return weights, profits, capacity


def display_result(selected, max_profit):
    """Display selected parcels and maximum profit."""
    print("\nSelected parcels:")
    print("{:<10}{:<10}{:<10}".format("Weight", "Profit", "Taken (%)"))
    for w, p, frac in selected:
        print("{:<10}{:<10}{:<10.2f}".format(w, p, frac * 100))
    
    print(f"\nMaximum Profit: {max_profit:.2f}\n")


# Main menu loop
while True:
    print("\n=== Fractional Knapsack Menu ===")
    print("1. Enter Data and Calculate")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # Step 1: Input data
        weights, profits, capacity = input_data()

        # Step 2: Calculate maximum profit
        max_profit, selected = fractional_knapsack(weights, profits, capacity)

        # Step 3: Display result
        display_result(selected, max_profit)

    elif choice == "2":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

