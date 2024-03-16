class Tankpiry:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def check_balance(self):
        print("Баланс танкпиров: ", self.balance)


# Пример использования

tankpiry_account = Tankpiry(100)  # Создание счета с начальным балансом 100 танкпиров
tankpiry_account.check_balance()  # Проверяем баланс
tankpiry_account.deposit(50)  # Вносим 50 танкпиров
tankpiry_account.check_balance()  # Проверяем обновленный баланс
tankpiry_account.withdraw(30)  # Снимаем 30 танкпиров
tankpiry_account.check_balance()  # Проверяем оставшийся баланс
