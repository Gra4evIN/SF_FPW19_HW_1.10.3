class Customers:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def savings_money(self, money):
        self.balance += money

    def withdraw_money(self, money):
        if self.balance > 0 and money <= self.balance:
            self.balance -= money
        else:
            return print('Недостаточно средств!', 'Текущий баланс: ' + str(self.balance) + 'руб')

        def print_balance(self):
            return (f'Клиент: "{self.name}", Баланс: {self.balance}, руб.')
