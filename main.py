from Person import Person
from Gift import Gift
from datetime import datetime

def main():
    test_guy = Person("tommy", age=11, relationship="friend")
    test_guy.add_gift(Gift("meme", 100, 2015, 144))
    test_guy.add_gift(Gift("another meme", 20, 2016, 145))
    test2 = Person("bob", age=50, relationship="father")
    test2.add_gift(Gift("Test", 2, 2016, 146))
    test2.add_gift(Gift("2test", 50, 2011, 147))
    testlist = [test_guy, test2]

    for person in generate_gift_list(testlist, 2010, 25):
        print(person.name)

    test_guy.save_person()

    test_again = Person(name="tommy")

    print(test_again.name)
    print(test_again.age)
    print(test_again.family)
    print(test_again.interests)
    print(test_again.no_gift_rule)

def send_card(person):
    """
    Checks if person sent a card last year
    """
    year = datetime.now().year
    for gift in person.gifts:
        if gift.is_card() and gift.year == year - 1 and not person.no_gift_rule:
            return True
    return False

def generate_gift_list(people, year_given, price_limit):
    result = list()
    for person in people:
        for gift in person.gifts:
            if gift.year > year_given and gift.price > price_limit and person not in result and not person.no_gift_rule:
                result.append(person)

    return result

if __name__ == "__main__":
    main()
