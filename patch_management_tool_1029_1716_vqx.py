# 代码生成时间: 2025-10-29 17:16:05
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
import os
import subprocess
import shutil

# Patch Management Tool
class PatchManagementToolApp(App):
    
    def build(self):
        # Main layout
        self.main_layout = BoxLayout(orientation='vertical')
        
        # Patch file selector
        self.patch_file_input = TextInput(multiline=False)
        self.patch_file_button = Button(text='Select Patch File')
        self.patch_file_button.bind(on_press=self.select_patch_file)
        
        # Patch status label
        self.patch_status_label = Label(text='No patch selected')
        
        # Apply patch button
        self.apply_patch_button = Button(text='Apply Patch')
        self.apply_patch_button.bind(on_press=self.apply_patch)
        
        # Add widgets to the main layout
        self.main_layout.add_widget(self.patch_file_input)
        self.main_layout.add_widget(self.patch_file_button)
        self.main_layout.add_widget(self.patch_status_label)
        self.main_layout.add_widget(self.apply_patch_button)
        
        return self.main_layout
    
    def select_patch_file(self, instance):
        # Open file dialog to select patch file
        file_path = Window.open_file对话框(
            filters={'Patch Files': ['*.patch']})
        if file_path:
            self.patch_file_input.text = file_path
            self.patch_status_label.text = 'Patch file selected: ' + file_path
        else:
            self.patch_status_label.text = 'No patch selected'
    
    def apply_patch(self, instance):
        # Get the selected patch file path
        patch_file_path = self.patch_file_input.text
        if not patch_file_path:
            self.show_error_popup('No patch file selected')
            return
        
        # Apply the patch using the patch command
        try:
            subprocess.run(['patch', '-p1', '-i', patch_file_path], check=True)
            self.patch_status_label.text = 'Patch applied successfully'
        except subprocess.CalledProcessError as e:
            self.show_error_popup(f'Failed to apply patch: {e}')
        except Exception as e:
            self.show_error_popup(f'An error occurred: {e}')
    
    def show_error_popup(self, message):
        # Show error popup with the given message
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# Run the Patch Management Tool App
if __name__ == '__main__':
    PatchManagementToolApp().run()