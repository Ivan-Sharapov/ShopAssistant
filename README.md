Program Description: Store Sales Management System

This program is a console application designed to manage sales, track inventory, calculate financial metrics, and collect customer feedback.
🔹 Key Features:

     Inventory Management

        Automatically tracks product stock levels

        Persists data between program runs (saved in stock.txt)

        Prevents negative stock (cannot sell more than available)

     Financial Calculations

        Calculates the maximum purchasable quantity based on customer budget

        Fixed item price ($2 per unit)

        Automatically computes:

            Revenue from sales

            Tax (20% of revenue)

            Net profit

     Transaction Logging

        All sales are recorded in sales.txt with details:

            Date and time

            Quantity sold

            Remaining stock

            Financial breakdown (revenue, tax, profit)

     Feedback System

        Customers can rate the store (1-5 stars)

        Optional text feedback

        All ratings and reviews are saved in feedback.txt

    Persistent Data

        Inventory levels are saved in stock.txt

        Sales history and feedback are preserved after closing the program

 How It Works?

    Initialization

        The customer enters their budget in dollars and cents.

        The program checks current stock and displays the maximum purchasable quantity.

    Purchase Process

        The customer selects the desired quantity.

        If funds are insufficient, the system suggests a reduced quantity.

        After purchase:

            Stock levels are updated

            Sale details are logged

    Store Rating

        After checkout, the customer rates the store (1-5 stars).

        Optional text feedback can be provided.

    Data Storage

        All data is saved in files:

            stock.txt — Current inventory count

            sales.txt — Sales history with financial data

            feedback.txt — Customer ratings and reviews

 Technical Details

    Language: Python

    Data Storage: Text files (no database required)

    Encoding: UTF-8 (supports Cyrillic in reviews)

    Error Handling:

        Input validation (numbers only, valid ranges)

        Prevents negative stock

        Auto-recovery for corrupted files

 Example Workflow
Copy

Enter your budget in dollars: 50  
Enter your budget in cents: 0  

Current stock: 1000 units  
You can purchase up to 25 units  

How many items would you like to buy? 10  

Purchase successful! Remaining balance: $30.00  

Rate the store (1-5 stars): 5  
Would you like to leave a review? (1-Yes, 0-No): 1  
Enter your review: Great store!  

Thank you for your feedback!  
See you next time!  
 Output Files

    stock.txt

    990

    sales.txt

    Date: 2024-05-21 14:30:00  
    Sold: 10 units  
    Remaining stock: 990  
    Revenue: $20.00  
    Tax: $4.00  
    Profit: $16.00  
    ----------------------------------------  

    feedback.txt

    [2024-05-21 14:30:00] Rating: 5/5  
    [2024-05-21 14:30:00] Review: Great store!  
    ----------------------------------------  
