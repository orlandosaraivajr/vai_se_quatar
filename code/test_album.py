# -*- coding: utf-8 -*-
from album import Album
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
        objeto = Album()
        assert len(objeto.figurinhas_coladas) == 0
        assert objeto.figurinhas_coladas == []
        assert not objeto.add_figure('BRA40')
        assert len(objeto.figurinhas_coladas) == 0
        assert objeto.figurinhas_coladas == []

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

    def test_method_check_is_present_2(self):
        objeto = Album()
        assert len(objeto.figurinhas_coladas) == 0
        assert not objeto.check_is_present('BRA1')  