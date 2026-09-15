"""Acceptance test for claim C4 (NFR-PRICING-002): discount applies and flag is set when category matches."""
from pricing.discount import apply_discount


def test_category_match_applies_discount_and_sets_flag():
    order = {"total": 1000, "category": "X", "discounted": False}
    result = apply_discount(order, 10, category="X")
    assert result["total"] == 900
    assert result is order
    assert order["discounted"] is True
