from typing import Iterable

def capitalize_words(words: Iterable[str]) -> Iterable[str]:
    # Використовуємо map() з функцією str.capitalize() для кожного елементу
    return map(str.capitalize, words)

# Приклади використання
print(list(capitalize_words(["why", "are", "you","mad"])))
