# 代码生成时间: 2025-10-18 13:24:03
import psutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.clock import Clock

"""
系统性能监控工具
使用Python和Kivy框架实现系统性能监控，包括CPU、内存和磁盘使用率
"""

class PerformanceMonitorApp(App):
    def build(self):
        # 创建主布局
        layout = BoxLayout(orientation='vertical')

        # 添加CPU使用率标签
        self.cpu_label = Label(text='CPU Usage: 0%')
        layout.add_widget(self.cpu_label)

        # 添加内存使用率标签
        self.mem_label = Label(text='Memory Usage: 0%')
        layout.add_widget(self.mem_label)

        # 添加磁盘使用率标签
        self.disk_label = Label(text='Disk Usage: 0%')
        layout.add_widget(self.disk_label)

        # 添加更新性能数据的定时器
        Clock.schedule_interval(self.update_performance_data, 1)

        return layout

    def update_performance_data(self, dt):
        try:
            # 获取CPU使用率
            cpu_usage = psutil.cpu_percent()
            self.cpu_label.text = f'CPU Usage: {cpu_usage}%'

            # 获取内存使用率
            mem_usage = psutil.virtual_memory().percent
            self.mem_label.text = f'Memory Usage: {mem_usage}%'

            # 获取磁盘使用率
            disk_usage = psutil.disk_usage('/').percent
            self.disk_label.text = f'Disk Usage: {disk_usage}%'

        except Exception as e:
            # 错误处理
            print(f'Error updating performance data: {e}')
            self.cpu_label.text = 'Error updating CPU data'
            self.mem_label.text = 'Error updating memory data'
            self.disk_label.text = 'Error updating disk data'

if __name__ == '__main__':
    PerformanceMonitorApp().run()
