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
        if age is not None and relationship is not None:
            self.name = name
            self.age = age
            self.relationship = relationship
            self.no_gift_rule = False
            self.gifts = []
            self.interests = []
            self.family = []  # List of tuples (relationship to this person, their person object)
        else:
            self.load_person(name)

    def save_person(self):
        """
        Saves this person to a JSON file
        :return:
        """
        with open(self.name + '.txt', 'w') as outfile:
            json.dump(self.__dict__, outfile)

    def load_person(self, name):
        with open(name + ".txt") as json_file:
            json_dict = json.load(json_file)

            self.name = json_dict["name"]
            self.age = int(json_dict["age"])
            self.relationship = json_dict["relationship"]
            self.no_gift_rule = json_dict["no_gift_rule"]
            self.gifts = json_dict["gifts"]  # TODO make sure this loads the gift class correctly
            self.interests = json_dict["interests"]
            self.family = json_dict["family"]  # TODO get this to work with linking to people

    def add_family_member(self, role, person):
        """
        Adds a family member to this person
        :return:
        """
        self.family.append((role, person))

    def add_gift(self, gift):
        """
        Records a gift that this person has given
        :return:
        """
        self.gifts.append(gift)
