import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada,
    promedio, maximo, minimo,
    calcular_area_rectangulo, calcular_perimetro_rectangulo
)
#!sumas, restas y multiplicaciones

def test_sumar_positivos():
    a, b = 7, 3
    resultado = sumar(a, b)
    assert resultado == 10

def test_sumar_negativos():
    
    a, b = -3, -4
    
    resultado = sumar(a, b)
    
    assert resultado == -7

def test_sumar_con_cero():
    
    a, b = 9, 0
    
    resultado = sumar(a, b)
    
    assert resultado == 9

def test_restar_da_resultado_negativo():
    
    a, b = 3, 10
    
    resultado = restar(a, b)
    
    assert resultado == -7

def test_multiplicar_por_cero_da_cero():
    
    a, b = 8, 0
    
    resultado = multiplicar(a, b)
    
    assert resultado == 0

def test_multiplicar_negativos_da_positivo():
    
    a, b = -3, -10
    
    resultado = multiplicar(a, b)
    
    assert resultado == 30

#!Dividir

def test_dividir_con_resultado_decimal():
    
    a, b = 1, 4
    
    resultado = dividir(a, b)
    
    assert resultado == 0.25

def test_dividir_negativos():
    
    a, b = -10, 2
    
    resultado = dividir(a, b)
    
    assert resultado == -5

def test_dividir_por_cero_lanza_error():
    
    a, b = 10, 0
    with pytest.raises(ValueError):
        dividir(a, b)

#! Potencia

def test_potencia_exponente_positivo():
    
    base, exponente = 2, 3
    
    resultado = potencia(base, exponente)
    
    assert resultado == 8

def test_potencia_exponente_cero_da_uno():
    
    base, exponente = 5, 0
    
    resultado = potencia(base, exponente)
    
    assert resultado == 1

def test_potencia_exponente_negativo_da_fraccion():
    
    base, exponente = 2, -1
    
    resultado = potencia(base, exponente)
    
    assert resultado == 0.5

#!Raiz Cuadrada

def test_raiz_cuadrada_de_numero_perfecto():
    
    numero = 16
    
    resultado = raiz_cuadrada(numero)
    
    assert resultado == 4

def test_raiz_cuadrada_de_cero():
    
    numero = 0
    
    resultado = raiz_cuadrada(numero)
    
    assert resultado == 0

def test_raiz_cuadrada_de_numero_no_exacto():
    
    numero = 2
    
    resultado = raiz_cuadrada(numero)
    
    assert resultado == pytest.approx(1.41421356)

def test_raiz_cuadrada_de_negativo_lanza_error():
    
    numero = -4
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


# ---------- promedio ----------

def test_promedio_lista_simple():
    
    lista = [2, 4, 6]
    
    resultado = promedio(lista)
    
    assert resultado == 4

def test_promedio_de_un_solo_elemento():
    
    lista = [7]
    
    resultado = promedio(lista)
    
    assert resultado == 7

def test_promedio_lista_vacia_lanza_error():
    
    lista = []
    with pytest.raises(ValueError):
        promedio(lista)

#! Maximo

def test_maximo_con_positivos():
    
    lista = [3, 9, 4]
    
    resultado = maximo(lista)
    
    assert resultado == 9

def test_maximo_con_todos_negativos():
    
    lista = [-5, -2, -9]
    
    resultado = maximo(lista)
    
    assert resultado == -2

def test_maximo_lista_vacia_lanza_error():
    
    lista = []
    with pytest.raises(ValueError):
        maximo(lista)


#! Minimo

def test_minimo_con_todos_positivos():
    
    lista = [5, 3, 8]
    
    resultado = minimo(lista)
    
    assert resultado == 3

def test_minimo_con_negativos():
    
    lista = [4, -7, 2]
    
    resultado = minimo(lista)
    
    assert resultado == -7

def test_minimo_de_un_solo_elemento_positivo():
    
    lista = [10]
    
    resultado = minimo(lista)
    
    assert resultado == 10

def test_minimo_lista_vacia_lanza_error():
    
    lista = []
    with pytest.raises(ValueError):
        minimo(lista)


#! A&P de un rectangulo

def test_area_rectangulo_normal():
    
    base, altura = 4, 5
    
    resultado = calcular_area_rectangulo(base, altura)
    
    assert resultado == 20

def test_area_rectangulo_con_base_cero_da_cero():
    
    base, altura = 0, 5
    
    resultado = calcular_area_rectangulo(base, altura)
    
    assert resultado == 0

def test_area_rectangulo_con_negativo_lanza_error():
    
    base, altura = -4, 5
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)

def test_perimetro_rectangulo_normal():
    
    base, altura = 4, 5
    
    resultado = calcular_perimetro_rectangulo(base, altura)
    
    assert resultado == 18

def test_perimetro_rectangulo_con_un_lado_cero():
    
    base, altura = 0, 5
    
    resultado = calcular_perimetro_rectangulo(base, altura)
    
    assert resultado == 10

def test_perimetro_rectangulo_con_negativo_lanza_error():
    
    base, altura = 4, -5
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)