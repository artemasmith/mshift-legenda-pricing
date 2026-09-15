from pricing.discount import apply_discount


def test_apply_discount_signature_backward_compatible():
    order = {"total": 1000, "category": "X"}
    result = apply_discount(order, 10)
    assert result is order
    assert order["total"] == 900
    order2 = {"total": 500, "category": "Z"}
    result2 = apply_discount(order2, 20, category=None)
    assert result2 is order2
    assert order2["total"] == 400
