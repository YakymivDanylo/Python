class Countdown:
    def __init__(self, start: int):
        self.current = start if start >= 0 else -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


if __name__ == "__main__":



    print(list(Countdown(6)))
    print(list(Countdown(2)))
    print(list(Countdown(0)))
    print(list(Countdown(-3)))