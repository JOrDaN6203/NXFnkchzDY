# 代码生成时间: 2025-10-27 09:04:12
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from cryptography.fernet import Fernet

class PasswordEncryptionDecryptionApp(App):
    # 文档字符串，解释类的作用
    """
    This application provides a simple GUI for password encryption and decryption
    using the Fernet symmetric encryption algorithm from the cryptography library.
    """
    def build(self):
        # 创建主布局
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Enter password to encrypt or decrypt:'))
        self.password_input = TextInput(multiline=False)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(Button(text='Encrypt', on_press=self.encrypt))
        self.layout.add_widget(Button(text='Decrypt', on_press=self.decrypt))
        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)
        return self.layout
    
def generate_key():
    # 函数生成密钥并保存到文件，以便以后使用
    return Fernet.generate_key()

def load_key():
    # 函数从文件加载密钥，如果文件不存在，则生成新密钥并保存
    try:
        with open('key.key', 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        return generate_key()

def save_key(key):
    # 函数保存密钥到文件
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def encrypt(self, instance):
    # 加密密码
    try:
        key = load_key()
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(self.password_input.text.encode())
        self.result_label.text = f'Encrypted: {encrypted_password.decode()}'
    except Exception as e:
        self.show_error_popup(f'Encryption error: {e}')

def decrypt(self, instance):
    # 解密密码
    try:
        key = load_key()
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(self.password_input.text.encode())
        self.result_label.text = f'Decrypted: {decrypted_password.decode()}'
    except Exception as e:
        self.show_error_popup(f'Decryption error: {e}')

def show_error_popup(self, error_message):
    # 显示错误信息的弹出窗口
    popup = Popup(title='Error', content=Label(text=error_message), size_hint=(None, None), size=(200, 200))
    popup.open()

if __name__ == '__main__':
    # 程序入口点
    PasswordEncryptionDecryptionApp().run()