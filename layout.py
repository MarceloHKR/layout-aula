from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#alterar a cor do background
from kivy.core.window import Window

Window.clearcolor = (28/255, 40/255, 51/255, 1)

class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        #Definindo o layout da aplicação
        self.cols = 1

        self.sub_layout = GridLayout()
        self.sub_layout.cols = 2

        #criando a label Nome
        self.nome_label = Label(text='Nome:')
        #adicionando a label Nome ao layout
        self.sub_layout.add_widget(self.nome_label)

        #criando o TextInput Nome
        self.nome_do_cliente = TextInput(multiline=False)
        #adicionando o TextInput Nome ao layout
        self.sub_layout.add_widget(self.nome_do_cliente)

        #--------------------------------------------------#

        #criando a label Mesa
        self.mesa_label = Label(text='Mesa:')
        #adicionando a label Mesa ao layout
        self.sub_layout.add_widget(self.mesa_label)

        #criando o TextInput Mesa
        self.mesa_do_cliente = TextInput(multiline=False)
        #adicionando o TextInput Mesa ao layout
        self.sub_layout.add_widget(self.mesa_do_cliente)

        #--------------------------------------------------#

        #criando a label Pedido
        self.pedido_label = Label(text='Pedido:')
        #adicionando a label Pedido ao layout
        self.sub_layout.add_widget(self.pedido_label)

        #criando o TextInput Pedido
        self.pedido_do_cliente = TextInput(multiline=True)
        #adicionando o TextInput Pedido ao layout
        self.sub_layout.add_widget(self.pedido_do_cliente)

        #--------------------------------------------------#

        #adicionando o sub_layout no layout principal
        self.add_widget(self.sub_layout)

        #criando o botão enviar
        self.enviar = Button(text='Enviar Pedido')
        #adicionando a função de callback ao botão
        self.enviar.bind(on_press=self.enviar_pedido)
        #adiciona o botão enviar ao layout
        self.add_widget(self.enviar)

    def enviar_pedido(self, instance):
        #criando o label de confirmação
        self.confirmacao =  Label(
            text=f'Cliente: {self.nome_do_cliente.text}\nMesa: {self.mesa_do_cliente.text}\nPedido: {self.pedido_do_cliente.text}'
        )
        #adicionando o label de confirmação ao layout
        self.add_widget(self.confirmacao)

        #lompando os campos de texto
        self.nome_do_cliente.text = ''
        self.mesa_do_cliente.text = ''
        self.pedido_do_cliente.text = ''


class LanchoneteApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    LanchoneteApp().run()