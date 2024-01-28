import time

import kivy_garden.mapview as mapview
import requests
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import plyer
import math

from data import notification

# from pyto import *

sm = ScreenManager()
log = False


class RegisterScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = "RegisterScreen"

        register_screen = FloatLayout()
        self.add_widget(register_screen)

        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})

        register_screen.add_widget(
            Label(text='Name and surename', color=(0.0, 0.0, 0.0, 1), size_hint=(None, None), size=(45, 25)))
        self.name_and_last_name = TextInput(multiline=False, size_hint=(None, None), size=(300, 30),
                                            pos_hint={'x': 0.35, 'y': 0.4})
        register_screen.add_widget(self.name_and_last_name)

        self.message = Label(text='', color=(0.0, 0.0, 0.0, 1), size_hint=(None, None), size=(100, 50), pos=(100, 2))
        register_screen.add_widget(self.message)

        register_screen.add_widget(
            Label(text='JMB', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.32, 'y': 0.37},
                  color=(0.0, 0.0, 0.0, 1)))
        self.username = TextInput(multiline=False, size_hint=(None, None), size=(300, 30),
                                  pos_hint={'x': 0.35, 'y': 0.34})
        register_screen.add_widget(self.username)
        register_screen.add_widget(
            Label(text='Password', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.34, 'y': 0.28},
                  color=(0.0, 0.0, 0.0, 1)))
        self.password = TextInput(password=True, multiline=False, size_hint=(None, None), size=(300, 30),
                                  pos_hint={'x': 0.35, 'y': 0.25})
        register_screen.add_widget(self.password)
        register_screen.enter = Button(text="Enter", size_hint=(None, None), size=(70, 40),
                                       pos_hint={'x': 0.45, 'y': 0.15}, background_color=(0.1, 0.1, 0.1, 0.1),
                                       color=(0.0, 0.0, 0.0, 1), on_press=self.send_check)
        register_screen.add_widget(register_screen.enter)

    def send_check(self, *args):
        # try:
        answer = requests.post(
            f'http://randminich.pythonanywhere.com/add_user?name={self.name_and_last_name.text}&login={self.username.text}&password={self.password.text}')
        if answer.text == '+':
            global log
            log = True
            sm.current = 'MainScreen'
        else:
            self.message.text = 'You already register'


