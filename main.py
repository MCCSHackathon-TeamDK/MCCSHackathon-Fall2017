from Person import Person
from Gift import Gift
from datetime import datetime

def main():
    test_guy = Person("tommy", age=11, relationship="friend")

    test_guy.save_person()

    test_again = Person(name="tommy")

    print(test_again.name)
    print(test_again.age)
    print(test_again.family)
    print(test_again.interests)
    print(test_again.no_gift_rule)

    print("stuff")
    print(send_card(test_guy))
    test_guy.add_gift(Gift("christmas card", 0, 2016, 144))
    print(send_card(test_guy))

def send_card(person):
    """
    Checks if person sent a card last year
    """
    year = datetime.now().year
    for gift in person.gifts:
        if gift.is_card() and gift.year == year - 1 and not person.no_gift_rule:
            return True
    return False

if __name__ == "__main__":
    main()
