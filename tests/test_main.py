import pytest
from main import iniciar_sistema


def test_iniciar_sistema_imprime_mensaje(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Prueba que la función principal imprima exactamente el mensaje de bienvenida.
    """
    # 1. Ejecutamos la función que queremos probar
    iniciar_sistema()

    # 2. Capturamos lo que la función escribió en la terminal
    captura = capsys.readouterr()

    # 3. Comprobamos (assert) que el texto sea el esperado.
    # Nota: La función print() de Python siempre añade un salto de línea (\n) al final.
    assert captura.out == "¡Bienvenido al sistema!\n"
