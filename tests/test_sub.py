"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
@pytest.mark.parametrize("a, b, esperado", [
    (3, 8, -5),
    (5, 0, 5),
    (-3, -5, 2),
    (3.5, 2.5, 1),
])

def test_sub_parametrizado(a,b,esperado):
    assert sub(a,b) == esperado
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
