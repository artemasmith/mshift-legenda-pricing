from pricing.discount import apply_discount


def test_no_double_discount_on_already_discounted_order():
    order = {"total": 900, "category": "electronics", "discounted": True}
    original_total = order["total"]
    result = apply_discount(order, 10, category="electronics")
    assert result is order
    assert result["total"] == original_total  # NFR-PRICING-001
    assert result["discounted"] is True
