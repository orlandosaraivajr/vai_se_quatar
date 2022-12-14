from abc import ABC
import csv


class StickerException(Exception):
    pass


class AbstractSticker(ABC):
    def __init__(self):
        self._paises = self._create_countries()
        self._figurinhas = self._create_figure() 

    @property
    def figurinhas(self):
        return self._figurinhas
    
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
    
    def _valid_stiker(self, sticker):
        if sticker not in self.figurinhas:
            raise StickerException('Não existe essa figurinha')
        return True


class RepeatedStickers(AbstractSticker):
    def __init__(self):
        super().__init__()
        self._figurinhas_repetidas = []

    @property
    def repetidas(self):
        return self._figurinhas_repetidas

    def add_figure(self, sticker):
        self._valid_stiker(sticker)
        if sticker in self.figurinhas:
            self.repetidas.append(sticker)
            return True

    def remove(self, sticker):
        self._valid_stiker(sticker)
        if sticker in self.repetidas:
            self.repetidas.remove(sticker)
            return sticker
        return False


    def __str__(self):
        return "Estrutura de figurinhas repetidas"

    def __repr__(self):
        return str(self)

class Album(AbstractSticker):
    def __init__(self):
        super().__init__()
        self._figurinhas_coladas_no_album = []

    @property
    def figurinhas_coladas(self):
        return self._figurinhas_coladas_no_album
    
    @property
    def figurinhas_faltantes(self):
        return list(set(self.figurinhas) - set(self.figurinhas_coladas))
    
    def add_figure(self, figure):
        self._valid_stiker(figure)
        if not self.check_is_present(figure):
                self.figurinhas_coladas.append(figure)
                return True
        return False

    def check_is_present(self, figure):
        return figure in self.figurinhas_coladas

    def is_pasted(self, figure):
        return self.check_is_present(figure)

    def __str__(self):
        return "Album da copa do Quatar"

    def __repr__(self):
        return str(self)


class CSVSticker:
    @classmethod
    def write(self, filename='figurinhas.csv', stickers=[]):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(stickers)

    @classmethod
    def reader(self, filename='figurinhas.csv'):
        with open(filename) as csvfile:
            sreader = csv.reader(csvfile)
            lista = [] 
            for row in sreader:
                lista += row
            return lista