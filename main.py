from Person import Person


def main():
    test_guy = Person("tommy", age=11, relationship="friend")

    test_guy.save_person()

    test_again = Person(name="tommy")

    print(test_again.name)
    print(test_again.age)
    print(test_again.family)
    print(test_again.interests)
    print(test_again.no_gift_rule)


if __name__ == "__main__":
    main()
