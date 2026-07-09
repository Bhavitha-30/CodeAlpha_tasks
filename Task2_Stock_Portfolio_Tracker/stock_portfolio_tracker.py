# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

# Variable to store total investment
total_investment = 0

# Dictionary to store user's portfolio
portfolio = {}

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    # Take stock name as input
    stock_name = input("\nEnter Stock Name (or type 'done' to finish): ").upper()

    # Stop taking input
    if stock_name == "DONE":
        break

    # Check if stock exists
    if stock_name in stock_prices:

        # Take quantity
        quantity = int(input("Enter Quantity: "))

        # Save in portfolio
        portfolio[stock_name] = quantity

        # Calculate investment
        investment = stock_prices[stock_name] * quantity

        # Add to total
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Invalid Stock Name!")

# Display Portfolio
print("\n========== Portfolio Summary ==========")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    print(f"{stock}")
    print(f"Price    : ${price}")
    print(f"Quantity : {quantity}")
    print(f"Investment : ${investment}")
    print()

print("--------------------------------------")
print(f"Total Investment Value = ${total_investment}")

# Save to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("========================\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"{stock}\n")
        file.write(f"Price: ${price}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Investment: ${investment}\n\n")

    file.write(f"Total Investment Value = ${total_investment}")

print("\nPortfolio saved successfully in 'portfolio.txt'")