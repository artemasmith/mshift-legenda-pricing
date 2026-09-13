from pricing.discount import apply_discount

def test_apply_discount_pct_zero_boundary():
    order = {'total': 1000}
    result = apply_discount(order, 0)
    assert result is order
    assert result['total'] == 1000, 'pct=0 must leave total unchanged'
    assert result['discounted'] is True

def test_apply_discount_pct_hundred_boundary():
    order2 = {'total': 1000}
    result2 = apply_discount(order2, 100)
    assert result2 is order2
    assert result2['total'] == 0, 'pct=100 must reduce total to zero'
    assert result2['discounted'] is True
