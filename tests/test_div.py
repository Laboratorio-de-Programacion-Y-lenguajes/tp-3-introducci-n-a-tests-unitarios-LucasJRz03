"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
@pytest.mark.parametrize("a, b, esperado", [
    (8, 5, 1.6), #   - División que da resultado decimal (float)
    (6, -3, -2), #   - División con el divisor negativo 
    (-6, 3, -2), #   - División con números negativos 
    (-6, -3, 2), #   - abmos numeros negativos
    (0, 5, 0)  # - cero dividido por un numero
])
def test_div_parametrize(a, b, esperado):
    assert div(a, b) == esperado
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
def test_div_por_cero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)
