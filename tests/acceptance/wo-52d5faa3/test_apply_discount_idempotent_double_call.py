from pricing.discount import apply_discount


def test_apply_discount_second_call_is_noop():
    order = {"total": 1000, "category": "X"}
    apply_discount(order, 10)
    result = apply_discount(order, 10)
    assert result is order
    assert order["total"] == 900, "NFR-PRICING-001 violated: discount applied more than once"
    assert order["discounted"] is True
