from pricing.discount import apply_discount


def test_boundary_pct_full_discount():
    order = {"total": 500, "category": "books", "discounted": False}
    result = apply_discount(order, 100)
    assert result["total"] == 0  # NFR-PRICING-003
    assert result["discounted"] is True
