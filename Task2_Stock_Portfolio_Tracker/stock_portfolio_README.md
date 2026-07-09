# Stock Portfolio Tracker

# Overview

The **Stock Portfolio Tracker** is a command-line Python application developed as part of the **CodeAlpha Python Programming Internship**. This application allows users to manage a simple stock portfolio by entering stock names, the number of shares owned, and the price of each share. It then calculates the total value of the portfolio and displays a summary of the investments.

This project demonstrates the use of Python fundamentals such as dictionaries, loops, functions, arithmetic operations, and user input handling to build a practical financial management application.

# Objective

The objective of this project is to develop a simple portfolio tracking system that enables users to:

- Add multiple stocks to their portfolio.
- Enter the number of shares owned.
- Enter the price per share.
- Calculate the investment value for each stock.
- Display the total value of the portfolio.

 # Features

-  Add multiple stock records.
-  Store stock name, quantity, and price.
-  Calculate the value of each investment.
-  Calculate the total portfolio value.
-  Easy-to-use command-line interface.

 # Technologies Used

- **Programming Language:** Python


# Project Structure

Stock_Portfolio_Tracker/
│── stock_portfolio.py
└── README.md

# Sample Console Output

===== Stock Portfolio Tracker =====

Available Stocks:
AAPL : $180
TSLA : $250
GOOG : $150
MSFT : $300
AMZN : $200

Enter Stock Name (or type 'done' to finish): MSFT
Enter Quantity: 7

Investment in MSFT: $2100

Enter Stock Name (or type 'done' to finish): AMZN
Enter Quantity: 5

Investment in AMZN: $1000

Enter Stock Name (or type 'done' to finish): done

========== Portfolio Summary ==========

MSFT
Price    : $300
Quantity : 7
Investment : $2100

AMZN
Price    : $200
Quantity : 5
Investment : $1000

--------------------------------------
Total Investment Value = $3100

Portfolio saved successfully in 'portfolio.txt'

# Generated Output File (portfolio.txt)

After execution, the program automatically creates a file named **portfolio.txt** containing the portfolio summary.

Example:

Stock Portfolio Summary
========================

MSFT
Price: $300
Quantity: 7
Investment: $2100

AMZN
Price: $200
Quantity: 5
Investment: $1000

Total Investment Value = $3100

# Concepts Used

- Variables and Data Types
- Dictionaries
- Loops
- Functions
- Arithmetic Operations
- User Input Handling
- Data Processing

# Future Enhancements

- Save portfolio data to a file.
- Load existing portfolios.
- Fetch live stock prices using APIs.
- Export portfolio reports.
- Develop a graphical user interface (GUI).

# Learning Outcomes

Through this project, I gained practical experience in:

- Working with dictionaries and data structures.
- Performing financial calculations.
- Handling user input efficiently.
- Building command-line applications.
- Applying Python programming concepts to real-world problems.

 # Author

**Bhavitha Gande**

CodeAlpha Python Programming Internship
