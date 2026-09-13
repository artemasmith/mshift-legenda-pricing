from pricing.discount import apply_discount


def test_pct_is_call_parameter_not_constant():
    order1 = {"total": 1000, "category": "toys", "discounted": False}
    order2 = {"total": 1000, "category": "toys", "discounted": False}
    r1 = apply_discount(order1, 10)
    r2 = apply_discount(order2, 20)
    assert r1["total"] == 900
    assert r2["total"] == 800
    assert r1["total"] != r2["total"]  # NFR-PRICING-004
