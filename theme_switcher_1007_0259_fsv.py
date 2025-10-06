# 代码生成时间: 2025-10-07 02:59:22
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty
from kivy.core.window import Window


class ThemeSwitcherApp(App):
    themes = ListProperty(["default", "dark"])  # Available themes
    current_theme = "default"  # Default theme

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen(name='theme_screen', ThemeScreen()))
        return sm

    def switch_theme(self, theme):
        """Switches the theme of the application."""
        if theme in self.themes:
            self.current_theme = theme
            Window.clearcolor = self.get_theme_color(theme)
            self.root.ids.theme_button.text = theme.title()
        else:
            raise ValueError("Theme not found")

    def get_theme_color(self, theme):
        """Returns the background color for a given theme."""
        if theme == "dark":
            return (0, 0, 0, 1)  # Black
        else:
            return (1, 1, 1, 1)  # White


class ThemeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ThemeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.add_widget(Button(text='Switch to Dark Theme', on_press=self.switch_to_dark))
        self.add_widget(Button(text='Switch to Default Theme', on_press=self.switch_to_default))

        self.theme_button = Button(text=self.root.current_theme.title())
        self.add_widget(self.theme_button)

    def switch_to_dark(self, instance):
        """Switches the theme to dark."""
        self.root.switch_theme('dark')

    def switch_to_default(self, instance):
        """Switches the theme to default."""
        self.root.switch_theme('default')

    def on_touch_down(self, touch):
        """Catch touch down event to change theme."""
        if touch.is_double_tap and self.collide_point(*touch.pos):
            self.root.switch_theme('dark' if self.root.current_theme == 'default' else 'default')
            return True
        return super(ThemeScreen, self).on_touch_down(touch)


if __name__ == '__main__':
    ThemeSwitcherApp().run()
