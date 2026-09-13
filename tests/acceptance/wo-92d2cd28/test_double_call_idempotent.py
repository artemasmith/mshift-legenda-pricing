from pricing.discount import apply_discount


def test_apply_discount_twice_is_idempotent():
    order = {"total": 1000, "category": "std"}
    apply_discount(order, 10)
    total_after_first = order["total"]
    apply_discount(order, 10)
    assert order["total"] == total_after_first, "NFR-PRICING-001 violated: second call re-applied discount"
