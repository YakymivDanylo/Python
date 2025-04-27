class Countdown:
    def __init__(self, start: int):
        self.current = start if start >= 0 else -1  # Якщо start від'ємний, відразу встановлюємо -1

    def __iter__(self):
        return self  # Повертаємо сам об'єкт як ітератор

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Зупиняємо ітерацію для від'ємних значень
        value = self.current
        self.current -= 1
        return value


if __name__ == "__main__":
    # Тестування з прикладів
    c = Countdown(5)
    for number in c:
        print(number, end=' ')  # Виведе: 5 4 3 2 1 0
    print()

    print(list(Countdown(6)))   # Виведе: [3, 2, 1, 0]
    print(list(Countdown(0)))   # Виведе: [0]
    print(list(Countdown(-3)))  # Виведе: []