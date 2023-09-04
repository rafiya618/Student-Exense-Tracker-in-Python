# Student-Exense-Tracker-in-Python
This project is a simple expense tracking and management system of a student with user authentication. Here's a brief description of the project:

    User Authentication: The project begins with user authentication. It requires the user to input a username and password. If the provided credentials match the predefined values (my_password and my_username), the user is granted access to the expense management features. Otherwise, access is denied.

    Expense Tracking: Once authenticated, the user can input their monthly expenses, which are categorized into various expense types such as hostel dues, transportation costs, food expenses, university dues, entertainment expenses, medical expenses, and personal expenses.

    Expense Calculation: The Expenses class is used to calculate the total monthly expenses and the money saved by subtracting the total expenses from a predefined monthly income (my_income).

    Data Storage: The project stores the expense data in a text file named 'Expenses.txt'. Each entry in this file contains details about the month, various expense categories, total expenses, and money saved.

    Viewing Monthly Expenses: Users can view their monthly expenses and savings by entering their username and password. The project reads the data from 'Expenses.txt' and presents it in a readable format, displaying the details of each expense category along with the total expenses and money saved for each month.
