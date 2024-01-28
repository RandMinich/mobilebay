import datetime
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from main import Notifications

class Based_Widget:
    def __init__(self, *args, **kwargs):
        self.lay = AnchorLayout()

    def show(self, *args):
        return self.lay

    def close(self, *args):
        self.lay.parent.remove_widget(self.lay)
