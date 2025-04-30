def sort_by_age(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda person: person['age'])


def input_people():
    people = []
    print("Введіть дані про людей (для завершення введіть 'done'):")
    while True:
        name = input("Ім'я: ")
        if name.lower() == 'done':
            break
        age = int(input("Вік: "))
        people.append({"name": name, "age": age})
    return people


def main():
    print("Програма сортування людей за віком")
    print("--------------------------------")

    people = input_people()

    if not people:
        print("Не введено жодної людини.")
        return

    sorted_people = sort_by_age(people)

    print("\nРезультат сортування:")
    for person in sorted_people:
        print(f"{person['name']}: {person['age']} років")


if __name__ == "__main__":
    main()