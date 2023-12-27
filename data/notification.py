import datetime
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from main import Notifications

class Notification:
    def __init__(self, type='info', index=0, tytle='', text='', date=datetime.datetime):
        self.type = type
        self.index = index
        self.tytle = tytle
        self.text = text
        self.date = date
        self.lay = AnchorLayout()
        tytle = Label(text=self.tytle)
        text = Label(text=self.text)
        date = Label(text=self.date)
        close = Button(text='close', on_press=self.close)
        #тип как то будет влиять на внешку
        self.lay.add_widget(tytle)
        self.lay.add_widget(text)
        self.lay.add_widget(close)

    def show(self):
        return self.lay

    def close(self):
        self.lay.parent.remove_widget(self.lay)


