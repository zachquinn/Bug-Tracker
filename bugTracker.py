import os
import json
from tkinter import *
from tkinter import ttk
from tabulate import tabulate

path = "BugReports/"


def create_tracker():
    if not os.path.exists(path):
        os.mkdir(path)
    name = input(
        "Please enter the name of the project you would like to create a tracker for:\n"
    )
    f = open(path + name + (".json"), "x")

    print("Please enter the following in order to add a bug:")
    bug = input("Class, Method, Line, Description:\n")
    bug = bug.split()
    dictionary = {
        "Class": bug[0],
        "Method": bug[1],
        "Line": bug[2],
        "Description": bug[3],
    }
    js_obj = json.dumps(dictionary, indent=4)
    with open(path + name + (".json"), "w") as outfile:
        outfile.write(js_obj)
    print_tracker(name)


def print_tracker(name):
    f = open(path + name + (".json"), "r")
    print("Bugs currently in ", name)
    for x in f:
        print(x)


def load_tracker(*args):
    pass


def main():
    print(
        "Please choose an option from the following by entering the corresponding number:"
    )
    selection = 0
    while True:
        try:
            selection = input(
                "1.) Create new Bug List \n2.) View/Modify existing Bug List \n3.) Quit\n"
            )
            selection = int(selection)
            if selection == 1:
                create_tracker()
            elif selection == 2:
                load_tracker()
            elif selection == 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nNot a valid integer! Please try again ...")
    pass


if __name__ == "__main__":
    main()


"""
root = Tk()
root.title("Bug Tracker")
frm = ttk.Frame(root, padding="3 3 12 12")
frm.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(frm, text="Welcome to BugTracker V1").grid(column=1, row=0)
ttk.Button(frm, text="Create Tracker", command=create_tracker).grid(column=0, row=1)
ttk.Button(frm, text="Load Tracker", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1, sticky=E)
root.mainloop()
"""
