def filter_long_words(words: list[str]) -> list[str]:
    filtered_words = filter(lambda word: len(word) > 3, words)
    return list(filtered_words)

# Приклади виклику функції
print(filter_long_words(["a", "the", "code", "Python", "is", "fun"]))
print(filter_long_words(["cat", "dog", "fish", "go", "egg"]))
print(filter_long_words(["", "aa", "bbb", "cccc", "ddddd"]))
print(filter_long_words([]))