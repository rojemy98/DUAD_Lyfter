import pytest

from services.filters import filter_transactions_by_date
from models.transaction import Transaction


# test_filter_transactions_by_date
def test_filter_transactions_by_date():
    # arrange
    transactions = [
        Transaction("A", 100, "Cat", "Income", "01/01/2025"),
        Transaction("B", 100, "Cat", "Income", "10/01/2025"),
        Transaction("C", 100, "Cat", "Income", "20/01/2025")
    ]

    start_date = "05/01/2025"
    end_date = "15/01/2025"

    # act
    result = filter_transactions_by_date(
        transactions,
        start_date,
        end_date
    )

    # assert
    assert len(result) == 1