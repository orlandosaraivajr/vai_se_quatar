
class RepeatedStickers:
    def __init__(self):
        self._figurinhas_repetidas = []

    @property
    def repetidas(self):
        return self._figurinhas_repetidas


class Album:
    def __init__(self):
        self._paises = self._create_countries()
        self._figurinhas = self._create_figure()
        self._figurinhas_coladas_no_album = []

    @property
    def figurinhas(self):
        return self._figurinhas
    
    @property
    def figurinhas_coladas(self):
        return self._figurinhas_coladas_no_album
    
    @property
    def figurinhas_faltantes(self):
        return list(set(self.figurinhas) - set(self.figurinhas_coladas))
    
    def _create_countries(self):
        _paises = ['qat', 'ecu', 'sen', 'ned']
        _paises += ['eng', 'irn', 'usa', 'wal']
        _paises += ['arg', 'ksa', 'mex', 'pol']
        _paises += ['fra', 'aus', 'den', 'tun']
        _paises += ['esp', 'crc', 'ger', 'jpn']
        _paises += ['bel', 'can', 'mar', 'cro']
        _paises += ['bra', 'srb', 'sui', 'cmr']
        _paises += ['por', 'gha', 'uru', 'kor']
        paises = []
        for pais in _paises:
            paises.append(pais.upper())
        return paises

    def _create_figure(self):
        paises = self._create_countries()
        figures = ['00']
        figures += ['FWC' + str(numero) for numero in range(1, 19)]
        figures += [pais + str(numero) for pais in paises for numero in range(1,21)]
        figures += ['FWC' + str(numero) for numero in range(19, 30)]
        figures += ['C' + str(numero) for numero in range(1, 9)]
        return figures

    def add_figure(self, figure):
        if figure in self.figurinhas and not self.check_is_present(figure):
                self.figurinhas_coladas.append(figure)
                return True
        return False

    def check_is_present(self, figure):
        return figure in self.figurinhas_coladas

    def is_pasted(self, figure):
        return self.check_is_present(figure)