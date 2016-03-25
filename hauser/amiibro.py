class Amiibro:
    def __init__(self):
        self._amiibos={#'hex': {'name': 'Noname', 'method': methodObject, 'params': params}
                     }

    def handleTag(self, hex=None):
        if hex in self._amiibos:
            print(self._amiibos[hex]['name'])
            if self._amiibos[hex]['params']:
                self._amiibos[hex]['method'](self._amiibos[hex]['params'])
            else:
                self._amiibos[hex]['method']()
            return self._amiibos[hex]['name']

