import pytest

from mymodule import functions


"""
Pruebas unitarias para cuatro funciones basicas de matemáticas.
"""
def test_add():
    assert functions.add(1, 2) == 3
    assert functions.add(1, -2) == -1
    assert functions.add(1, 0) == 1	

def test_subtract():
    assert functions.subtract(1, 2) == -1
    assert functions.subtract(1, -2) == 3
    assert functions.subtract(1, 0) == 1

def test_multiply():
    assert functions.multiply(1, 2) == 2
    assert functions.multiply(1, -2) == -2
    assert functions.multiply(1, 0) == 0

def test_divide():
    assert functions.divide(1, 2) == 0.5
    assert functions.divide(1, -2) == -0.5
    assert functions.divide(1, 1) == 1
    with pytest.raises(ZeroDivisionError):
        functions.divide(1, 0)
