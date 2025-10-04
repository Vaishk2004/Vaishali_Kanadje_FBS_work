#Build a currency converter application that convert between different currencies
# currency_converter.py

def currency_converter():
    # Conversion rates relative to USD
    rates = {
        "USD": 1.00,
        "EUR": 0.92,
        "GBP": 0.79,
        "INR": 83.50,
        "JPY": 144.25,
        "AUD": 1.49
    }

    print(" Welcome to Currency Converter ")
    print("Available currencies:", ", ".join(rates.keys()))

    try:
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print(" Invalid amount. Please enter a number.")
        return

    from_currency = input("Enter input currency (e.g., USD): ").upper()
    to_currency = input("Enter output currency (e.g., EUR): ").upper()

    if from_currency not in rates:
        print(f"Currency '{from_currency}' not supported.")
        return
    if to_currency not in rates:
        print(f"Currency '{to_currency}' not supported.")
        return

    # Conversion logic
    usd_amount = amount / rates[from_currency]   # Convert to USD first
    converted_amount = usd_amount * rates[to_currency]

    print(f"\n{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")


if __name__ == "__main__":
    while True:
        currency_converter()
        cont = input("\nDo you want to convert again? (y/n): ").lower()
        if cont != "y":
            print("Thank you for using Currency Converter!")
            break
