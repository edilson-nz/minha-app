from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import random

PROBLEMAS = [
    ("P0300 - Falha no motor", "Uma vela esta fraca. O carro vai tremer e gastar mais."),
    ("P0171 - Mistura pobre", "Esta a entrar muito ar. Verifica a mangueira."),
    ("P0420 - Catalisador fraco", "O catalisador esta cansado. Nao e urgente."),
    ("C1234 - Sensor ABS", "Sensor de travao sujo. Travao ainda funciona."),
    ("P0562 - Bateria fraca", "Bateria com pouca carga. Vai custar a pegar de manha."),
    ("P0115 - Temperatura alta", "Motor a aquecer! Verifica a agua do radiador."),
    ("B0001 - Airbag", "Luz do airbag acesa. Precisa ver eletricista."),
    ("NENHUM PROBLEMA", "Parabens! O teu carro esta saudavel."),
]

class Tela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.add_widget(Label(text='CARDOCTOR DEMO', font_size=28, bold=True, size_hint_y=None, height=50))
        self.add_widget(Label(text='Escolhe o teu carro:', font_size=18))
        self.carro = Spinner(text='Toyota Corolla', values=('Toyota Corolla','Mazda Demio','Nissan Note','Hyundai i10','Suzuki Swift','Honda Fit'), font_size=18, size_hint_y=None, height=50)
        self.add_widget(self.carro)
        self.status = Label(text='Pronto para ligar...', font_size=18)
        self.add_widget(self.status)
        self.botao = Button(text='FAZER SCAN AGORA', font_size=22, background_color=(0, 0.7, 0.3, 1), size_hint_y=None, height=70)
        self.botao.bind(on_press=self.scan)
        self.add_widget(self.botao)
        self.resultado = Label(text='', font_size=17, halign='left', valign='top')
        self.resultado.bind(size=self.resultado.setter('text_size'))
        self.add_widget(self.resultado)

    def scan(self, *args):
        self.status.text = 'A ligar ao carro... Aguarde...'
        self.resultado.text = ''
        self.botao.disabled = True
        Clock.schedule_once(self.mostrar, 2.5)

    def mostrar(self, *args):
        self.botao.disabled = False
        prob = random.choice(PROBLEMAS)
        self.status.text = f'Carro: {self.carro.text} - Scan completo!'
        if 'NENHUM' in prob[0]:
            self.resultado.text = 'OK ' + prob[0] + '\n\n' + prob[1]
        else:
            self.resultado.text = 'PROBLEMA ENCONTRADO:\n\n' + prob[0] + '\n\n' + prob[1] + '\n\nCusto estimado: 500 - 2000 MT'

class CarDoctorApp(App):
    def build(self):
        return Tela()

if __name__ == '__main__':
    CarDoctorApp().run()
