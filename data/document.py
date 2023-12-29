import datetime
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from main import Notifications
from data.basic_widget import Based_Widget

class Documents(Based_Widget):
    def __init__(self, type='info', tytle='', text='', image=''):
        super().__init__()
        self.type = type
        self.tytle = tytle
        self.text = text
        self.image = image
        tytle = Label(text=self.tytle)
        text = Label(text=self.text)
        image = Image(image=self.image)
        close = Button(text='close', on_press=self.close)
        self.lay.add_widget(tytle)
        self.lay.add_widget(text)
        self.lay.add_widget(image)
        self.lay.add_widget(close)