from pricing.discount import apply_discount

def test_apply_discount_category_mismatch_no_effect():
    order = {'total': 1000, 'category': 'A'}
    result = apply_discount(order, 10, category='B')
    assert result is order
    assert result['total'] == 1000, 'discount must not apply when requested category differs from order category'
    assert result['category'] == 'A'
