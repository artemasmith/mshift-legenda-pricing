"""Acceptance test for claim C1: basic discount application stays correct and sets the discounted flag."""
from pricing.discount import apply_discount


def test_basic_discount_applies_and_sets_flag_and_same_object():
    order = {"total": 1000, "category": "X"}
    result = apply_discount(order, 10)
    assert result["total"] == 900
    assert result is order
    assert order["discounted"] is True
