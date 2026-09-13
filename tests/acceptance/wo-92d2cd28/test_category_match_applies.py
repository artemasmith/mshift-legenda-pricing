from pricing.discount import apply_discount


def test_category_match_applies_discount():
    order = {"total": 1000, "category": "A", "discounted": False}
    result = apply_discount(order, 10, category="A")
    assert result["total"] == 900, "NFR-PRICING-002 violated: discount not applied on matching category"
    assert result["discounted"] is True
