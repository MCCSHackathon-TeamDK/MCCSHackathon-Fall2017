from Person import Person


def main():
    test_guy = Person("tommy", age=11, relationship="friend")

    test_guy.save_person()


if __name__ == "__main__":
    main()
