# 代码生成时间: 2025-10-31 20:36:59
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from faker import Faker
import random


class MockDataGeneratorScreen(Screen):
    """
    Mock Data Generator Screen.
    This screen provides a simple UI for generating mock data.
    """
    def __init__(self, **kwargs):
        super(MockDataGeneratorScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.add_mock_data_button()

    def add_mock_data_button(self):
        """
        Adds a button to the layout that generates mock data.
        """
        button = Button(text='Generate Mock Data', on_release=self.generate_mock_data)
        self.layout.add_widget(button)

    def generate_mock_data(self, instance):
        """
        Generates mock data and prints it to the console.
        """
        try:
            fake = Faker()
            data = {
                'name': fake.name(),
                'address': fake.address(),
                'phone_number': fake.phone_number(),
                'email': fake.email()
            }
            print(data)
        except Exception as e:
            print(f"An error occurred: {e}")


class MockDataGeneratorApp(App):
    """
    Mock Data Generator Application.
    This application manages the screens and initializes the UI.
    """
    def build(self):
        sm = ScreenManager()
        mock_data_screen = MockDataGeneratorScreen(name='mock_data')
        sm.add_widget(mock_data_screen)
        return sm


if __name__ == '__main__':
    MockDataGeneratorApp().run()