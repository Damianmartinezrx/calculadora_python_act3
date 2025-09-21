import pytest
from main import suma, resta, multiplicacion, division

@pytest.mark.skip(reason="No es necesario ejecutar esta prueba ahora")
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

def test_division_flotante():
    assert division(10, 3) == pytest.approx(3.3333, rel=1e-4)
    assert division(-4.4, 2) == -2.2
    assert division(-3.3, -1.1) == pytest.approx(3.0, rel=1e-4)


@pytest.mark.zero
def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)  

