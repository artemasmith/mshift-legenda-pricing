from pricing.discount import apply_discount


def test_apply_discount_does_not_reapply_when_already_discounted():
    order = {"total": 1000, "category": "X", "discounted": True}
    result = apply_discount(order, 50)
    assert result is order
    assert order["total"] == 1000, "NFR-PRICING-001 violated: discount re-applied to already discounted order"
    assert order["discounted"] is True
