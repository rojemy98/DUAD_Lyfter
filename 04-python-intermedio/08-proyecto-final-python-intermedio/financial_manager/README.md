📊 Personal Finance Manager

A desktop application built with FreeSimpleGUI that allows users to manage personal finances, including expenses, incomes, categories, filtering, and CSV reporting.
The project is designed to apply OOP principles, modular architecture, file persistence, and unit testing with pytest.

🚀 Features

📌 Add income and expense transactions
🏷️ Create and manage categories with custom colors
📊 View transactions in separate income/expense tables
💾 Automatic CSV persistence (no database required)
🔎 Filter transactions by date range
📤 Export financial reports to CSV
🧮 Real-time balance calculations
🧪 Unit testing with pytest

🧠 Technologies Used

Python 3.13.5
FreeSimpleGUI
CSV (file-based persistence)
Pytest (unit testing)
OOP (Object-Oriented Programming)

⚙️ Installation

1. Clone the repository
git clone https://github.com/your-username/personal-finance-manager.git
cd personal-finance-manager

2. Install dependencies

pip install FreeSimpleGUI pytest

▶️ Run the application
python main.py

🧪 Run Tests
pytest


📌 Core Functionalities

💰 Transactions
Add income and expense entries
Assign category and date
Automatic persistence to CSV

🏷️ Categories
Create custom categories
Assign colors using color picker

🔎 Filters
Filter transactions by date range
Clear filters to restore full view

📤 Export Reports
Export all transactions to CSV
Includes totals:
Total Income
Total Expenses
Net Balance

🧠 Architecture Principles

This project follows:

Separation of Concerns (GUI / Logic / Persistence)
Single Responsibility Principle
Modular design
Testable functions (no GUI dependency in logic layer)

Tests are written using pytest and follow the AAA pattern:

Arrange
Act
Assert

Developed as a learning project at Lyfter academy to practice:

Python OOP
GUI development
Clean architecture
Testing practices
File persistence systems