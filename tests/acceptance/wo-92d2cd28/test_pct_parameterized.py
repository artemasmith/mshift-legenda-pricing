import pytest
from pricing.discount import apply_discount


@pytest.mark.parametrize("pct,expected_total", [(10, 900), (20, 800), (50, 500)])
def test_pct_is_used_as_parameter_not_hardcoded(pct, expected_total):
    order = {"total": 1000, "category": "std"}
    result = apply_discount(order, pct)
    assert result["total"] == expected_total, "NFR-PRICING-003 violated: pct not applied as parameter"
