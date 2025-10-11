# 代码生成时间: 2025-10-12 02:28:20
# 数据脱敏工具
# 用于将给定的字符串中的敏感信息进行脱敏处理

import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# 敏感信息脱敏函数
def mask_sensitive_info(text, mask_char='*'):
    """
    对给定的字符串进行脱敏处理，将敏感信息替换为mask_char
    :param text: 原始字符串
    :param mask_char: 用于替换敏感信息的字符，默认为'*'
    :return: 脱敏后的字符串
    """
    # 定义敏感信息的正则表达式
    sensitive_pattern = r'\w+'  # 这里可以根据需要自定义敏感信息的正则表达式
    
    return re.sub(sensitive_pattern, lambda m: mask_char * len(m.group()), text)

# Kivy主程序类
class DataMaskingApp(App):
    def build(self):
        # 创建一个水平布局
        layout = BoxLayout(orientation='horizontal')
        
        # 创建输入框，用于输入原始字符串
        self.input_text = TextInput(multiline=False)
        layout.add_widget(self.input_text)
        
        # 创建脱敏按钮
        mask_button = Button(text='Mask Sensitive Info')
        mask_button.bind(on_press=self.mask_sensitive_info)
        layout.add_widget(mask_button)
        
        # 创建标签，用于显示脱敏后的字符串
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        
        return layout
    
    def mask_sensitive_info(self, instance):
        # 获取输入框中的原始字符串
        original_text = self.input_text.text
        
        # 进行脱敏处理
        masked_text = mask_sensitive_info(original_text)
        
        # 在标签中显示脱敏后的字符串
        self.result_label.text = f'Masked Text: {masked_text}'

# 程序入口
if __name__ == '__main__':
    DataMaskingApp().run()