from pricing.discount import apply_discount


def test_regression_apply_discount_basic():
    order = {"total": 1000, "category": "std"}
    result = apply_discount(order, 10)
    assert result["total"] == 900
    assert result is order
