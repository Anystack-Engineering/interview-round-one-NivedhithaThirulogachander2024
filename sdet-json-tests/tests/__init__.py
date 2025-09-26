{
  "orders": [
    {
      "id": "A-1001",
      "status": "PAID",
      "customer": { "email": "john@example.com" },
      "lines": [
        { "sku": "PEN-RED", "qty": 2, "price": 10 },
        { "sku": "BOOK-ENG", "qty": 1, "price": 50 }
      ],
      "payment": { "captured": true },
      "shipping": { "fee": 5 }
    },
    {
      "id": "A-1002",
      "status": "PENDING",
      "customer": { },
      "lines": [],
      "payment": { "captured": false },
      "shipping": { "fee": 0 }
    },
    {
      "id": "A-1003",
      "status": "CANCELLED",
      "customer": { "email": "invalid-email" },
      "lines": [
        { "sku": "USB-32GB", "qty": 0, "price": 15 }
      ],
      "refund": { "amount": -15 },
      "shipping": { "fee": 0 }
    },
    {
      "id": "A-1004",
      "status": "PAID",
      "customer": { "email": "mary@example.com" },
      "lines": [
        { "sku": "PEN-BLUE", "qty": 2, "price": 8 }
      ],
      "payment": { "captured": true },
      "shipping": { "fee": 2 }
    },
    {
      "id": "A-1005",
      "status": "PAID",
      "customer": { "email": "alex@example.com" },
      "lines": [
        { "sku": "PEN-RED", "qty": 3, "price": 10 },
        { "sku": "USB-32GB", "qty": 2, "price": 12.5 }
      ],
      "payment": { "captured": true },
      "shipping": { "fee": 3 }
    }
  ]
}
