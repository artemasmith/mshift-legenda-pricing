from pricing.discount import apply_discount

def test_apply_discount_not_applied_twice():
    order = {'total': 1000, 'discounted': True}
    result = apply_discount(order, 10)
    assert result is order
    assert result['total'] == 1000, 'discount must not be applied to an already discounted order'
    assert result['discounted'] is True
