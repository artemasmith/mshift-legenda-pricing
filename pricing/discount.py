"""Ценообразование заказа."""


def apply_discount(order, pct, category=None):
    """Применить скидку к заказу.

    Скидка не применяется повторно к уже уценённому заказу.
    Если передана category и она не совпадает с order['category'],
    заказ не изменяется.
    """
    if order.get("discounted") is True:
        return order
    if category is not None and category != order.get("category"):
        return order
    order["total"] = order["total"] * (1 - pct / 100)
    order["discounted"] = True
    return order
