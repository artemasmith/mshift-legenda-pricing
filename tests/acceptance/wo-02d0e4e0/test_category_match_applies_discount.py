"""C3: discount must be applied when requested category matches order category."""
from pricing.discount import apply_discount


def test_category_match_applies_discount():
    order = {"total": 1000, "category": "X", "discounted": False}
    result = apply_discount(order, 10, category="X")
    assert result["total"] == 900, "NFR-PRICING-002 violated: discount not applied on category match"
    assert result["discounted"] is True
    assert result is order
