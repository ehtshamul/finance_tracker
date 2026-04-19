# Finance Tracker

A simple yet powerful command-line application to track income and expenses, manage budgets, and generate financial summaries.

## Overview

Finance Tracker is a Python-based personal finance management tool that helps users monitor their spending, categorize transactions, and maintain an overview of their financial health. With an intuitive CLI interface, users can easily add transactions, view balances, set budgets, and export financial reports.

## Features

- **Transaction Management**: Add income and expense transactions with detailed descriptions
- **Category-Based Tracking**: Organize transactions into predefined categories (food, salary, entertainment, other)
- **Balance Overview**: View total income, total expenses, and current balance at a glance
- **Category Summary**: Get a breakdown of spending by category, sorted from highest to lowest
- **Budget Alerts**: Set budget limits for categories and receive warnings when approaching or exceeding limits
- **Data Persistence**: Save and load transactions from persistent storage
- **Export Functionality**: Export transactions to CSV format for further analysis
- **Input Validation**: Robust error handling with custom exceptions for invalid data

## Project Structure

```
finance_tracker/
├── finance_tracker.py      # Main application and FinanceTracker class
├── transaction.py          # Transaction class with validation
├── store.py               # Data storage and export functionality
├── report.txt             # Stored transaction data (auto-generated)
├── LICENSE                # Apache License 2.0
└── README.md             # Project documentation
```

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone or download the project files:
```bash
cd finance_tracker
```

2. No external dependencies required - the project uses only Python standard library modules.

## Usage

### Running the Application

Start the application by running:

```bash
python finance_tracker.py
```

### Main Menu Options

The application provides an interactive menu with the following options:

#### 1. Add Transaction
Add a new income or expense transaction.
- **Amount**: Enter the transaction amount (must be positive)
- **Category**: Choose from: `food`, `salary`, `entertainment`, `other`
- **Description**: Brief description of the transaction
- **Type**: Specify as `income` or `expense`

Example:
```
Enter amount: 50.00
Enter category (food, salary, entertainment, other): food
Enter description: Weekly groceries
Enter type (income/expense): expense
```

#### 2. Show Transactions
Display all recorded transactions with their details:
```
Transaction(amount=50.0, category='food', description='Weekly groceries', t_type='expense')
Transaction(amount=2500.0, category='salary', description='Monthly salary', t_type='income')
```

#### 3. Show Balance
View your financial overview:
```
Current balance: 2450.0
Total income: 2500.0
Total expense: 50.0
net balance: 2450.0
```

#### 4. Category Summary
Get a breakdown of expenses by category (highest to lowest):
```
Category Summary: high to low
food: 150.0
entertainment: 75.0
other: 25.0
```

#### 5. Save and Exit
Save all transactions to persistent storage and exit the application.

## Core Components

### FinanceTracker Class

The main application controller that manages:
- Transaction storage and retrieval
- Budget tracking and alerts
- Balance calculations
- Category summaries
- Data persistence

### Transaction Class

Represents individual financial transactions with:
- Amount validation (must be positive)
- Category validation (food, salary, entertainment, other)
- Type validation (income or expense)
- String representation for display

### Storage Module (store.py)

Provides functionality for:
- **CsvExporter**: Export transactions to CSV format
- **save__to_file()**: Save transactions to text file
- **load_file()**: Load transactions from persistent storage

## Data Format

Transactions are stored in `report.txt` with CSV-like format:
```
amount,category,description,t_type
50.0,food,Weekly groceries,expense
2500.0,salary,Monthly salary,income
```

## Budget Management

Set budget limits for categories to stay on track:

```python
tracker.budget["food"] = 300  # Set 300 monthly budget for food
```

The application will warn you when adding a transaction would exceed your budget.

## Error Handling

The application includes comprehensive error handling:

- **InvalidAmountError**: Raised when amount is not positive
- **InvalidCategoryError**: Raised when category is not valid
- **ValueError**: Raised when transaction type is invalid
- **File I/O Errors**: Gracefully handled during save/load operations

## Example Workflow

```
$ python finance_tracker.py

1.Add transaction
2.Show transactions
3.Show balance
4.Category summary
5.Save and exit

Choose an option: 1
Enter amount: 100
Enter category (food, salary, entertainment, other): food
Enter description: Restaurant dinner
Enter type (income/expense): expense
Transaction added successfully.

Choose an option: 3
Current balance: [amount]
Total income: [amount]
Total expense: [amount]
net balance: [amount]

Choose an option: 5
Data saved. Exiting...
```

## Contributing

Contributions are welcome! Feel free to:
- Report issues or bugs
- Suggest new features
- Improve documentation
- Submit pull requests

## Future Enhancements

Potential features for future versions:
- Date tracking for transactions
- Detailed weekly/monthly reports
- Budget alerts and notifications
- Data visualization with charts
- Multi-currency support
- Recurring transactions
- Transaction search and filtering
- Database integration for larger datasets

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Author

Created as a personal finance management tool.

## Support

For issues or questions, please check the project files and ensure:
- Python 3.7+ is installed
- All project files are in the same directory
- `report.txt` has proper read/write permissions
