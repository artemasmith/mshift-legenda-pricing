# mypy: ignore-errors
# Фикстура бенчмарка: репозиторий-двойник, не код продукта.

"""Ценообразование заказа."""


def apply_discount(order, pct, category=None):
    """Применить скидку к заказу.

    Правила:
    - если order уже уценён (discounted is True) — вернуть без изменений;
    - если category передана и не совпадает с order['category'] — вернуть без изменений;
    - иначе применить скидку pct к order['total'], выставить discounted=True.
    """
    if not (0 <= pct <= 100):
        raise ValueError("pct must be within 0..100")

    if order.get("discounted") is True:
        return order

    if category is not None and order.get("category") != category:
        return order

    order["total"] = round(order["total"] * (1 - pct / 100), 2)
    order["discounted"] = True
    return order
