# Program: Online Orders Sorting using Merge Sort

def merge(arr, left, mid, right):
    """Merge two sorted halves of arr."""
    # Create temporary subarrays for left and right halves
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    # Initialize pointers for L, R and main array
    i = j = 0
    k = left

    # Merge the two halves by comparing delivery times
    while i < len(L) and j < len(R):
        if L[i][2] <= R[j][2]:  # Compare based on delivery time (3rd element)
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R (if any)
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    """Recursive merge sort function."""
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)        # Sort left half
        merge_sort(arr, mid + 1, right)   # Sort right half
        merge(arr, left, mid, right)      # Merge the sorted halves


def display_orders(orders):
    """Display all orders neatly."""
    print("\nOrders:")
    print("{:<5} {:<20} {:<15}".format("ID", "Item", "Delivery Time (min)"))
    for order in orders:
        print("{:<5} {:<20} {:<15}".format(order[0], order[1], order[2]))


def main():
    orders = []  # List to store orders

    while True:
        print("\n--- Online Orders Merge Sort Menu ---")
        print("1. Add Order")
        print("2. Display Orders")
        print("3. Sort Orders by Delivery Time")
        print("4. Exit")

        choice = input("Enter choice: ")

        # Option 1: Add a new order
        if choice == "1":
            order_id = input("Enter Order ID: ")
            item_name = input("Enter Item Name: ")
            delivery_time = int(input("Enter Delivery Time (in minutes): "))
            orders.append((order_id, item_name, delivery_time))

        # Option 2: Display all orders
        elif choice == "2":
            if orders:
                display_orders(orders)
            else:
                print("No orders available!")

        # Option 3: Sort orders using merge sort
        elif choice == "3":
            if orders:
                merge_sort(orders, 0, len(orders) - 1)
                print("\nOrders sorted by delivery time:")
                display_orders(orders)
            else:
                print("No orders to sort!")

        # Option 4: Exit
        elif choice == "4":
            print("Exiting program...")
            break

        # Invalid choice
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
