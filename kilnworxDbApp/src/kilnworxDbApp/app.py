"""
Kilnworx members check-in system
"""

import toga
from toga.style.pack import COLUMN, ROW

class KilnworxMembersDatabase(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(direction=COLUMN)

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

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(msg_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def check_in(self, widget):
        print(f"Hello, {self.name_input.value}")
        self.msg_label.text = f"Hello, {self.name_input.value}"


def main():
    return KilnworxMembersDatabase()
