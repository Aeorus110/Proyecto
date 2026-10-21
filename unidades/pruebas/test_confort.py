from modulos.confort import (describir_confort, clasificar_temperatura, es_humedad_adecuada)

def test_sensor_inactivo():
    assert describir_confort(19.5, 50, False) == "revisar sensor"

def test_limite_temperatura_18():
    assert clasificar_temperatura(18) == "adecuada"

def test_limite_temperatura_27():
    assert clasificar_temperatura(27) == "adecuada"

def test_limite_humedad_30():
    assert es_humedad_adecuada(30) is True

def test_limite_humedad_65():
    assert es_humedad_adecuada(65) is True

def test_humedad_fuera_de_rango():
    assert es_humedad_adecuada(99) is False