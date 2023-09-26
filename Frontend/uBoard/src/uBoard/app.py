"""
Crossplatform frontend of the uboard
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import httpx

def pieceAdder(name):
    if name: return f"{name} have been added"
    else: return "Can't be added"

def pieceFinder(selv, widget):
    with httpx.Client() as client:
        reponse = client.get("http://127.0.0.1:8000/piece/")
    payload = reponse.json()

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
        buttonShow = toga.Button("show me your piece", on_press=self.pieceOfMind, style=Pack(padding=5)) #this is also funny because its a pun!
        
        main_box.add(name_box)
        main_box.add(button)
        main_box.add(buttonShow)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    async def pieceOfMind(self, widget): #it's still funny because its a pun!
        with httpx.AsyncClient() as client:
            #response = client.get("http://127.0.0.1:8000/piece/")
            response = await client.get("http://127.0.0.1:8000/piece/6510af927f02845b2fdf708a")
            #response = client.get("https://jsonplaceholder.typicode.com/posts/42")
        
        payload = response.json()
        
        self.main_window.info_dialog(pieceAdder(self.name_input.value), "{name}: ({x},{y}), Size={size}".format(name=payload["name"], x=payload["xPos"], y=payload["yPos"], size=payload["size"]),)
    



def main():
    return uBroardSurface()
