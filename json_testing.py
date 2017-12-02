import os

from Person import Person


def save_people(people):
    if not os.path.exists("people"):
        os.mkdir("people")

    for person in people:
        person.save_person("people")


def load_people(people):
    for file in os.listdir("people"):
        people.append(Person("people/" + file))


def json_testing():
    people = [Person("bob", 0, age=11, relationship="friend"), Person("alice", 1, age=11, relationship="friend")]

    people[0].family.append(("sister", 1))

    save_people(people)

    new_people = []

    load_people(new_people)

    for person in people:
        print(person.name)
        print(person.age)
        print(person.family)
        print(person.interests)
        print(person.no_gift_rule)


if __name__ == "__main__":
    json_testing()
