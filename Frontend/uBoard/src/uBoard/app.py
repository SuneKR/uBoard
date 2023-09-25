"""
Crossplatform frontend of the uboard
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class uBroardSurface(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        name_label = toga.Label("your Piece: ", style=Pack(padding=(0,5)))
        self.name_input = toga.TextInput(style=Pack(flex=1))
        
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        
        button = toga.Button("Give me your piece of mind!", on_press=self.pieceOfMind, style=Pack(padding=5)) #it's funny because its a pun!
        
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    def pieceOfMind(self, widget): #it's still funny because its a pun!
        print(f"{self.name_input.value} have added to a board")



def main():
    return uBroardSurface()
