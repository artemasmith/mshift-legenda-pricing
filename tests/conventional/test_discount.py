# mypy: ignore-errors
# Фикстура бенчмарка: репозиторий-двойник, не код продукта.

from pricing.discount import apply_discount


def test_applies_ten_percent():
    order = {"total": 1000, "category": "X"}
    assert apply_discount(order, 10)["total"] == 900


def test_returns_same_order():
    order = {"total": 500, "category": "X"}
    assert apply_discount(order, 10) is order
