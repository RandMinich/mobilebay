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
import requests

class Making_requests(Based_Widget):
    def __init__(self, name='', image='', type=''):
        super().__init__()
        self.name = name
        self.icon = image
        self.type= type
        image = Image(image=self.icon)
        mr_button = Button(text='make request', on_press=self.up_button)
        name = Label(text=self.name)
        self.lay.add_widget(image)
        self.lay.add_widget(mr_button)
        self.lay.add_widget(name)

    def up_button(self):
        p = Popup(title='')
        p.show()
        if self.type == 1:
            try:
                x = requests.get('')
            except Exception as e:
                p = Popup(title='', content=Label(text=str(e)))
                p.open()
