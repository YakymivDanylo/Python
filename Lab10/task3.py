from typing import Iterator


def float_range(start: float, stop: float, step: float) -> Iterator[float]:
    """
    Генератор послідовності чисел з плаваючою крапкою, аналогічний range(), але для float.

    Args:
        start: Початкове значення послідовності
        stop: Кінцеве значення (не включається)
        step: Крок зміни значень

    Yields:
        Наступне число у послідовності

    Raises:
        ValueError: Якщо step == 0
    """
    if step == 0:
        raise ValueError("step cannot be 0")

    current = start
    decimals = max(len(str(step).split('.')[1]), len(str(start).split('.')[1])) if '.' in str(step) or '.' in str(
        start) else 0

    if step > 0:
        while current < stop:
            yield round(current, 10)  # округлення для уникнення проблем з точністю
            current += step
    else:
        while current > stop:
            yield round(current, 10)  # округлення для уникнення проблем з точністю
            current += step


# Приклади використання з умови
if __name__ == "__main__":
    # Приклад 1: Крок додатній, від 1.0 до 2.0 (не включно)
    print(list(float_range(1.0, 2.0, 0.3)))  # [1.0, 1.3, 1.6, 1.9]

    # Приклад 2: Крок від'ємний, від 5.0 до 3.0 (не включно)
    print(list(float_range(5.0, 3.0, -0.5)))  # [5.0, 4.5, 4.0, 3.5]

    # Приклад 3: Малий крок 0.1, беремо тільки перші 3 елементи
    print(list(float_range(0.0, 1.0, 0.1))[:3])  # [0.0, 0.1, 0.2]