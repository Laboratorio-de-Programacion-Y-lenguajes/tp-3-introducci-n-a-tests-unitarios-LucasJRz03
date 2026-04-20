"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
@pytest.mark.parametrize("a, b, esperado", [
    (4, 0, 0),
    (-5,-7,35),
    (5, -8, -40),
    (4, 1, 4),
    (6, 2.5, 15),
])

def test_mul_parametrize(a, b, esperado):
    assert mul(a,b) == esperado
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
