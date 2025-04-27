from typing import Iterable


def capitalize_words(words: Iterable[str]) -> Iterable[str]:
    return map(str.capitalize, words)


def main():
    # Введення даних від користувача
    input_str = input("Введіть рядки через кому (наприклад: python,java,c++): ")

    # Розділення введених даних на список рядків
    words_list = [word.strip() for word in input_str.split(',')]

    # Виклик функції capitalize_words
    capitalized = capitalize_words(words_list)

    # Виведення результату
    print("Результат:", list(capitalized))


if __name__ == "__main__":
    main()