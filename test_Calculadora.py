import pytest
from main import suma, resta, multiplicacion, division


@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 5),
    (-1, 1, 0),
    (-1, -1, -2)
])
def test_suma(a, b, expected):
    assert suma(a, b) == expected


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

@pytest.mark.parametrize("a, b", [
    (1, 0),
    (0, 0),
    (-1, 0) 
])
def test_division_por_cero(a, b):
    with pytest.raises(ZeroDivisionError):
        division(a, b)