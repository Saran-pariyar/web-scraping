from cProfile import label
from io import open_code
from turtle import onclick
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs): # we used ***kwargs for adding unlimited argument(example: spread operator in js)
        super(childApp,self).__init__()
        self.cols = 2

        self.add_widget(Label(text = "Student Name"))
        self.s_name=TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text = "Student Age"))
        self.s_age=TextInput()
        self.add_widget(self.s_age)

        self.press = Button(text="Click me!")
        self.press.bind(onclick = self.click_me)
        self.add_widget(self.press)

        def click_me(self,instance):
            print("Name of the student is " + self.s_name.text)


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()