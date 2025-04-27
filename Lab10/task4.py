from typing import Iterator, Dict, Any

def walk_tree(data: Dict[str, Any]) -> Iterator[str]:
    for key, value in data.items():
        yield key  # Повертаємо поточний ключ
        if isinstance(value, dict):  # Якщо значення є словником
            yield from walk_tree(value)  # Рекурсивно обходимо вкладений словник

# Приклади використання
if __name__ == "__main__":
    tree1 = {"a": {"b": {"c": 1}}, "d": 2}
    print(list(walk_tree(tree1)))  # ['a', 'b', 'c', 'd']

    tree2 = {"x": {"y": {"z": {}}}, "m": {"n": 42}}
    print(list(walk_tree(tree2)))  # ['x', 'y', 'z', 'm', 'n']