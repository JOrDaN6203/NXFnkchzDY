# 代码生成时间: 2025-10-15 16:35:24
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
System Backup and Restore Tool using Python and Kivy

This script provides a simple GUI to backup and restore system settings.
It includes error handling, necessary comments, and follows Python best practices.
"""

import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup

class BackupRestoreApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Label for instructions
        instructions_label = Label(text='Click on the backup or restore button to start.')
        
        # File chooser for backup and restore
        self.backup_restore_dir = FileChooserListView(size_hint=(1, 0.3))
        self.backup_restore_dir.filters = ['*.zip']
        
        # Backup button
        backup_btn = Button(text='Backup', size_hint=(1, 0.2))
        backup_btn.bind(on_press=self.backup)
        
        # Restore button
        restore_btn = Button(text='Restore', size_hint=(1, 0.2))
        restore_btn.bind(on_press=self.restore)
        
        # Add widgets to the main layout
        main_layout.add_widget(instructions_label)
        main_layout.add_widget(self.backup_restore_dir)
        main_layout.add_widget(backup_btn)
        main_layout.add_widget(restore_btn)
        
        return main_layout
    
    def backup(self, instance):
        # Get the selected directory path
        selected_path = self.backup_restore_dir.path
        if not selected_path:
            self.show_error('Please select a directory to save the backup.')
            return
        
        # Create a backup
        try:
            backup_file = f'backup_{os.path.basename(selected_path)}.zip'
            shutil.make_archive(backup_file, 'zip', selected_path)
            self.show_success(f'Backup created successfully at {backup_file}.zip')
        except Exception as e:
            self.show_error(f'Error creating backup: {e}')
    
    def restore(self, instance):
        # Get the selected file path
        selected_file = self.backup_restore_dir.selection
        if not selected_file:
            self.show_error('Please select a backup file to restore.')
            return
        
        # Restore from the selected file
        try:
            shutil.unpack_archive(selected_file[0], os.path.dirname(selected_file[0]))
            self.show_success(f'Restored successfully from {selected_file[0]}')
        except Exception as e:
            self.show_error(f'Error restoring backup: {e}')
    
    def show_error(self, message):
        # Show an error popup
        error_popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        error_popup.open()
    
    def show_success(self, message):
        # Show a success popup
        success_popup = Popup(title='Success', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        success_popup.open()

if __name__ == '__main__':
    BackupRestoreApp().run()