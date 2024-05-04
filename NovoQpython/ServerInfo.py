#ServerInfo.py
class Info:
    def __init__(self, attribute):
        self.attribute = attribute

    def get(self):
        # Lógica para obter o valor do atributo
        if self.attribute == 'uid':
            return '0x00000000'
        elif self.attribute == 'heap':
            return '0x8000-0x1000000'
        elif self.attribute == 'name':
            return 'simpleserver'
        elif self.attribute == 'about':
            return 'linux version'
        elif self.attribute == 'ver':
            return '1.0.0b'
        elif self.attribute == 'date':
            return '07-09-2014'
        elif self.attribute == 'by':
            return 'inunxlabs'
        elif self.attribute == 'mail':
            return 'inunxlabs@gmail.com'
        elif self.attribute == 'remode':
            return 'Sane4tsu'
        else:
            return 'Unknown attribute'

    def get_info(self):
        return self.get()
