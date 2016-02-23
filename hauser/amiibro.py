import koditalker

class Amiibro:
    def __init__(self):
        self.kodiTalker = koditalker.KodiTalker()
        self.amiibos={
                "04625FAA554980": {'name': "Mewtwo" , 'method': self.kodiTalker.PlayPause , 'param': None},
                "0457ABE29A3D80": {'name': "Pikachu", 'method': self.kodiTalker.VolumeUp  , 'param': 10},
                "040C9A0AFE3D81": {'name': "Kirby"  , 'method': self.kodiTalker.VolumeDown, 'param': 10}}

    def handleTag(self, hex=None):
        if hex in self.amiibos:
            print(self.amiibos[hex]['name'])
            if self.amiibos[hex]['param']:
                self.amiibos[hex]['method'](self.amiibos[hex]['param'])
            else:
                self.amiibos[hex]['method']()
            return dict(msg= self.amiibos[hex]['name'])

