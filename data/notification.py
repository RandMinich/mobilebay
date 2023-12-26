import datetime
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

class Notification:
    def __init__(self, type='info', tytle='', text='', date=datetime.datetime):
        self.type = type
        self.tytle = tytle
        self.text = text
        self.date = date

    def show(self):
        lay = AnchorLayout()
        tytle = Label(text=self.tytle)
        text = Label(text=self.text)
        date = Label(text=self.date)
        close = Button(text='close')
        #тип как то будет влиять на внешку
        lay.add_widget(tytle)
        lay.add_widget(text)
        lay.add_widget(close)
        return lay

