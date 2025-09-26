import json
import pytest
from collections import Counter
from jsonpath_ng import parse

@pytest.fixture(scope="module")
def data():
    with open("orders.json") as f:
        return json.load(f)

def test_list_order_ids(data):
    ids = [m.value for m in parse("$.orders[*].id").find(data)]
    assert ids == ["A-1001", "A-1002", "A-1003", "A-1004", "A-1005"]

def test_total_line_items(data):
    line_counts = [len(order["lines"]) for order in data["orders"]]
    assert sum(line_counts) == 8

def test_top_2_skus(data):
    counter = Counter()
    for order in data["orders"]:
        for line in order["lines"]:
            if line["qty"] > 0:
                counter[line["sku"]] += line["qty"]
    top2 = counter.most_common(2)
    assert top2 == [("PEN-RED", 5), ("USB-32GB", 2)]

def test_gmv_per_order(data):
    gmvs = {}
    for order in data["orders"]:
        gmvs[order["id"]] = sum(line["qty"] * line["price"] for line in order["lines"])
    assert gmvs == {
        "A-1001": 70.0,
        "A-1002": 0.0,
        "A-1003": -15.0, # invalid, should be flagged separately
        "A-1004": 16.0,
        "A-1005": 55.0
    }

def test_orders_missing_or_invalid_emails(data):
    bad_orders = []
    for order in data["orders"]:
        email = order.get("customer", {}).get("email")
        if not email or "@" not in email:
            bad_orders.append(order["id"])
    assert bad_orders == ["A-1002", "A-1003"]
