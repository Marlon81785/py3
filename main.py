import kivy
import self as self
from kivy.app import App
from kivy.app import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



class PaginaInicial(Screen):
    pass


class LabelConfig(Screen):
    pass


class Ferritina(Screen):
    pass

class Ist(Screen):
    pass

class Resultado(Screen):
    pass



class ScreenManagement(ScreenManager):

    def switch_to_ferritina(self):
        if(self.get_screen('labelConfig').ids.teste.text != ''):
            self.current = 'ferritina'
        else:
            self.current = 'labelConfig'

    def switch_to_labelConfig(self):
        self.get_screen('resultado').ids.txt1.text = 'Renovacao'
        self.current = 'labelConfig'

    def switch_to_labelConfig2(self):
        self.get_screen('resultado').ids.txt1.text = 'Inicial'
        self.current = 'labelConfig'

    def switch_to_paginaInicial(self):
        self.get_screen('resultado').ids.txt1.text = ''
        self.get_screen('labelConfig').ids.teste.text = ''
        self.get_screen('ferritina').ids.ferro.text = ''
        self.get_screen('ist').ids.ist_id.text = ''

        self.current = 'paginaInicial'

    def switch_to_Ist(self):
        if(self.get_screen('ferritina').ids.ferro.text != ''):
            self.current = 'ist'
        else:
            self.current = 'ferritina'


    def switch_to_resultado(self):
        if (self.get_screen('ist').ids.ist_id.text != ''):
            self.current = 'resultado'
        else:
            self.current = 'ist'
        estado = self.get_screen('resultado').ids.txt1.text
        hb = float(self.get_screen('labelConfig').ids.teste.text)
        ferritina = float(self.get_screen('ferritina').ids.ferro.text)
        indicedesaturacao = float(self.get_screen('ist').ids.ist_id.text)
        #
        #condiconais#
        #
        if(estado == 'Inicial'):#condita inicial|sao 2 casos epo sozinho e nori sozinho
            if(hb < 10 and ferritina > 200 and indicedesaturacao > 20):
                self.get_screen('resultado').ids.txt2.text = 'Alfaepoetina dose ataque'
                self.get_screen('resultado').ids.txt3.text = 'Aplicar 3x por semana'
                self.get_screen('resultado').ids.txt4.text = '12 ampolas no primeiro, segundo e terceiro mes'
            else:
                if(hb < 10 and ferritina < 200 or hb < 10 and indicedesaturacao < 20):
                    self.get_screen('resultado').ids.txt2.text = 'Tomar somente o Saxarato de hidroxido ferrico dose ataque'
                    self.get_screen('resultado').ids.txt3.text = 'Aplicar 1 ampola ev a cada 15 dias durante 30 dias no primeiro mes'
                    self.get_screen('resultado').ids.txt4.text = 'Dose ataque 10 ampolas no primeiro mes, 2 no segundo e terceiro'

        else:#conduta renovacao
            if(hb < 13 and ferritina > 200 < 500 and indicedesaturacao > 20 < 30):
                self.get_screen('resultado').ids.txt2.text = 'Manter Alfaepoetina dose ataque'
                self.get_screen('resultado').ids.txt3.text = 'Aplicar 3x por semana'
                self.get_screen('resultado').ids.txt3.text = 'Caso o individuo estiver em uso de \nSacarato de hidroxido ferrico ele \ndeve manter com a dose manutencao'
            else:
                if(hb < 13 and ferritina < 200 or hb < 13 and indicedesaturacao < 20):
                    self.get_screen('resultado').ids.txt2.text = 'Tomar somente o Saxarato de hidroxido ferrico dose ataque'
                    self.get_screen('resultado').ids.txt3.text = 'Aplicar 1 ampola ev a cada 15 dias durante 30 dias no primeiro mes'
                    self.get_screen('resultado').ids.txt4.text = 'Dose ataque 10 ampolas no primeiro mes, 2 no segundo e terceiro'
                else:
                    self.get_screen('resultado').ids.txt2.text = 'C nao tem anemia não sinho'
                    self.get_screen('resultado').ids.txt3.text = 'nao consegue montar processo de Alfaepoetina'
                    self.get_screen('resultado').ids.txt4.text = 'ou Sacarato de hidroxido ferrico'





    def switch_to_exit(self):
        exit()




#mesmo nome do arquivo kv! main.kv main.py
class main(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root


if __name__ == '__main__':
    main().run()