class Filler(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'Filler'
        filler_screen = BoxLayout()
        self.add_widget(filler_screen)

        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})
        filler_screen.add_widget(Label(text='Here will be menu of request', color=(0,0,0,1), size=(50, 30)))
        filler_screen.add_widget(Button(text='Escape', size_hint=(None, None), size=(50, 30), pos=(100, 2), on_press=self.to_main))
    def to_main(self, *args):
        sm.current = 'MainScreen'


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = "LoginScreen"

        login_screen = FloatLayout()
        self.add_widget(login_screen)

        # background-color
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})

        self.message = Label(text='', color=(0.0, 0.0, 0.0, 1), size_hint=(None, None), size=(100, 50), pos=(100, 2))
        login_screen.add_widget(self.message)

        login_screen.add_widget(
            Label(text='JMB', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.32, 'y': 0.37},
                  color=(0.0, 0.0, 0.0, 1)))
        self.username = TextInput(multiline=False, size_hint=(None, None), size=(300, 30),
                                  pos_hint={'x': 0.35, 'y': 0.34})
        login_screen.add_widget(self.username)

        login_screen.add_widget(Button(text='register', size_hint=(None, None), size=(50, 25), on_press=self.to_reg))

        login_screen.add_widget(
            Label(text='Password', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.34, 'y': 0.28},
                  color=(0.0, 0.0, 0.0, 1)))
        self.password = TextInput(password=True, multiline=False, size_hint=(None, None), size=(300, 30),
                                  pos_hint={'x': 0.35, 'y': 0.25})
        login_screen.add_widget(self.password)
        login_screen.enter = Button(text="Enter", size_hint=(None, None), size=(70, 40),
                                    pos_hint={'x': 0.45, 'y': 0.15}, background_color=(0.1, 0.1, 0.1, 0.1),
                                    color=(0.0, 0.0, 0.0, 1), on_press=self.send_check)
        login_screen.add_widget(login_screen.enter)

    def send_check(self, *args):
        # try:
        answer = requests.get(
            f'http://randminich.pythonanywhere.com/check?name={self.username.text}&password={self.password.text}')
        if answer.text == '+':
            global log
            log = True
            sm.current = 'MainScreen'
        else:
            self.message.text = 'YOU ENTER WRONG PASSWORD OR JMB'


    def to_main(self, *args):
        sm.current = 'MainScreen'
        return 0

    def to_reg(self, *args, **kwargs):
        sm.current = 'RegisterScreen'
        return 0


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = "MainScreen"

        main_screen = FloatLayout()
        self.add_widget(main_screen)

        # background-color
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})

        main_screen.bell = Button(text="BELL", size_hint=(None, None), size=(80, 80), pos_hint={'x': 0.0, 'y': 0.9},
                                  color=(0.0, 0.0, 0.0, 1), background_color=(0.1, 0.1, 0.1, 0), on_press=self.notifs)
        main_screen.profile = Button(text="USER", size_hint=(None, None), size=(80, 80), pos_hint={'x': 0.92, 'y': 0.9},
                                     color=(0.0, 0.0, 0.0, 1), background_color=(0.1, 0.1, 0.1, 0), on_press=self.to_filler)
        main_screen.docs = Button(text="docs", size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.2, 'y': 0.75},
                                  color=(0.0, 0.0, 0.0, 1), on_press=self.to_filler)
        main_screen.helthcare = Button(text="Hospital\nrequest", size_hint=(None, None), size=(100, 100),
                                       pos_hint={'x': 0.45, 'y': 0.75}, color=(0.0, 0.0, 0.0, 1), on_press=self.to_filler)
        # main_screen.taxes = Button(text="taxes") Здесь я хз что делать поэтому просто закоментил и ниже тоже самое
        main_screen.more = Button(text="more", size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.7, 'y': 0.75},
                                  color=(0.0, 0.0, 0.0, 1), on_press=self.to_filler)
        main_screen.map = Button(text="map", size_hint=(None, None), size=(600, 300), pos_hint={'x': 0.2, 'y': 0.325},
                                 color=(0.0, 0.0, 0.0, 1), on_press=self.to_map)
        main_screen.text1 = Button(text="passport", size_hint=(None, None), size=(250, 150),
                                   pos_hint={'x': 0.2, 'y': 0.1}, color=(0.0, 0.0, 0.0,
                                                                         1), on_press=self.to_filler)  # Паспорт + права в кнопку надо сделать, я заменю, но просто чтобы ты не искал, они должны по-сути переводить на эти два раздела документов
        main_screen.text2 = Button(text="driver licence", size_hint=(None, None), size=(250, 150),
                                   pos_hint={'x': 0.55, 'y': 0.1}, color=(0.0, 0.0, 0.0, 1), on_press=self.to_filler)
        main_screen.help = Button(text="help", size_hint=(None, None), size=(50, 20), pos_hint={'x': 0.48, 'y': 0.02},
                                  color=(0.0, 0.0, 0.0, 1), background_color=(0.1, 0.1, 0.1, 0), on_press=self.to_filler)
        main_screen.add_widget(main_screen.help)
        main_screen.add_widget(main_screen.text1)
        main_screen.add_widget(main_screen.text2)
        main_screen.add_widget(main_screen.map)
        main_screen.add_widget(main_screen.more)
        # main_screen.add_widget(main_screen.taxes)
        main_screen.add_widget(main_screen.helthcare)
        main_screen.add_widget(main_screen.docs)
        main_screen.add_widget(main_screen.bell)
        main_screen.add_widget(main_screen.profile)

        # radius i ne tolko
        '''
        self.main_screen.docs.setStyleSheet (
            """"
            border-top-left-radius: {5};
            border-bottom-left-radius: {5};
            border-top-right-radius: {5};
            border-bottom=right-radius: {5};
            """
        )
        '''

    def to_filler(self, *args):
        sm.current = 'Filler'

    def to_map(self, *args):
        sm.current = 'MapScreen'

    def notifs(self, *args):
        sm.current = 'Notifications'


notification_list = [('Attention', 'fsffwfwfffgsdgdgddgdgdfg'), ('Warning', 'fsffwfwfffgsdgdgddgdgdfg')]


