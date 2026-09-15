"""Acceptance test for claim C3 (NFR-PRICING-002): discount must not apply when category does not match."""
from pricing.discount import apply_discount


def test_category_mismatch_prevents_discount():
    order = {"total": 1000, "category": "Y", "discounted": False}
    result = apply_discount(order, 10, category="X")
    assert result["total"] == 1000
    assert result is order
    assert order["discounted"] is False
