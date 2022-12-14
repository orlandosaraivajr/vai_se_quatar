#!/usr/bin/env python3

from code.album import Album, RepeatedStickers, CSVSticker

if __name__ == "__main__":
    album = Album()
    album.add_figure('GER9')
    album.add_figure('CMR19')
    album.add_figure('BRA10')
    album.add_figure('BRA4')
    repetidas = RepeatedStickers()
    repetidas.add_figure('BRA1')
    repetidas.add_figure('BRA1')
    repetidas.add_figure('BRA1')
    repetidas.add_figure('BRA1')
    CSVSticker.write('figurinhas.csv', album.figurinhas_coladas)
    CSVSticker.write('repetidas.csv', repetidas.repetidas)

    album2 = Album()
    repetidas2 = RepeatedStickers()

    for figurinha in CSVSticker.reader('figurinhas.csv'):
        if album2.check_is_present(figurinha):
            repetidas2.add_figure(figurinha)
        else:
            album2.add_figure(figurinha)

    for figurinha in CSVSticker.reader('repetidas.csv'):
        if album2.check_is_present(figurinha):
            repetidas2.add_figure(figurinha)
        else:
            album2.add_figure(figurinha)