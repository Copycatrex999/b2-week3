from tipos.Deluxe import HabitacionDeluxe
from tipos.Ejecutiva import HabitacionEjecutiva
from tipos.Presidencial import HabitacionPresidencial
from tipos.Suite import HabitacionSuite
from tipos.Standard import HabitacionStandard
import pytest


def test_habitacion_standard_calculo():
    hab = HabitacionStandard(numero="101", noches=2)
    assert hab.calcular_total() == 100.0


def test_habitacion_deluxe_calculo():
    hab = HabitacionDeluxe(numero="102", noches=2)
    assert hab.calcular_total() == (2 * 80.0) + 15.0


def test_habitacion_ejecutiva_calculo():
    hab = HabitacionEjecutiva(numero="103", noches=2)
    assert hab.calcular_total() == (2 * 120.0) + 25.0


def test_habitacion_presidencial_calculo():
    hab = HabitacionPresidencial(numero="104", noches=1)
    assert hab.calcular_total() == 600.0  # 500 + 100


def test_habitacion_suite_calculo():
    hab = HabitacionSuite(numero="105", noches=2)
    assert hab.calcular_total() == pytest.approx(440.0)
