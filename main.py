'''
Simply ToDo, a simple ToDo list app by Carter Weems
'''

from kivy.app import App
from kivy.uix.widget import Widget


class SimplyTodo(Widget):
    pass


class SimplyTodoApp(App):
    def build(self):
        return SimplyTodo()


if __name__ == '__main__':
    SimplyTodoApp().run()
