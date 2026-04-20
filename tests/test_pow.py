"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
@pytest.mark.parametrize("a,b, esperado", [
    (5, 0, 1),
    (5, 1, 5),
    (-5, 2, 25),
    (-2, 3, -8), #Base negativa con exponente impar (resultado negativo)
    (9, 0.5, 3.0),
    (0, 8, 0), # 0 a cualquier potencia positiva es 0
])

def test_pow_parametrize(a, b, esperado):
    assert pow_(a, b) == esperado
    
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
