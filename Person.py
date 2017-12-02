import json


class Person:

    def __init__(self, name, age=None, relationship=None):
        """
        Initializes the person class with a person's name, age, and relationship.
        This will only be used when creating a new person that has not been added yet, as people who have already been
        added will be stored in JSON files.
        :param name: Name of this person
        :param age: Age of this person
        :param relationship: Relationship of this person to the user
        """
        if age is None or relationship is None:
            self.name = name
            self.age = age
            self.relationship = relationship
            self.no_gift_rule = False
            self.gifts = []
            self.interests = []
            self.family = []  # List of tuples (relationship to this person, their person object)
        else:


    def save_person(self):
        """
        Saves this person to a JSON file
        :return:
        """
        with open(self.name + '.txt', 'w') as outfile:
            json.dump(self, outfile)

    def load_person(self, name):
        json_dict = json.load(name)

    def add_family_member(self, role, person):
        """
        Adds a family member to this person
        :return:
        """
        self.family.append((role, person))

    def add_gift(self):
        """
        Records a gift that this person has given
        :return:
        """
        pass
