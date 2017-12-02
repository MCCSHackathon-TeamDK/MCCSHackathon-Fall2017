import tkinter
from tkinter import Tk, Menu, Label, END

import os
import pygubu

from Person import Person


class GiftGudGUI:

    def __init__(self):

        # Value initialization

        self.people = []
        self.load_people(self.people)

        # GUI initialization

        root = Tk()

        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('GiftGudGUI.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('gift_gud_frame', root)

        # menu = Menu(root)
        # root.config(menu=menu)
        #
        # file_menu = Menu(menu)
        # menu.add_cascade(label="File", menu=file_menu)
        # file_menu.add_command(label="Add Person", command=self.gui_add_person)
        # file_menu.add_command(label="Add Gift", command=self.gui_add_gift)

        # person

        self.name_text = self.builder.get_variable("name_text")
        self.age_text = self.builder.get_variable("age_text")
        self.relationship_text = self.builder.get_variable("relationship_text")
        self.interest_list = self.builder.get_object("interests_list")
        self.gifts_to_list = self.builder.get_object("gifts_given_list")
        self.gifts_from_list = self.builder.get_object("gifts_from_list")
        self.family_list = self.builder.get_object("family_list")

        self.interest_list.insert(END, "ba da boom")

        root.mainloop()

        self.gui_show_person(self.people[0])

    def gui_add_person(self):
        pass

    def gui_edit_person(self):
        pass

    def gui_show_person(self, person):
        self.name_text = person.name
        self.age_text = str(person.age)
        self.relationship_text = person.relationship

        for interest in person.interests:
            self.interest_list.insert(END, interest)

        for gift in person.gifts_given:
            self.gifts_to_list.insert(END, gift.name)

        for family_member in person.family:
            person = next((x for x in self.people if x.id == family_member[1]), None)
            self.family_list.insert(END, person.name)

    def gui_add_gift(self):
        pass

    def gui_edit_gift(self):
        pass

    def save_people(self, people):
        if not os.path.exists("people"):
            os.mkdir("people")

        for person in people:
            person.save_person("people")

    def load_people(self, people):
        for file in os.listdir("people"):
            people.append(Person("people/" + file))


if __name__ == "__main__":
    GiftGudGUI()