import inspect
from pricing.discount import apply_discount

def test_apply_discount_signature_backward_compatible():
    sig = inspect.signature(apply_discount)
    params = list(sig.parameters.values())
    assert [p.name for p in params[:2]] == ['order', 'pct']
    assert 'category' in sig.parameters
    assert sig.parameters['category'].default is None
    order = {'total': 1000}
    result = apply_discount(order, 10)
    assert result is order
    assert result['total'] == 900
