"""C5: calling apply_discount twice on the same order must not double the discount."""
from pricing.discount import apply_discount


def test_repeated_call_does_not_double_discount():
    order = {"total": 1000, "category": "X"}
    apply_discount(order, 10)
    assert order["total"] == 900
    result = apply_discount(order, 10)
    assert result["total"] == 900, "NFR-PRICING-001 violated: second call changed total again"
    assert result["discounted"] is True
    assert result is order
