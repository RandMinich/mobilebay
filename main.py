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



import sys
# from pyto import *
from PyQt5 import QtCore, QtGui, QtWidgets



from data import notification

sm = ScreenManager()


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = "LoginScreen"

        login_screen = FloatLayout()
        self.add_widget(login_screen)

        #background-color
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})

        #здесь должно быть лого!!!
        login_screen.add_widget(Label(text='JMB', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.32, 'y': 0.37}, color=(0.0, 0.0, 0.0, 1)))
        login_screen.username = TextInput(multiline=False, size_hint=(None, None), size=(300, 30), pos_hint={'x': 0.35, 'y': 0.34})
        login_screen.add_widget(login_screen.username)
        login_screen.add_widget(Label(text='Password', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.34, 'y': 0.28}, color=(0.0, 0.0, 0.0, 1)))
        login_screen.password = TextInput(password=True, multiline=False, size_hint=(None, None), size=(300, 30), pos_hint={'x': 0.35, 'y': 0.25})
        login_screen.add_widget(login_screen.password)
        login_screen.enter = Button(text="Enter", size_hint=(None, None), size=(70, 40), pos_hint={'x': 0.45, 'y': 0.15}, background_color=(0.1, 0.1, 0.1, 0.1), color=(0.0, 0.0, 0.0, 1))

        # login_screen.enter.bind(on_press=self.send_check)
        login_screen.add_widget(login_screen.enter)



    def send_check(self):
        try:
            answer = requests.get('')
        except Exception as e:
            e = str(e)
            p = Popup()
            p.title = 'Answer'
            c = Label(text=f'Процесс захода не произведен')
            p.add_widget(c)
            p.show()
            with open('logs.txt') as f:
                f.write(f'\nError: {e}')
            return 0
        self.manager.current = 'LoadingScreen'

    def to_main(self, *args):
        self.manager.current = 'MainScreen'
        return 0


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = "MainScreen"

        main_screen = FloatLayout()
        self.add_widget(main_screen)

        #background-color
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})

        main_screen.bell = Button(text="BELL", size_hint=(None, None), size=(80, 80), pos_hint={'x': 0.0, 'y': 0.9}, color=(0.0, 0.0, 0.0, 1), background_color=(0.1,0.1,0.1,0))
        main_screen.profile = Button(text="USER", size_hint=(None, None), size=(80, 80), pos_hint={'x': 0.92, 'y': 0.9}, color=(0.0, 0.0, 0.0, 1), background_color=(0.1,0.1,0.1,0))
        main_screen.docs = Button(text="docs", size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.2, 'y': 0.75}, color=(0.0, 0.0, 0.0, 1))
        main_screen.helthcare = Button(text="Hospital\nrequest", size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.45, 'y': 0.75}, color=(0.0, 0.0, 0.0, 1))
        # main_screen.taxes = Button(text="taxes") Здесь я хз что делать поэтому просто закоментил и ниже тоже самое
        main_screen.more = Button(text="more", size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.7, 'y': 0.75}, color=(0.0, 0.0, 0.0, 1))
        main_screen.map = Button(text="map", size_hint=(None, None), size=(600,300), pos_hint={'x': 0.2, 'y': 0.325}, color=(0.0, 0.0, 0.0, 1))
        main_screen.text1 = Button(text="passport", size_hint=(None, None), size=(250, 150), pos_hint={'x': 0.2, 'y': 0.1}, color=(0.0, 0.0, 0.0, 1)) # Паспорт + права в кнопку надо сделать, я заменю, но просто чтобы ты не искал, они должны по-сути переводить на эти два раздела документов
        main_screen.text2 = Button(text="driver licence", size_hint=(None, None), size=(250, 150), pos_hint={'x': 0.55, 'y': 0.1}, color=(0.0, 0.0, 0.0, 1))
        main_screen.help = Button(text="help", size_hint=(None, None), size=(50, 20), pos_hint={'x': 0.48, 'y': 0.02}, color=(0.0, 0.0, 0.0, 1), background_color=(0.1,0.1,0.1,0))
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

        #radius i ne tolko
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

notification_list = [('fuck', 'fsffwfwfffgsdgdgddgdgdfg'), ('you', 'fsffwfwfffgsdgdgddgdgdfg')]


class Notifications(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.notifications = []
        notification_screen = BoxLayout(orientation='vertical')
        self.add_widget(notification_screen)
        for i in notification_list:
            self.notifications.append(notification.Notification(tytle=i[0]).show())
        for i in self.notifications:
            notification_screen.add_widget(i)



        #background-color
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the color (RGBA)
            self.rect = Rectangle(size=(1000, 1000), pos_hint={'x': 0.5, 'y': 0.5})


class Documents(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        documents_screen = FloatLayout()
        self.documents = []
        for i in self.documents:
            documents_screen.add_widget(i)


class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'LoadingScreen'
        # requests.get('запрос к серверу на получение уведомлений')
        # запрос документов тут и тп


class Services(Screen):

    def __init__(self, **kwargs):
        super().__init__()


#          Хз как представить список услуг, думаю на каждую услугу свое окно а тут типо списка

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'MapsScreen'
        self.text = TextInput(multiline=False)
        # gps.configure(on_location=self.check)
        # gps.start()
        self.map = mapview.MapView(lat=42.4381206, lon=19.2562048)
        self.adding = Button(text='Add', on_press=self.add_thing)
        self.p = Image(source='marker_const.png')
        self.add_widget(self.adding)
        self.add_widget(self.map)

    '''
    
    def check(self, **kwargs):
        # c = requests.get('/get_coords').json()
        lat = kwargs['lat']
        lon = kwargs['lon']
        for i in c:
            if i.lan > lat - 0.0001 and i.lan < lat + 0.0001 and i.lon > lon - (
                    (111111 * math.cos(math.radians(lon)) * 0.0001) / 111111) \
                    and i.lon < lon + (
                    (111111 * math.cos(math.radians(lon)) * 0.0001) / 111111):
                notification_list.append(notification.Notification().show())
                plyer.notification.notify(title='Warning', message="Уебывай оттуда")
                
                 '''

    def add_thing(self):
        accept_button = Button(text='acept', on_press=self.text_entering)
        self.add_widget(accept_button)
        self.add_widget(self.p)

    def text_entering(self):
        p = Popup(title='Your description of event', content=self.text)
        p.bind(on_dismiss=self.send_event)
        p.open()

    def send_event(self):
        self.remove_widget(self.p)
        text = self.text
        data = {'lan': self.map.lat, 'lon': self.map.lon, 'author': '', 'text': text}
        # requests.post('/geo', data)


class MyApp(App):

    def build(self):
        # sm.add_widget(LoginScreen())
        # sm.add_widget(MainScreen())
        # sm.add_widget(Notifications())
        # sm.add_widget(LoginScreen())
        # sm.add_widget(MainScreen())
        sm.add_widget(Notifications())
        # schedule.every(1).minute.run(MapScreen().check())
        return sm


if __name__ == '__main__':
    MyApp().run()

# prosto