"""Acceptance test for claim C2 (NFR-PRICING-001): a discounted order must not be discounted again."""
from pricing.discount import apply_discount


def test_discounted_order_is_not_discounted_again():
    order = {"total": 1000, "category": "X", "discounted": True}
    result = apply_discount(order, 50)
    assert result["total"] == 1000
    assert result is order
    assert order["discounted"] is True
