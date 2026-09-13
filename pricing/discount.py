# mypy: ignore-errors
# Фикстура бенчмарка: репозиторий-двойник, не код продукта.

"""Ценообразование заказа."""


def apply_discount(order, pct, category=None):
    """Применить скидку к заказу.

    Скидка не применяется повторно к уценённому заказу и не применяется,
    если передана категория, не совпадающая с категорией заказа.
    """
    if order.get("discounted") is True:
        return order
    if category is not None and category != order.get("category"):
        return order
    order["total"] = order["total"] * (1 - pct / 100)
    order["discounted"] = True
    return order
