import json
import re
import pytest
from jsonpath_ng import parse

@pytest.fixture(scope="module")
def data():
    with open("orders.json") as f:
        return json.load(f)

def test_order_has_non_empty_id(data):
    ids = [match.value for match in parse("$.orders[*].id").find(data)]
    assert all(i and i.strip() for i in ids)

def test_status_valid(data):
    valid_status = {"PAID", "PENDING", "CANCELLED"}
    statuses = [match.value for match in parse("$.orders[*].status").find(data)]
    assert all(s in valid_status for s in statuses)

def test_customer_email_format(data):
    email_re = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    emails = [match.value for match in parse("$.orders[*].customer.email").find(data)]
    for e in emails:
        if e:
            assert email_re.match(e), f"Invalid email: {e}"

def test_lines_integrity(data):
    for order in data["orders"]:
        if order["status"] in ("PAID", "PENDING"):
            assert order["lines"], f"Order {order['id']} has empty lines"
            for line in order["lines"]:
                assert line["sku"], "Missing SKU"
                assert line["qty"] > 0, "Quantity must be > 0"
                assert line["price"] >= 0, "Price must be >= 0"

def test_payment_refund_consistency(data):
    for order in data["orders"]:
        if order["status"] == "PAID":
            assert order["payment"]["captured"] is True
        if order["status"] == "CANCELLED" and order.get("lines"):
            total = sum(l["qty"] * l["price"] for l in order["lines"])
            assert order["refund"]["amount"] == total or order["refund"]["amount"] == 0

def test_shipping_fee(data):
    fees = [match.value for match in parse("$.orders[*].shipping.fee").find(data)]
    assert all(fee >= 0 for fee in fees)
