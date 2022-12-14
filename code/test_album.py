# -*- coding: utf-8 -*-
from album import Album, RepeatedStickers, StickerException
import pytest


class TestAlbum:
    def test_instance_declared(self):
        objeto = Album()
        assert isinstance(objeto, Album)

    def test_default_attributes(self):
        objeto = Album()
        assert isinstance(objeto._figurinhas, list)
        assert len(objeto._figurinhas) == 678
        assert isinstance(objeto._paises, list)
        assert len(objeto._paises) == 32
        assert objeto._paises[0] == 'QAT'
        assert len(objeto.figurinhas_coladas) == 0

    def test_method__create_countries(self):
        objeto = Album()
        lista_de_paises = objeto._create_countries()
        assert isinstance(lista_de_paises, list)
        assert len(lista_de_paises) == 32
        assert lista_de_paises[0] == 'QAT'
        assert 'BRA' in lista_de_paises
        assert 'XXX' not in lista_de_paises

    def test_method__create_figure(self):
        objeto = Album()
        lista_de_paises = objeto._create_figure()
        assert isinstance(lista_de_paises, list)
        assert len(lista_de_paises) == 678
        assert lista_de_paises[0] == '00'
        assert lista_de_paises[-1] == 'C8'
        assert 'BRA1' in lista_de_paises
        assert 'BRA20' in lista_de_paises
        assert 'BRA21' not in lista_de_paises

    def test_method_add_figure_ok(self):
        objeto = Album()
        assert len(objeto.figurinhas_coladas) == 0
        assert objeto.figurinhas_coladas == []
        assert objeto.add_figure('BRA1')
        assert len(objeto.figurinhas_coladas) == 1
        assert objeto.figurinhas_coladas == ['BRA1']

    def test_method_add_figure_fail_1(self):
        msg_erro = "Não existe essa figurinha"
        objeto = Album()
        assert len(objeto.figurinhas_coladas) == 0
        assert objeto.figurinhas_coladas == []
        with pytest.raises(StickerException) as error:
            objeto.add_figure('BRA40')
        assert str(error.value) == msg_erro
        
    def test_method_add_figure_fail_2(self):
        objeto = Album()
        assert len(objeto.figurinhas_coladas) == 0
        assert objeto.figurinhas_coladas == []
        assert objeto.add_figure('BRA1')
        assert not objeto.add_figure('BRA1')
        assert len(objeto.figurinhas_coladas) == 1
        assert objeto.figurinhas_coladas == ['BRA1']

    def test_method_check_is_present_1(self):
        objeto = Album()
        assert len(objeto.figurinhas_coladas) == 0
        objeto.add_figure('BRA1')
        assert objeto.check_is_present('BRA1')        

    def test_method_check_is_present_fail(self):
        objeto = Album()
        assert len(objeto.figurinhas_coladas) == 0
        assert not objeto.check_is_present('BRA1')  

    def test_method_is_pasted_1(self):
        objeto = Album()
        objeto.add_figure('BRA1')
        objeto.add_figure('BRA2')
        assert objeto.is_pasted('BRA1')
        assert objeto.is_pasted('BRA2')
        assert not objeto.is_pasted('BRA3')

    def test_report_pasted(self):
        objeto = Album()
        objeto.add_figure('BRA1')
        objeto.add_figure('BRA2')
        assert objeto.figurinhas_coladas == ['BRA1','BRA2']
    
    def test_property_missing_pictures_1(self):
        objeto = Album()
        objeto.add_figure('BRA1')
        assert type(objeto.figurinhas_faltantes) == list
        assert 'BRA1' not in objeto.figurinhas_faltantes
        assert 'BRA2' in objeto.figurinhas_faltantes
        assert '00' in objeto.figurinhas_faltantes
    
    def test_property_missing_pictures_2(self):
        objeto = Album()
        objeto.add_figure('BRA2')
        assert type(objeto.figurinhas_faltantes) == list
        assert 'BRA1' in objeto.figurinhas_faltantes
        assert 'C1' in objeto.figurinhas_faltantes
        assert 'BRA2' not in objeto.figurinhas_faltantes
        assert '00' in objeto.figurinhas_faltantes

    def test_str_repr(self):
        objeto = Album()
        assert str(objeto) == "Album da copa do Quatar"
        assert repr(objeto) == "Album da copa do Quatar"

class TestRepeatedStickersAlbum:
    def test_instance_declared(self):
        objeto = RepeatedStickers()
        assert isinstance(objeto, RepeatedStickers)

    def test_repeatedstickers_structure(self):
        objeto = RepeatedStickers()
        assert type(objeto.repetidas) is list
        assert len(objeto.repetidas) == 0

    def test_default_attributes(self):
        objeto = RepeatedStickers()
        assert isinstance(objeto._figurinhas, list)
        assert len(objeto._figurinhas) == 678
        assert isinstance(objeto._paises, list)
        assert len(objeto._paises) == 32
        assert objeto._paises[0] == 'QAT'
        assert len(objeto.repetidas) == 0

    def test_method_add_figure_ok_1(self):
        objeto = RepeatedStickers()
        assert len(objeto.repetidas) == 0
        assert objeto.repetidas == []
        assert objeto.add_figure('BRA1')
        assert len(objeto.repetidas) == 1
        assert objeto.repetidas == ['BRA1']

    def test_method_add_figure_ok_2(self):
        objeto = RepeatedStickers()
        assert len(objeto.repetidas) == 0
        assert objeto.repetidas == []
        assert objeto.add_figure('BRA1')
        objeto.add_figure('BRA2')
        assert len(objeto.repetidas) == 2
        assert objeto.repetidas == ['BRA1','BRA2']

    def test_method_add_figure_fail_1(self):
        msg_erro = "Não existe essa figurinha"
        objeto = RepeatedStickers()
        assert len(objeto.repetidas) == 0
        assert objeto.repetidas == []
        assert objeto.add_figure('BRA1')
        with pytest.raises(StickerException) as error:
            objeto.add_figure('BRA40')
        assert str(error.value) == msg_erro

    def test_method_remove_ok_1(self):
        objeto = RepeatedStickers()
        objeto.add_figure('BRA1')
        objeto.add_figure('BRA2')
        assert len(objeto.repetidas) == 2
        assert objeto.repetidas == ['BRA1','BRA2']
        objeto.remove('BRA2')
        assert objeto.repetidas == ['BRA1']
        assert len(objeto.repetidas) == 1

    def test_method_remove_ok_2(self):
        objeto = RepeatedStickers()
        objeto.add_figure('BRA1')
        objeto.add_figure('BRA1')
        assert len(objeto.repetidas) == 2
        assert objeto.repetidas == ['BRA1','BRA1']
        objeto.remove('BRA2')
        assert objeto.repetidas == ['BRA1','BRA1']
        assert len(objeto.repetidas) == 2

    def test_method_remove_fail_1(self):
        msg_erro = "Não existe essa figurinha"
        objeto = RepeatedStickers()
        assert len(objeto.repetidas) == 0
        assert objeto.repetidas == []
        with pytest.raises(StickerException) as error:
            objeto.remove('BRA40')
        assert str(error.value) == msg_erro
    
    def test_str_repr(self):
        objeto = RepeatedStickers()
        assert str(objeto) == "Estrutura de figurinhas repetidas"
        assert repr(objeto) == "Estrutura de figurinhas repetidas"