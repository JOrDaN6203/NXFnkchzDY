# 代码生成时间: 2025-10-11 03:34:21
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
import math

"""
价格计算引擎程序

该程序使用Kivy框架创建一个简单的图形界面，用户可以输入数量和单价，
程序将计算总价格并展示结果。

功能：
1. 输入数量和单价
2. 计算总价格
3. 显示结果

错误处理：
- 检查输入是否为数字
- 处理除法时的除以零错误

作者：[你的名字]
创建日期：[创建日期]
"""

class PriceCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='数量'))
        self.quantity_input = TextInput(multiline=False)
        self.add_widget(self.quantity_input)
        self.add_widget(Label(text='单价'))
        self.unit_price_input = TextInput(multiline=False)
        self.add_widget(self.unit_price_input)
        self.calculate_button = Button(text='计算')
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)
        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def calculate(self, instance):
        """计算总价格"""
        try:
            quantity = float(self.quantity_input.text)
            unit_price = float(self.unit_price_input.text)
            total_price = quantity * unit_price
            self.result_label.text = f'总价格为：{total_price}元'
        except ValueError:
            # 输入不是数字
            self.show_error_popup('输入必须为数字')
        except ZeroDivisionError:
            # 除以零错误
            self.show_error_popup('单价不能为0')

    def show_error_popup(self, error_message):
        "