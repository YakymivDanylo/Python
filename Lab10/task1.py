def filter_even_numbers(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]

# Вхідні дані з консолі
input_numbers = list(map(int, input("Введіть список чисел через пробіл: ").split()))
print("Парні числа:", filter_even_numbers(input_numbers))