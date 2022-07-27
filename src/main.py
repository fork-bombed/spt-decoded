from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from ui import TicketView, TicketWindow

DARK_PURPLE = [75, 29, 63]
RED = [214, 34, 70]
AERO = [212, 244, 221]
BLUE = [212, 244, 221]
TEAL = [14, 124, 123]

def rgb_to_rgba(rgb: list[int]) -> tuple[int]:
    return tuple([number/255 for number in rgb] + [1])

class Ticketed(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(TicketWindow(name='main'))
        sm.add_widget(TicketView(name='ticket'))
        Window.clearcolor = rgb_to_rgba(DARK_PURPLE)
        return sm

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '400')
Config.write()
LabelBase.register(name='VCR', fn_regular='assets/vcr.ttf')
Ticketed().run()