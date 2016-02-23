import koditalker

class Amiibro:
    def __init__(self):
        self.kodiTalker = KodiTalker()
        self.amiibos={
                "04625FAA554980": {'name': "Mewtwo", 'method':  self.kodiTalker.PlayPause()},
                "0457ABE29A3D80": {'name': "Pikachu", 'method':  self.kodiTalker.VolumeUp(10)},
                "040C9A0AFE3D81": {'name': "Kirby", 'method':  self.kodiTalker.VolumeDown(10)}}

    def broforce(self, hex=None):
        if hex in self.amiibos:
            self.amiibos[hex]['method']()
            return dict(msg= self.amiibos[hex]['name'])

