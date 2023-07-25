def display_routes():
    print("Available Train Routes:")
    print("1. Route 1 - Fare: $5")
    print("2. Route 2 - Fare: $7")
    print("3. Route 3 - Fare: $6")
    
def book_ticket():
    display_routes()
    route_choice = int(input("Enter the route number: "))

    if route_choice not in [1, 2, 3]:
        print("Invalid route number.")
        return

    num_tickets = int(input("Enter the number of tickets: "))
    fare = 0

    if route_choice == 1:
        fare = 5
    elif route_choice == 2:
        fare = 7
    elif route_choice == 3:
        fare = 6

    total_amount = fare * num_tickets
    print(f"Total amount payable: ${total_amount}")

    confirm_booking = input("Do you want to confirm the booking? (yes/no): ").lower()

    if confirm_booking == "yes":
        print("Booking confirmed! Enjoy your journey.")
    else:
        print("Booking canceled.")

if __name__ == "__main__":
    print("Welcome to the Local Train Ticketing System!")
    while True:
        print("\nMenu:")
        print("1. Book a Ticket")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_ticket()
        elif choice == 2:
            print("Thank you for using the Local Train Ticketing System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
