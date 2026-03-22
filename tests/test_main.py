from unittest.mock import patch
from menu.Menu import menu


def test_iniciar_sistema_imprime_mensaje(capsys):
    # Usamos 'patch' para evitar que el Controlador intente leer el JSON real
    with patch("controlador.controller.Controlador._cargar_datos"):
        # Simulamos una entrada para que el menú se cierre rápido (opción 5: Salir)
        with patch("builtins.input", return_value="5"):
            menu()

    captured = capsys.readouterr()
    assert "SISTEMA DE GESTIÓN HOTELERA" in captured.out
    assert "¡Hasta pronto!" in captured.out
