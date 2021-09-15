from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

class MyApp(App):
    def build(self):
        return CodeInput(lexer= HtmlLexer())

        return Button(text = 'Это моя первая кнопка!',
                      font_size = 30,
                      on_press = self.btnpress,
                      background_color = [59, 0, 0, 1],
                      background_normal = '')

    def btnpress(self, instance):
        print('кнопка нажата')
        instance.text = 'Я нажата'


if __name__ == "__main__":
    MyApp().run()
