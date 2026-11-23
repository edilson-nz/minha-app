from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(text='Ola Edilson!', font_size=32))
        layout.add_widget(Label(text='Minha primeira app!', font_size=20))
        btn = Button(text='Clica aqui', size_hint=(1, 0.3))
        btn.bind(on_press=self.clicou)
        layout.add_widget(btn)
        self.label = Label(text='', font_size=20)
        layout.add_widget(self.label)
        return layout

    def clicou(self, instance):
        self.label.text = 'Funcionou! Parabens!'

if __name__ == '__main__':
    MeuApp().run()
