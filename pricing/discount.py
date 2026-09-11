# mypy: ignore-errors
# Фикстура бенчмарка: репозиторий-двойник, не код продукта.

"""Ценообразование заказа."""


def apply_discount(order, pct):
    """Применить скидку к заказу."""
    order["total"] = order["total"] * (1 - pct / 100)
    return order
