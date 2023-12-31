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
from kivy.uix.popup import Popup
from data.basic_widget import Based_Widget

class Category(Based_Widget):
    def __init__(self):
        super().__init__()
        open_list = Button(text='', on_press=self.opening_of_list)
        self.everyone=[]

    def opening_of_list(self):
        #тут должна быть раскладка элементов
        pass

    def add_element(self, obj):
        self.everyone.append(obj)