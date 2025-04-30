from typing import Iterator


def float_range(start: float, stop: float, step: float) -> Iterator[float]:
    if step == 0:
        raise ValueError("step cannot be 0")

    current = start

    # Визначаємо кількість знаків після крапки в start і step
    def count_decimals(number: float) -> int:
        if '.' not in str(number):
            return 0
        return len(str(number).split('.')[1].rstrip('0'))

    decimals = max(count_decimals(start), count_decimals(step))

    if step > 0:
        while current < stop:
            yield round(current, decimals)
            current += step
    else:
        while current > stop:
            yield round(current, decimals)
            current += step


if __name__ == "__main__":
    print(list(float_range(1.0, 2.0, 0.3)))
    print(list(float_range(5.0, 3.0, -0.5)))
    print(list(float_range(0.0, 1.0, 0.1))[:3])
    print(list(float_range(0.0, 0.003, 0.001)))