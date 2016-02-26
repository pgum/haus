class Amiibro:
    def __init__(self):
        self.amiibos={
                #"hex": {'name': name, 'method': method, 'params': params
                }

    def handleTag(self, hex=None):
        if hex in self.amiibos:
            print(self.amiibos[hex]['name'])
            if self.amiibos[hex]['params']:
                self.amiibos[hex]['method'](self.amiibos[hex]['params'])
            else:
                self.amiibos[hex]['method']()
            return dict(msg= self.amiibos[hex]['name'])

