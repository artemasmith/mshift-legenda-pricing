from pricing.discount import apply_discount


def test_category_mismatch_no_discount():
    order = {"total": 1000, "category": "A", "discounted": False}
    result = apply_discount(order, 10, category="B")
    assert result["total"] == 1000, "NFR-PRICING-002 violated: discount applied despite category mismatch"
    assert result.get("discounted") is False
