import pytest
from src.conversor import (
    celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin, kelvin_a_celsius,
    metros_a_kilometros, kilometros_a_metros,
    libras_a_kilogramos, kilogramos_a_libras,
    galones_a_litros, litros_a_galones,
    millas_a_kilometros, kilometros_a_millas,
    pies_a_metros, metros_a_pies,
    onzas_a_gramos, gramos_a_onzas
)


#! Valores conocidos

@pytest.mark.parametrize("funcion, entrada, esperado", [
    (celsius_a_fahrenheit, 100, 212),        #? punto de ebullición del agua
    (celsius_a_fahrenheit, 0, 32),           #? punto de congelación
    (celsius_a_fahrenheit, -40, -40),        #? donde ambas escalas coinciden
    (fahrenheit_a_celsius, 212, 100),
    (fahrenheit_a_celsius, -40, -40),
    (celsius_a_kelvin, 0, 273.15),
    (kelvin_a_celsius, 273.15, 0),
    (metros_a_kilometros, 1500, 1.5),
    (kilometros_a_metros, 2.5, 2500),
    (libras_a_kilogramos, 10, 4.53592),
    (kilogramos_a_libras, 1, 2.20462),
    (galones_a_litros, 1, 3.78541),
    (litros_a_galones, 3.78541, 1),
    (millas_a_kilometros, 10, 16.0934),
    (pies_a_metros, 10, 3.048),
    (metros_a_pies, 0.3048, 1),
    (onzas_a_gramos, 1, 28.3495),
    (gramos_a_onzas, 28.3495, 1),
])
def test_conversion_con_valor_conocido(funcion, entrada, esperado):
    # Arrange: funcion, entrada y esperado vienen de parametrize
    # Act
    resultado = funcion(entrada)
    # Assert
    assert resultado == pytest.approx(esperado, rel=1e-4)

@pytest.mark.parametrize("funcion", [
    metros_a_kilometros, kilometros_a_metros,
    libras_a_kilogramos, kilogramos_a_libras,
    galones_a_litros, litros_a_galones,
    millas_a_kilometros, kilometros_a_millas,
    pies_a_metros, metros_a_pies,
    onzas_a_gramos, gramos_a_onzas,
])
def test_conversion_de_cero_da_cero(funcion):
    # Arrange: la función viene de parametrize
    entrada = 0
    # Act
    resultado = funcion(entrada)
    # Assert
    assert resultado == 0


#! Datos de ida y vuelta

@pytest.mark.parametrize("ida, vuelta, valor", [
    (millas_a_kilometros, kilometros_a_millas, 26.2),
    (metros_a_kilometros, kilometros_a_metros, 1234),
    (libras_a_kilogramos, kilogramos_a_libras, 150),
    (galones_a_litros, litros_a_galones, 12),
    (pies_a_metros, metros_a_pies, 100),
    (onzas_a_gramos, gramos_a_onzas, 8),
    (celsius_a_fahrenheit, fahrenheit_a_celsius, 37),
    (celsius_a_kelvin, kelvin_a_celsius, 25),
])
def test_convertir_ida_y_vuelta_devuelve_el_valor_original(ida, vuelta, valor):
    # Arrange: las dos funciones y el valor vienen de parametrize
    # Act
    resultado = vuelta(ida(valor))
    # Assert
    assert resultado == pytest.approx(valor)


#! KM a Millas

def test_kilometros_a_millas_cien_km_son_unas_62_millas():
    # Arrange
    kilometros = 100
    # Act
    resultado = kilometros_a_millas(kilometros)
    # Assert: 100 / 1.60934 = 62.137...
    assert resultado == pytest.approx(62.1371, rel=1e-4)


#! K° a C°

def test_kelvin_cero_es_el_cero_absoluto():
    # Arrange
    kelvin = 0
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(-273.15)

def test_kelvin_negativo_lanza_error():
    # Arrange: por debajo del cero absoluto no existe temperatura
    kelvin = -1
    # Act / Assert
    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)


#! Entradas negativas

@pytest.mark.parametrize("funcion", [
    metros_a_kilometros, kilometros_a_metros,
    libras_a_kilogramos, kilogramos_a_libras,
    galones_a_litros, litros_a_galones,
    millas_a_kilometros, kilometros_a_millas,
    pies_a_metros, metros_a_pies,
    onzas_a_gramos, gramos_a_onzas,
])
def test_valor_negativo_lanza_value_error(funcion):
    # Arrange: la función viene de parametrize
    entrada = -1
    # Act / Assert
    with pytest.raises(ValueError):
        funcion(entrada)