class Notifications(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'Notifications'
        self.notifications = []
        notification_screen = BoxLayout(orientation='vertical')
        self.add_widget(Label(text='Notifications', color=(0, 0, 0, 1)))
        self.add_widget(Button(text='escape', size=(70, 40), size_hint=(None, None), on_press=self.to_main))
        self.add_widget(notification_screen)
        for i in notification_list:
            self.notifications.append(notification.Notification(tytle=i[0], text=i[1]).show())
        for i in self.notifications:
            notification_screen.add_widget(i)
        if len(notification_list) == 0:
            self.add_widget(Label(text='Empty', color=(0, 0, 0, 1)))

        # background-color
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})

    def to_main(self, *args):
        sm.current = 'MainScreen'
        return 0


class Documents(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        documents_screen = FloatLayout()
        self.documents = []
        for i in self.documents:
            documents_screen.add_widget(i)

    def to_main(self, *args):
        sm.current = 'MainScreen'
        return 0


class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'LoadingScreen'
        # requests.get('запрос к серверу на получение уведомлений')
        if log:
            self.change()

    def change(self, **kwargs):
        time.sleep(10)
        sm.current = 'MainScreen'


class Services(Screen):

    def __init__(self, **kwargs):
        super().__init__()


#          Хз как представить список услуг, думаю на каждую услугу свое окно а тут типо списка

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'MapScreen'
        self.text = TextInput(multiline=False)
        # gps.configure(on_location=self.check)
        # gps.start()
        self.map = mapview.MapView(lat=42.4381206, lon=19.2562048, zoom=11, size=(500, 400), size_hint=(None, None),
                                   pos=(50, 300))
        self.adding = Button(text='Add', size=(70, 40), size_hint=(None, None), pos=(600, 100))
        self.adding.bind(on_press=self.add_thing)
        self.p = Image(source='marker_const.png', size_hint=(None, None), pos=(600, 100))
        self.add_widget(self.adding)
        self.add_widget(self.map)
        self.escape = Button(text='Escape', on_press=self.to_main, size_hint=(None, None), size=(50, 50), pos=(500, 40))
        self.add_widget(self.escape)

        self.pop = Popup(title='Your description of event', size_hint=(None, None), size=(400, 400),
                         auto_dismiss=False)

    
    def check(self, **kwargs):
        c = requests.get('http://randminich.pythonanywhere.com/get_coords').json()
        lat = kwargs['lat']
        lon = kwargs['lon']
        for i in c:
            if i.lan > lat - 0.0001 and i.lan < lat + 0.0001 and i.lon > lon - (
                    (111111 * math.cos(math.radians(lon)) * 0.0001) / 111111) \
                    and i.lon < lon + (
                    (111111 * math.cos(math.radians(lon)) * 0.0001) / 111111):
                notification_list.append(notification.Notification().show())
                plyer.notification.notify(title='Warning', message="Уходи оттуда")

    def add_thing(self, *args):
        self.accept_button = Button(text='acept', on_press=self.text_entering, size_hint=(None, None), size=(50, 50))
        self.add_widget(self.accept_button)
        self.add_widget(self.p)

    def text_entering(self, *args):
        content = BoxLayout()
        content.add_widget(TextInput(multiline=False, size_hint=(None, None), size=(300, 30)))
        content.add_widget(Button(text='close', size_hint=(None, None), size=(30, 30), on_press=self.pop.dismiss))
        self.pop.content = content
        self.pop.bind(on_dismiss=self.send_event)
        self.pop.open()

    def send_event(self, *args):
        self.remove_widget(self.p)
        text = self.text
        data = {'lan': self.map.lat, 'lon': self.map.lon, 'author': '', 'text': text}
        self.remove_widget(self.accept_button)
        requests.post('http://randminich.pythonanywhere.com/geo', data)

    def to_main(self, *args):
        sm.current = 'MainScreen'
        return 0


class MyApp(App):

    def build(self):
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(MainScreen())
        sm.add_widget(Notifications())
        sm.add_widget(LoadingScreen())
        sm.add_widget(MapScreen())
        sm.add_widget(Filler())
        # schedule.every(1).minute.run(MapScreen().check())
        return sm


if __name__ == '__main__':
    MyApp().run()

# prosto
