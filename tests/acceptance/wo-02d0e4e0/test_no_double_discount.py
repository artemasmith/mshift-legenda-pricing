"""C1: already-discounted order must be returned unchanged."""
from pricing.discount import apply_discount


def test_discounted_order_unchanged_by_new_discount():
    order = {"total": 1000, "category": "X", "discounted": True}
    result = apply_discount(order, 50)
    assert result["total"] == 1000, "NFR-PRICING-001 violated: total changed on already-discounted order"
    assert result["discounted"] is True
    assert result is order
