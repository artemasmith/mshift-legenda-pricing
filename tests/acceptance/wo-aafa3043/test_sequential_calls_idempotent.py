"""Acceptance test for claim C5 (NFR-PRICING-001): two sequential calls must not compound the discount."""
from pricing.discount import apply_discount


def test_sequential_calls_do_not_double_discount():
    order = {"total": 1000, "category": "X"}
    apply_discount(order, 10)
    result = apply_discount(order, 10)
    assert result["total"] == 900
    assert result is order
    assert order["discounted"] is True
