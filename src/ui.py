from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.graphics.svg import Svg
from spt import Ticket

class SvgWidget(Scatter):
    filename = ""
    def __init__(self):
        super(SvgWidget, self).__init__()
        with self.canvas:
            svg = Svg(self.filename)
        self.size = svg.width, svg.height

class PixButton(Button):
    offset = 20
    def pixel_press(self, instance):
        instance.ids.image.source = 'assets/button_pressed.png'
        for child in instance.children:
            if isinstance(child, Label):
                child.pos = (child.x, child.y - self.offset)
        
    def pixel_release(self, instance):
        instance.ids.image.source = 'assets/button.png'
        for child in instance.children:
            if isinstance(child, Label):
                child.pos = (child.x, child.y + self.offset)

class TicketWindow(Screen):
    def __init__(self, **kwargs):
        super(TicketWindow, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if self.ids.bytes_input.focus and keycode == 40:
            self.decode()
    def clear_text(self):
        self.ids.bytes_input.text = ''
    def decode(self):
        ticket = Ticket(self.ids.bytes_input.text)
        self.manager.transition.direction = "left"
        self.manager.current = 'ticket'
        self.manager.screens[1].ids.fare_type.text = ticket.fare_type.upper()
        self.manager.screens[1].ids.journey_type.text = ticket.journey_type.upper()
        self.manager.screens[1].ids.uid.text = ticket.uid
        self.manager.screens[1].ids.fare.text = ticket.fare_type.capitalize()
        self.manager.screens[1].ids.cost.text = ticket.cost
        self.manager.screens[1].ids.journey.text = ticket.journey_type.capitalize()
        self.manager.screens[1].ids.date.text = ticket.date.strftime('%d %b %y')
        self.manager.screens[1].ids.station.text = ticket.last_station
        self.manager.screens[1].ids.uses.text = str(ticket.uses_left)
        self.manager.screens[1].ids.hash.text = ticket.hash


class TicketView(Screen):
    pass

# class TicketWindow(Widget):
#     def clear_text(self):
#         self.ids.bytes_input.text = ''
