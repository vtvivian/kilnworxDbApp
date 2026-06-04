"""
Kilnworx members check-in system
"""

import toga
from toga.style.pack import COLUMN, ROW
from kilnworxDbApp.db_main import db_main
from pathlib import Path

class KilnworxMembersDatabase(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(direction=COLUMN,flex=1)

        name_label = toga.Label(
            "Your name: ",
            margin=(0, 5),
        )
        self.name_input = toga.TextInput(flex=1)

        name_box = toga.Box(direction=ROW, margin=5)
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Check in!",
            on_press=self.check_in,
            margin=5,
        )

        msg_box = toga.Box(margin=10)
        self.msg_label = toga.Label(
            "Welcome to Kilnworx!",
            margin=(0, 5),
        )
        msg_box.add(self.msg_label)

        self.msg_table = toga.Table(columns=["Column1", "Column2"], data=[("", "")], show_headings=False, flex=1)


        main_box.add(name_box)
        main_box.add(button)
        main_box.add(msg_box)
        main_box.add(self.msg_table)

        self.main_window = toga.MainWindow(title=self.formal_name,size=(800, 600))
        self.main_window.content = main_box
        self.main_window.show()

    def check_in(self, widget):
        name_in = self.name_input.value
        # print(f"Hello, {nameIn}")
        self.msg_label.text = f"Hello, {name_in}"

        # Excel database file path
        filepath_db = self.paths.app / "resources" / "db.xlsx"

        msgOut = self.update_db(name_in,filepath_db)
        # Creat printable output
        # msgOut = [
        #     ("r1c1", 'r1c2'),
        #     ("r2c1", 'r2c2'),
        #     ("r3c1", 'r3c2'),
        # ]
        self.msg_table.data = msgOut
        print(msgOut)

    def update_db(self,name_in,filepath_db):
        # Calling the external function directly
        msg_out = db_main(name_in,filepath_db)
        return msg_out



def main():
    return KilnworxMembersDatabase()
