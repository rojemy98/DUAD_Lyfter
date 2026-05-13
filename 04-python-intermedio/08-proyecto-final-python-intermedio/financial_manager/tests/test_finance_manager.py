from models.finance_manager import FinanceManager
from models.transaction import Transaction
from models.category import Category


# test_add_category
def test_add_category():
    # arrange
    manager = FinanceManager()
    category = Category("Food", "#FFFFFF")

    # act
    manager.add_category(category)

    # assert
    assert len(manager.categories) == 1


# test_add_transaction
def test_add_transaction():
    # arrange
    manager = FinanceManager()

    transaction = Transaction(
        "Salary",
        1000,
        "Work",
        "Income",
        "01/01/2025"
    )

    # act
    manager.add_transaction(transaction)

    # assert
    assert len(manager.transactions) == 1


# test_total_income
def test_total_income():
    # arrange
    manager = FinanceManager()

    manager.add_transaction(
        Transaction("Salary", 1000, "Work", "Income", "01/01/2025")
    )

    # act
    result = manager.get_total_income()

    # assert
    assert result == 1000


# test_total_expenses
def test_total_expenses():
    # arrange
    manager = FinanceManager()

    manager.add_transaction(
        Transaction("Food", 200, "Food", "Expense", "01/01/2025")
    )

    # act
    result = manager.get_total_expenses()

    # assert
    assert result == 200