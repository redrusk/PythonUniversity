class CashRegister:
    def __init__(self, initial_amount=0):
        if initial_amount < 0:
            raise ValueError("Начальная сумма не может быть отрицательной.")
        self._balance = initial_amount

    def top_up(self, x):
        if x < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной.")
        self._balance += x

    def count_1000(self):
        return self._balance // 1000

    def take_away(self, x):
        if x < 0:
            raise ValueError("Сумма снятия не может быть отрицательной.")
        if x > self._balance:
            raise ValueError(
                f"Недостаточно денег в кассе. Требуется: {x}, доступно: {self._balance}"
            )
        self._balance -= x

    @property
    def balance(self):
        return self._balance
