orders = [
   {"order_id": 1, "status": "оплачен", "amount": 250.75, "buyer": "Алексей"},
   {"order_id": 2, "status": "отменен", "amount": 0, "buyer": "Мария"},
   {"order_id": -1, "status": "оплачен", "amount": 100.50, "buyer": "Иван"},
   {"order_id": 3, "status": "в обработке", "amount": 50.25, "buyer": ""},
   {"order_id": 4, "status": "ошибка", "amount": 300.00, "buyer": "Николай"}
]
def validate_orders(orders: dict):
  result_orders = []
  for i in orders:
      if i['order_id'] > 0 and i['status'] != "ошибка" and i['amount'] > 0 and len(i['buyer']) > 0:
          result_orders.append(i)
  return print(result_orders)

validate_orders(orders)