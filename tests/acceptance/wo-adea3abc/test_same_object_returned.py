from pricing.discount import apply_discount


def test_apply_discount_mutates_and_returns_same_object():
    order = {"total": 1000, "category": "books", "discounted": False}
    result = apply_discount(order, 10, category="books")
    assert result is order  # NFR-PRICING-005
    assert id(result) == id(order)
