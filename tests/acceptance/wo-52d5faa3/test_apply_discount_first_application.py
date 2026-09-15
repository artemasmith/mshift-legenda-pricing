from pricing.discount import apply_discount


def test_apply_discount_first_application():
    order = {"total": 1000, "category": "X"}
    result = apply_discount(order, 10)
    assert result is order
    assert order["total"] == 900
    assert order["discounted"] is True
