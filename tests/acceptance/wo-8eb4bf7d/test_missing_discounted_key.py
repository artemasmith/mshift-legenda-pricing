from pricing.discount import apply_discount

def test_apply_discount_missing_discounted_key_treated_as_false():
    order = {'total': 1000}
    assert 'discounted' not in order
    result = apply_discount(order, 10)
    assert result is order
    assert result['total'] == 900, 'missing discounted key must be treated as not-discounted, so discount applies'
    assert result['discounted'] is True
