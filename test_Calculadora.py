import pytest
from main import suma, resta, multiplicacion, division

def test_suma():
    assert suma(3, 2) == 5
    assert suma(-1, 1) == 0
    assert suma(-1, -1) == -2

def test_resta():
    assert resta(3, 2) == 1
    assert resta(-1, 1) == -2
    assert resta(-1, -1) == 0

def test_multiplicacion():
    assert multiplicacion(3, 2) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(-1, -1) == 1

def test_division():
    assert division(3, 2) == 1.5
    assert division(-1, 1) == -1
    assert division(-1, -1) == 1    