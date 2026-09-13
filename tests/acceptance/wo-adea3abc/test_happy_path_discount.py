from pricing.discount import apply_discount


def test_happy_path_discount_applied_once():
    order = {"total": 1000, "category": "electronics", "discounted": False}
    result = apply_discount(order, 10, category="electronics")
    assert result is order
    assert result["total"] == 900
    assert result["discounted"] is True
