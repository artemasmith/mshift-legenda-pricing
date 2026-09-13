from pricing.discount import apply_discount


def test_discount_not_applied_on_category_mismatch():
    order = {"total": 1000, "category": "electronics", "discounted": False}
    result = apply_discount(order, 10, category="furniture")
    assert result is order
    assert result["total"] == 1000  # NFR-PRICING-002
    assert result["discounted"] is False
