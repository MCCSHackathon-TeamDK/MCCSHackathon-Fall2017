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

        self.current_person = 0
        self.edited_interests = []
        self.edited_gifts_to = []
        self.edited_gifts_from = []
        self.edited_family = []

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

        self.name_entry = self.builder.get_variable("name_entry_text")
        self.age_entry = self.builder.get_variable("age_entry_text")
        self.relationship_entry = self.builder.get_variable("relationship_entry_text")
        self.interest_list = self.builder.get_object("interest_listbox")
        self.gifts_to_list = self.builder.get_object("gifts_to_listbox")
        self.gifts_from_list = self.builder.get_object("gifts_from_listbox")
        self.family_list = self.builder.get_object("family_listbox")

        # Button Configuration
        self.save_button = self.builder.get_object("save_button")
        self.save_button.configure(command=self.gui_save_person)
        self.next_button = self.builder.get_object("next_button")
        self.next_button.configure(command=self.gui_add_interest)

        # Add interest toplevel config
        self.interest_toplevel = self.builder.get_object("add_interest_toplevel")
        add_interest_save_button = self.builder.get_object("add_interest_done_button")
        add_interest_save_button.configure(command=self.gui_add_interest)
        add_interest_cancel_button = self.builder.get_object("add_interest_cancel_button")
        add_interest_cancel_button.configure(command=self.interest_toplevel.withdraw)
        add_interest_button = self.builder.get_object("add_interest_button")
        add_interest_button.configure(command=self.interest_toplevel.deiconify)
        self.add_interest_entry_text = self.builder.get_variable("add_interest_entry_text")

        self.gui_show_person()

        root.mainloop()

    def gui_save_person(self):
        """
        Saves edited information to the person
        :return: None
        """
        person = self.people[self.current_person]
        person.age = self.age_entry.get()
        person.name = self.name_entry.get()
        person.relationship = self.relationship_entry.get()
        person.interests.extend(self.edited_interests)
        person.gifts_given.extend(self.edited_gifts_to)
        person.gifts_received.extend(self.edited_gifts_from)
        person.family.extend(self.edited_family)

        person.save_person("people")

        self.edited_interests.clear()
        self.edited_gifts_to.clear()
        self.edited_gifts_from.clear()
        self.edited_family.clear()

    def gui_add_person(self):
        pass

    def gui_edit_person(self):
        pass

    def gui_show_person(self):
        person = self.people[self.current_person]
        self.name_entry.set(person.name)
        self.age_entry.set(str(person.age))
        self.relationship_entry.set(person.relationship)

        for interest in person.interests:
            self.interest_list.insert(END, interest)

        for gift in person.gifts_given:
            self.gifts_to_list.insert(END, gift.name)

        for family_member in person.family:
            person = next((x for x in self.people if x.id == family_member[1]), None)
            self.family_list.insert(END, person.name)

    def gui_add_gift(self):
        """
        Adds a gift to this person. This function is responsible for adding it to their class
        :return:
        """
        pass

    def gui_edit_gift(self):
        pass

    def gui_add_interest(self):
        interest_text = self.add_interest_entry_text.get()
        self.edited_interests.append(interest_text)
        self.interest_list.insert(END, interest_text)
        self.interest_toplevel.withdraw()

    def save_people(self, people):
        """
        Saves the people to files
        :param people: List of people to save
        :return: None
        """
        if not os.path.exists("people"):
            os.mkdir("people")

        for person in people:
            person.save_person("people")

    def load_people(self, people):
        """
        Loads the people files from a previous session if they exist
        :param people: people list to put data into
        :return: None
        """
        if not os.path.exists("people"):
            return

        for file in os.listdir("people"):
            people.append(Person("people/" + file))


if __name__ == "__main__":
    GiftGudGUI()
