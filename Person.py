import json


class Person:

    def __init__(self, name, id=None, age=None, relationship=None):
        """
        Initializes the person class with a person's name, age, and relationship.
        This will only be used when creating a new person that has not been added yet, as people who have already been
        added will be stored in JSON files.
        :param name: Name of this person
        :param age: Age of this person
        :param relationship: Relationship of this person to the user
        """
        if id is not None:
            # If an ID was passed we know we are creating a new person
            self.id = id
            self.name = name
            self.age = age
            self.relationship = relationship
            self.no_gift_rule = False
            self.gifts_received = []
            self.gifts_given = []
            self.interests = []
            self.family = []  # List of tuples (relationship to this person, their person id)
        else:
            self.load_person(name)

    def save_person(self, base_directory):
        """
        Saves this person to a JSON file
        :return:
        """
        with open(base_directory + "/" + self.name + '.txt', 'w') as outfile:
            json.dump(self.__dict__, outfile)

    def load_person(self, name):
        """
        Loads this person's data from a JSON file
        :param name:
        :return:
        """
        with open(name) as json_file:
            json_dict = json.load(json_file)

            self.name = json_dict["name"]
            self.age = int(json_dict["age"])
            self.relationship = json_dict["relationship"]
            self.no_gift_rule = json_dict["no_gift_rule"]
            self.gifts_received = json_dict["gifts_received"]
            self.gifts_given = json_dict["gifts_given"]
            self.interests = json_dict["interests"]
            self.family = json_dict["family"]

    def receive_gift(self, gift_id):
        """
        Records a gift as received from this person
        :param gift_id: ID number of the gift
        :return: None
        """
        self.gifts_received.append(gift_id)

    def give_gift(self, gift_id):
        """
        Records a gift as given to this person
        :param gift_id: ID number of the gift
        :return: None
        """
        self.gifts_given.append(gift_id)

    def add_family(self, person_id, relationship):
        """
        Records another person as a member of this person's family
        :param person_id:
        :param relationship:
        :return:
        """
        self.family.append((person_id, relationship))

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
        self.gifts_received.append(gift)
