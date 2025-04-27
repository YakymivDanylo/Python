def filter_long_words(words: list[str]) -> list[str]:
    # Використовуємо filter() з lambda-функцією, яка перевіряє довжину слова > 3
    filtered_words = filter(lambda word: len(word) > 3, words)
    # Перетворюємо результат filter() у список і повертаємо
    return list(filtered_words)

# Приклади виклику функції
print(filter_long_words(["a", "the", "code", "Python", "is", "fun"]))  # ['code', 'Python']
print(filter_long_words(["cat", "dog", "fish", "go", "egg"]))         # ['fish']
print(filter_long_words(["", "aa", "bbb", "cccc", "ddddd"]))         # ['cccc', 'ddddd']
print(filter_long_words([]))                                          # []