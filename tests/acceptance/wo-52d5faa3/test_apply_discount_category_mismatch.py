from pricing.discount import apply_discount


def test_apply_discount_skips_when_category_mismatch():
    order = {"total": 1000, "category": "Y", "discounted": False}
    result = apply_discount(order, 10, category="X")
    assert result is order
    assert order["total"] == 1000, "NFR-PRICING-002 violated: discount applied to mismatched category"
    assert order["discounted"] is False
