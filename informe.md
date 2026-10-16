# Informe — Análisis y Mejora de Pruebas Unitarias

## 1. Datos

- **Nombre:** Alejandro Rojas Casas

---

## 2. Módulo `calculadora.py`

### 2.1 Qué hace
Agrupa operaciones matemáticas básicas (`sumar`, `restar`, `multiplicar`, `dividir`, `potencia`, `raiz_cuadrada`), estadísticas sobre listas (`promedio`, `maximo`, `minimo`) y cálculos geométricos de un rectángulo (`calcular_area_rectangulo`, `calcular_perimetro_rectangulo`).

### 2.2 Casos probados y por qué
Escribí 32 pruebas con estructura AAA. Para cada función combiné un caso normal con los casos límite donde el código podía fallar.

| Función | Casos probados | Por qué |
|---|---|---|
| `sumar` | positivos, negativos, suma con cero | el cero es el elemento neutro y los negativos prueban el signo |
| `restar` | resultado negativo | verifica que no asuma resultados positivos |
| `multiplicar` | por cero, dos negativos | el cero anula el resultado y negativo por negativo da positivo |
| `dividir` | decimal, negativos, división por cero | la división por cero debe lanzar `ValueError` |
| `potencia` | exponente positivo, 0 y negativo | el exponente 0 da 1 y el negativo produce una fracción |
| `raiz_cuadrada` | cuadrado perfecto, cero, no exacto, negativo | el negativo no tiene raíz real; el no exacto exige `pytest.approx` |
| `promedio` | lista simple, un elemento, lista vacía | la lista vacía provocaría división por cero |
| `maximo` | positivos, todos negativos, lista vacía | los negativos revelan si el valor inicial está mal elegido |
| `minimo` | todos positivos, con negativos, un elemento, lista vacía | es el caso que reveló el bug 2 |
| `calcular_area_rectangulo` | normal, base cero, lado negativo | el cero es el límite válido y el negativo debe lanzar error |
| `calcular_perimetro_rectangulo` | normal, un lado cero, lado negativo | igual que el área |

### 2.3 Bugs encontrados

| # | Función | Entrada que lo revela | Resultado erróneo | Resultado esperado | Corrección |
|---|---|---|---|---|---|
| 1 | `raiz_cuadrada` | `-4` | Devuelve un número complejo (`1.2e-16+2j`) sin lanzar error | `ValueError` | Se agregó `if numero < 0: raise ValueError(...)` |
| 2 | `minimo` | `[5, 3, 8]` y `[10]` | Devuelve `0` | `3` y `10` | `min_val` arrancaba en `0`; ahora arranca en `lista[0]` |

**Bug 1:** en Python 3, elevar un negativo a `0.5` no lanza error, devuelve un complejo. Es un bug silencioso: el programa sigue con un valor que el resto del código no espera. Elegí `ValueError` por coherencia con `dividir` y `promedio`.

**Bug 2:** `min_val` se iniciaba en `0`. Si todos los números son positivos, ninguno es menor que `0` y la función devuelve `0`, que ni siquiera está en la lista. Con `[4, -7, 2]` sí funcionaba, porque aparece un valor menor que `0`.

### 2.4 Evidencia

![calculadora en rojo](img/calculadora_roja.png)

Pruebas en verde (después de corregir):

![calculadora en verde](img/calculadora_verde.png)

---

## 3. Módulo `descuentos.py`

### 3.1 Qué hace
(...)

### 3.2 Casos probados y por qué

| Función | Casos probados | Por qué |
|---|---|---|
| (...) | (...) | (...) |

### 3.3 Bugs encontrados

| # | Función | Entrada que lo revela | Resultado erróneo | Resultado esperado | Corrección |
|---|---|---|---|---|---|
| 3 | (...) | (...) | (...) | (...) | (...) |
| 4 | (...) | (...) | (...) | (...) | (...) |

**Bug 3:** (...)

**Bug 4:** (...)

### 3.4 Evidencia

![descuentos en rojo](capturas/descuentos_rojo.png)

![descuentos en verde](capturas/descuentos_verde.png)

**Commits relacionados:** (...)

---

## 4. Módulo `(tercer_modulo).py`

### 4.1 Qué hace
(...)

### 4.2 Casos probados y por qué

| Función | Casos probados | Por qué |
|---|---|---|
| (...) | (...) | (...) |

### 4.3 Bugs encontrados

| # | Función | Entrada que lo revela | Resultado erróneo | Resultado esperado | Corrección |
|---|---|---|---|---|---|
| 5 | (...) | (...) | (...) | (...) | (...) |

**Bug 5:** (...)

### 4.4 Evidencia

![tercer módulo en rojo](capturas/modulo3_rojo.png)

![tercer módulo en verde](capturas/modulo3_verde.png)

**Commits relacionados:** (...)

---

## 5. Resumen de bugs

| # | Módulo | Función | Entrada | Erróneo vs esperado | Corrección |
|---|---|---|---|---|---|
| 1 | calculadora | `raiz_cuadrada` | `-4` | complejo vs `ValueError` | validar negativos |
| 2 | calculadora | `minimo` | `[5, 3, 8]` | `0` vs `3` | iniciar en `lista[0]` |
| 3 | descuentos | (...) | (...) | (...) | (...) |
| 4 | descuentos | (...) | (...) | (...) | (...) |
| 5 | (módulo 3) | (...) | (...) | (...) | (...) |

---

## 6. Cobertura

Comando:

```
pytest tests/ -v --cov=src --cov-report=term-missing
```

Salida:

```
(pega aquí la tabla completa)
```

![cobertura](capturas/cobertura.png)

**Lectura de los resultados:** (qué módulos superaron el 85 %, cuáles quedaron más bajos y por qué, qué aparece en la columna `Miss`)

---

## 7. Reflexión final

**¿Qué NO mide la cobertura?**
(...)

**¿Qué aprendí?**
(...)