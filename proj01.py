# Zakarri Smith
# Due October 1st, 2023
# Title: Project 1
import time


def customer_summary(classification, rental_days, start_odometer, end_odometer, miles_driven, amount_billed):
    # Display customer summary
    print("\nCustomer Summary:")
    print(f"Classification Code: {classification}")
    print(f"Rental Days: {rental_days}")
    print(f"Start Odometer Reading: {start_odometer}")
    print(f"End Odometer Reading: {end_odometer}")
    print(f"Miles Driven: {miles_driven}")
    print(f"Amount Billed: ${amount_billed:.2f}\n")


def goodbye_function():
    # Used as a Goodbye
    time.sleep(1)
    print("Have a good day!")


def main():
    try:
        # User choice options
        while True:
            classification = input("Enter classification code (B, D, or W. Press Q to quit)\n: ")
            if classification.upper() == "Q":
                goodbye_function()
                break

            if classification.upper() not in ('B', 'D', 'W'):
                print("Invalid classification code. Please enter 'B' or 'D'.")
                continue

            rental_days = int(input("Enter the number of rental days: "))
            start_odometer = int(input("Enter start odometer reading: "))
            end_odometer = int(input("Enter end odometer reading: "))

            # Calculate the miles driven
            miles_driven = end_odometer - start_odometer

            # Calculate billing amount based on classification code and miles driven
            if classification.upper() == 'B':
                base_charge = 40.00 * rental_days
                mileage_charge = 0.25 * miles_driven
                amount_billed = base_charge + mileage_charge
            elif classification.upper() == 'D':
                base_charge = 60.00 * (rental_days // 7) + 60.00 * (rental_days % 7)
                if miles_driven / rental_days <= 100:
                    mileage_charge = 0
                else:
                    mileage_charge = 0.25 * (miles_driven - 100 * rental_days)
                amount_billed = base_charge + mileage_charge
            elif classification.upper() == 'W':
                base_charge = 190.00 * (rental_days // 7) + 60.00 * (rental_days % 7)
                if miles_driven / rental_days <= 900:
                    mileage_charge = 100.00
                elif miles_driven / rental_days <= 1500:
                    mileage_charge = 200.00
                else:
                    mileage_charge = 0.25 * (miles_driven - 100 * rental_days)
                amount_billed = base_charge + mileage_charge

            # customer_summary function
            customer_summary(classification, rental_days, start_odometer, end_odometer, miles_driven, amount_billed)

    except KeyboardInterrupt:
        print("\nThe process was has been cancelled.")
        goodbye_function()
    except TypeError:
        print("\nA TypeError has occurred within the code.")
        goodbye_function()


main()
