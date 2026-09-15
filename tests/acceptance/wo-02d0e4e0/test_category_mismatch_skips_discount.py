"""C2: discount must be skipped when requested category does not match order category."""
from pricing.discount import apply_discount


def test_category_mismatch_skips_discount():
    order = {"total": 1000, "category": "Y", "discounted": False}
    result = apply_discount(order, 10, category="X")
    assert result["total"] == 1000, "NFR-PRICING-002 violated: discount applied despite category mismatch"
    assert result["discounted"] is False
    assert result is order
