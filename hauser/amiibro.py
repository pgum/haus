class Amiibro:
    def __init__(self):
        self.amiibos={
                #'hex': {'name': 'Noname', 'method': methodObject, 'params': params }
                }

    def handleTag(self, hex=None):
        if hex in self.amiibos:
            print(self.amiibos[hex]['name'])
            if self.amiibos[hex]['params']:
                self.amiibos[hex]['method'](self.amiibos[hex]['params'])
            else:
                self.amiibos[hex]['method']()
            return self.amiibos[hex]['name']

