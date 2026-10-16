import pytest
from src.descuentos import (
    aplicar_descuento, calcular_descuento, calcular_precio_final,
    descuento_por_volumen, descuento_cumulativo, descuento_apilado
)
#! aplicar_descuento & Calcularlo

def test_aplicar_descuento_normal():
    
    precio, porcentaje = 100, 20
    
    resultado = aplicar_descuento(precio, porcentaje)
    
    assert resultado == pytest.approx(80)

def test_aplicar_descuento_cien_porcentaje_da_cero():
    
    precio, porcentaje = 100, 100
    
    resultado = aplicar_descuento(precio, porcentaje)
    
    assert resultado == 0

def test_calcular_descuento_normal():
    
    precio, porcentaje = 200, 25
    
    resultado = calcular_descuento(precio, porcentaje)
    
    assert resultado == pytest.approx(50)


#! Calcular precio final

def test_precio_final_solo_con_impuesto():
    
    precio, impuesto, descuento = 100, 19, 0
    
    resultado = calcular_precio_final(precio, impuesto, descuento)
    
    assert resultado == pytest.approx(119)

def test_precio_final_con_descuento_e_impuesto():
    # Arrange: el impuesto debe calcularse sobre el precio ya descontado (80)
    precio, impuesto, descuento = 100, 10, 20
    
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert: 80 + 10% de 80 = 88
    assert resultado == pytest.approx(88)

def test_precio_final_con_descuento_total_no_cobra_impuesto():
    # Arrange: con 100% de descuento no queda base sobre la cual cobrar impuesto
    precio, impuesto, descuento = 100, 10, 100
    
    resultado = calcular_precio_final(precio, impuesto, descuento)
    
    assert resultado == 0


#! Descuento por volumen

@pytest.mark.parametrize("cantidad, esperado", [
    (9, 90),     # justo debajo del primer tramo: sin descuento
    (10, 95),    # límite inferior del tramo 5%
    (20, 180),   # límite inferior del tramo 10%
    (50, 425),   # límite inferior del tramo 15%
    (100, 800),  # límite inferior del tramo 20%
])
def test_descuento_por_volumen_en_el_limite_de_cada_tramo(cantidad, esperado):
    
    precio_unitario = 10
    
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    
    assert resultado == pytest.approx(esperado)


#! Descuento cumulativo

def test_descuento_cumulativo_aplica_los_descuentos_en_cadena():
    
    precio, descuentos = 100, [10, 10]
    
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert: 100 -> 90 -> 81
    assert resultado == pytest.approx(81)

def test_descuento_cumulativo_lista_vacia_devuelve_precio_original():
    
    precio, descuentos = 100, []
    
    resultado = descuento_cumulativo(precio, descuentos)
    
    assert resultado == 100


#! Descuento apilado

def test_descuento_apilado_suma_los_porcentajes():
    
    precio, descuentos = 100, [10, 10]
    
    resultado = descuento_apilado(precio, descuentos)
    # Assert: 20% de descuento total
    assert resultado == pytest.approx(80)

def test_descuento_apilado_que_excede_cien_se_limita_a_cien():
    # Arrange: 60 + 50 = 110%, el precio no puede quedar negativo ni dar error
    precio, descuentos = 100, [60, 50]
    
    resultado = descuento_apilado(precio, descuentos)
    
    assert resultado == 0


#! Entradas inválidas

@pytest.mark.parametrize("funcion, args", [
    (aplicar_descuento, (-1, 10)),            # precio negativo
    (aplicar_descuento, (100, 101)),          # porcentaje > 100
    (calcular_descuento, (-200, 25)),         # precio negativo
    (calcular_descuento, (200, 150)),         # porcentaje > 100
    (calcular_precio_final, (-100, 10, 10)),  # precio negativo
    (calcular_precio_final, (100, -10, 10)),  # impuesto negativo
    (calcular_precio_final, (100, 10, 101)),  # descuento > 100
    (descuento_por_volumen, (-1, 10)),        # cantidad negativa
    (descuento_por_volumen, (10, -10)),       # precio unitario negativo
    (descuento_cumulativo, (-100, [10])),     # precio negativo
    (descuento_cumulativo, (100, [10, 150])), # un descuento inválido en la lista
    (descuento_apilado, (-100, [10])),        # precio negativo
])
def test_entradas_invalidas_lanzan_value_error(funcion, args):
    # Arrange: la función y sus argumentos vienen de parametrize
    # Act / Assert
    with pytest.raises(ValueError):
        funcion(*args)