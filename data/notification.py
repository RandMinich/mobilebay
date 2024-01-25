import datetime

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from data.basic_widget import Based_Widget


class Notification(Based_Widget):
    def __init__(self, type='info', index=0, tytle='', text='', date=datetime.datetime):
        super().__init__()
        self.lay = RelativeLayout()
        self.type = type
        self.index = index
        self.tytle = tytle
        self.text = text
        self.date = date
        tytle = Label(text=self.tytle, color=(0.0, 0.0, 0.0, 1), size_hint=(0.09, 1.9))
        text = Label(text=self.text, color=(0.0, 0.0, 0.0, 1), size_hint=(0.5, 1.5))
        date = Label(text=str(self.date))
        close = Button(text='close', on_press=self.close, pos_hint ={'bottom':0.5, 'right':0.5}, size_hint=(None, None) , size=(70, 40))
        # тип как то будет влиять на внешку
        self.lay.add_widget(tytle)
        self.lay.add_widget(text)
        self.lay.add_widget(close)
