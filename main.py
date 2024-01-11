import plyer
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import kivy_garden.mapview as mapview
from plyer import gps
from data import notification

sm = ScreenManager()


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = "LoginScreen"

        login_screen = FloatLayout()
        self.add_widget(login_screen)

        login_screen.add_widget(Label(text='User Name'))
        login_screen.username = TextInput(multiline=False)
        login_screen.add_widget(login_screen.username)
        login_screen.add_widget(Label(text='password'))
        login_screen.password = TextInput(password=True, multiline=False)
        login_screen.add_widget(login_screen.password)
        login_screen.enter = Button(text="Enter")
        login_screen.enter.bind(on_press=self.send_check)
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

        main_screen.bell = Button(text="BELL")
        main_screen.profile = Button(text="USER")
        main_screen.docs = Button(text="docs")
        main_screen.helthcare = Button(text="Hospital\nrequest")
        main_screen.taxes = Button(text="taxes")
        main_screen.more = Button(text="more")
        main_screen.map = Button(text="map")
        main_screen.text1 = Label(text="Text1")
        main_screen.text2 = Label(text="Text2")
        main_screen.help = Button(text="help")
        main_screen.add_widget(main_screen.help)
        main_screen.add_widget(main_screen.text1)
        main_screen.add_widget(main_screen.text2)
        main_screen.add_widget(main_screen.map)
        main_screen.add_widget(main_screen.more)
        main_screen.add_widget(main_screen.taxes)
        main_screen.add_widget(main_screen.helthcare)
        main_screen.add_widget(main_screen.docs)
        main_screen.add_widget(main_screen.bell)
        main_screen.add_widget(main_screen.profile)

notification_list = [('fuck'),('you')]
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
        requests.get('запрос к серверу на получение уведомлений')
        # запрос документов тут и тп


class Services(Screen):

    def __init__(self, **kwargs):
        super().__init__()


#          Хз как представить список услуг, думаю на каждую услугу свое окно а тут типо списка

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'MapsScreen'
        gps.configure(on_location=self.check)
        gps.start()
        self.map = mapview.MapView(lat=42.4381206, lon=19.2562048)

    def check(self, **kwargs):
        c = requests.get('/get_coords').json()
        for i in c:
            if i.lan == kwargs['lat'] and i.lon == kwargs['lon']:
                plyer.notification.notify(title='Warning', message="Уебывай оттуда")



class MyApp(App):

    def build(self):
        # sm.add_widget(LoginScreen())
        # sm.add_widget(MainScreen())
        sm.add_widget(Notifications())
        return sm


if __name__ == '__main__':
    MyApp().run()
