from pricing.discount import apply_discount


def test_discounted_order_not_discounted_again():
    order = {"total": 1000, "category": "std", "discounted": True}
    original_total = order["total"]
    result = apply_discount(order, 10)
    assert result["total"] == original_total, "NFR-PRICING-001 violated: total changed on already-discounted order"
    assert result["discounted"] is True
