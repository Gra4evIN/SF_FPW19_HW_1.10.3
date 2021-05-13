from e_wallet import Customers

byuer_1 = Customers("Boris Mikhailov", 0)
print(byuer_1.balance)

byuer_1.savings_money(60)
print(byuer_1.balance)

byuer_1.withdraw_money(35)
print(byuer_1.balance)
