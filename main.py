import kivy
from kivy.app import App 
from kivy.uix.label import Label    
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#  Creating Grid Layout 
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        #  Adding elements - columns
        self.cols = 2 #Defining the amount of columns to be 2
        self.add_widget(Label(text="First Name: ")) # Add a label widget
        self.name = TextInput(multiline=False) # Create a Text input box stored in the name variable
        self.add_widget(self.name) # Add the text input widget to the GUI

        self.add_widget(Label(text="Last Name: ")) # Add a label widget
        self.name = TextInput(multiline=False) # Create a Text input box stored in the name variable
        self.add_widget(self.lastName) # Add the text input widget to the GUI

        self.add_widget(Label(text="Email: ")) # Add a label widget
        self.name = TextInput(multiline=False) # Create a Text input box stored in the name variable
        self.add_widget(self.email) # Add the text input widget to the GUI

class MyApp(App):
    def build(self):
        return MyGrid()

# Created window -low level for test-
if __name__ == "__main__":
    MyApp().run()