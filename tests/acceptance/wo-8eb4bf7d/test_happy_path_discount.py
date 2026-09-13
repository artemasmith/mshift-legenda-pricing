from pricing.discount import apply_discount

def test_apply_discount_happy_path_no_category():
    order = {'total': 1000}
    result = apply_discount(order, 10)
    assert result is order, 'apply_discount must mutate and return the same order object'
    assert result['total'] == 900, 'total must be reduced by pct percent'
