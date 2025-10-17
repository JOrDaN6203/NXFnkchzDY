# 代码生成时间: 2025-10-17 20:20:44
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import os
import shutil

# AI模型版本管理类
class ModelVersionManager:
    def __init__(self):
        self.models_dir = 'models'  # AI模型存储目录
        self.current_version = None  # 当前版本

    def load_models(self):
        """加载所有AI模型版本"""
        models = []
        for version in sorted(os.listdir(self.models_dir)):
            models.append((version, os.path.isdir(os.path.join(self.models_dir, version))))
        return models

    def create_version(self, version_name):
        """创建新版本目录"""
        new_version_path = os.path.join(self.models_dir, version_name)
        if os.path.exists(new_version_path):
            raise ValueError(f'版本 {version_name} 已存在')
        os.mkdir(new_version_path)
        return new_version_path

    def delete_version(self, version_name):
        """删除指定版本目录"""
        version_path = os.path.join(self.models_dir, version_name)
        if not os.path.exists(version_path):
            raise FileNotFoundError(f'版本 {version_name} 不存在')
        shutil.rmtree(version_path)

    def switch_version(self, version_name):
        """切换到指定版本"""
        version_path = os.path.join(self.models_dir, version_name)
        if not os.path.exists(version_path):
            raise FileNotFoundError(f'版本 {version_name} 不存在')
        self.current_version = version_name

# Kivy应用界面
class ModelVersionApp(App):
    def build(self):
        layout = GridLayout()
        layout.cols = 1

        self.model_versions = ModelVersionManager()
        self.model_list = BoxLayout()
        self.model_list.orientation = 'vertical'

        # 版本列表
        self.version_label = Label(text='模型版本列表:')
        self.model_list.add_widget(self.version_label)

        self.version_scroll = ScrollView()
        self.version_scroll.add_widget(FileChooserListView(size_hint_y=None, height=200))
        self.model_list.add_widget(self.version_scroll)

        # 创建版本按钮
        create_version_btn = Button(text='创建新版本')
        create_version_btn.bind(on_press=self.create_version)
        self.model_list.add_widget(create_version_btn)

        # 删除版本按钮
        delete_version_btn = Button(text='删除选中版本')
        delete_version_btn.bind(on_press=self.delete_version)
        self.model_list.add_widget(delete_version_btn)

        # 切换版本按钮
        switch_version_btn = Button(text='切换到选中版本')
        switch_version_btn.bind(on_press=self.switch_version)
        self.model_list.add_widget(switch_version_btn)

        layout.add_widget(self.model_list)

        self.update_version_list()
        return layout

    def update_version_list(self):
        """更新版本列表"""
        version_list = self.model_versions.load_models()
        for version in version_list:
            btn = Button(text=version[0])
            btn.bind(on_press=lambda btn, v=version: self.select_version(v))
            self.version_scroll.add_widget(btn)

    def create_version(self, instance):
        """创建新版本"""
        version_name = input('请输入新版本名称:')
        try:
            self.model_versions.create_version(version_name)
            self.update_version_list()
        except ValueError as e:
            print(e)

    def delete_version(self, instance):
        """删除选中版本"""
        selected_version = self.version_scroll.selected
        if not selected_version:
            print('请先选中一个版本')
            return
        try:
            self.model_versions.delete_version(selected_version)
            self.update_version_list()
        except FileNotFoundError as e:
            print(e)

    def switch_version(self, instance):
        """切换到选中版本"""
        selected_version = self.version_scroll.selected
        if not selected_version:
            print('请先选中一个版本')
            return
        try:
            self.model_versions.switch_version(selected_version)
            print(f'切换到版本 {self.model_versions.current_version}')
        except FileNotFoundError as e:
            print(e)

    def select_version(self, version):
        """选中版本"""
        self.version_scroll.selected = version[0]

# 运行Kivy应用
def main():
    ModelVersionApp().run()

if __name__ == '__main__':
    main()