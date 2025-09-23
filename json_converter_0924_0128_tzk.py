# 代码生成时间: 2025-09-24 01:28:46
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

"""
JSON数据格式转换器
"""


class JsonConverterApp(App):
    def build(self):
        # 创建布局容器
        layout = BoxLayout(orientation='vertical')

        # 创建文本输入框用于输入JSON数据
        self.json_input = TextInput(multiline=True, hint_text='Enter JSON data')
        layout.add_widget(self.json_input)

        # 创建按钮，点击时执行转换操作
        self.convert_button = Button(text='Convert')
        self.convert_button.bind(on_press=self.convert_json)
        layout.add_widget(self.convert_button)

        # 创建标签显示转换结果
        self.result_label = Label(text='Result will be shown here')
        layout.add_widget(self.result_label)

        return layout

    def convert_json(self, instance):
        # 获取输入框中的JSON数据
        json_data = self.json_input.text

        # 尝试解析JSON数据
        try:
            # 使用json.loads()函数解析JSON字符串
            data = json.loads(json_data)
            # 将解析后的数据转换为字符串，并显示在标签中
            self.result_label.text = json.dumps(data, indent=4)
        except json.JSONDecodeError as e:
            # 如果解析失败，显示错误信息
            self.result_label.text = f'Error: {str(e)}'

# 运行应用
if __name__ == '__main__':
    JsonConverterApp().run()