from pricing.discount import apply_discount


def test_apply_discount_applies_when_category_matches():
    order = {"total": 1000, "category": "X", "discounted": False}
    result = apply_discount(order, 10, category="X")
    assert result is order
    assert order["total"] == 900, "NFR-PRICING-002 violated: discount not applied despite matching category"
    assert order["discounted"] is True
