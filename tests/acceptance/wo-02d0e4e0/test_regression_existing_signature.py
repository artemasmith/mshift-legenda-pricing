"""C4: regression - legacy two-arg call and explicit category=None must keep working."""
from pricing.discount import apply_discount


def test_existing_signature_and_behaviour_preserved():
    order = {"total": 1000, "category": "X"}
    result = apply_discount(order, 10)
    assert result["total"] == 900
    assert result is order

    order2 = {"total": 500, "category": "Z"}
    result2 = apply_discount(order2, 10, category=None)
    assert result2["total"] == 450
    assert result2 is order2
