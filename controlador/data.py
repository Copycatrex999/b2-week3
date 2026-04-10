import os
import json
from typing import Dict, Any, Union,Optional

from habitaciones import (
    HabitacionDeluxe,
    HabitacionEjecutiva,
    HabitacionStandard,
    Habitacion,
    HabitacionSuite,
    HabitacionPresidencial
)


class Data:
    def __init__(self, archivo_json:Dict[str, Dict[str, Any]]) -> None:
        self.archivo_json = archivo_json
        self.habitaciones: Dict[str, Habitacion] = {}

    def _inicializar_datos(self, forzar: bool = False):
        """Crea el archivo JSON con datos por defecto. Si 'forzar' es True, lo sobreescribe."""
        if not os.path.exists(self.archivo_json) or forzar:
            datos_iniciales = self.crear_datos_iniciales()
            with open(self.archivo_json, "w", encoding="utf-8") as archivo:
                json.dump(datos_iniciales, archivo, indent=4, ensure_ascii=False)

    def cargar_datos(self) -> None:
        #intenta carcar el JSON  de forma segura.s
        self._inicializar_datos() #se asegura de que exista antes de leer
        hab: Habitacion
        try:
            with open(self.archivo_json, "r", encoding="utf-8") as archivo:
                datos: Dict[int, Any] = json.load(archivo)
                for numero, info in datos.items():
                    hab = self.crear_habitacion()

                    self.habitaciones[numero] = hab

        except (json.JSONDecodeError, AttributeError):
            print(
                "\nERROR: El archivo de base de datos está corrupto. Restaurando a los valores por defecto..."
            )
            self._inicializar_datos(forzar=True)
            print("sexoooooo")
            self.cargar_datos()  # Reintenta cargar tras reparar

    def guardar_datos(self, datos_a_guardar:Dict[str, Dict[str, Any]]) -> None:

        with open(self.archivo_json, "w", encoding="utf-8") as archivo:
            json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)

    def crear_datos_iniciales(self):

        datos_iniciales: Dict[str, Any] = {
        "101": {
            "tipo": "Standard",
            "precio_noche": 50.0,
            "estado": "disponible",
            "huesped": "",
            "noches": 0,
        },
        "102": {
            "tipo": "Deluxe",
            "precio_noche": 80.0,
            "estado": "disponible",
            "huesped": "",
            "noches": 0,
        },
        "201": {
            "tipo": "Ejecutiva",
            "precio_noche": 120.0,
            "estado": "disponible",
            "huesped": "",
            "noches": 0,
        },
        "202": {
            "tipo": "Suite",
            "precio_noche": 200.0,
            "estado": "disponible",
            "huesped": "",
            "noches": 0,
        },
        "301": {
            "tipo": "Presidencial",
            "precio_noche": 500.0,
            "estado": "disponible",
            "huesped": "",
            "noches": 0,
        },
        }
        return datos_iniciales

    def crear_habitacion(self, numero, info)->Habitacion:
        tipo: str = info.get("tipo", "Standard")
        precio: float = info.get("precio_noche", 50.0)
        estado: str = info.get("estado", "disponible")
        huesped: str = info.get("huesped", "")
        noches: int = info.get("noches", 0)

        tipos_habitacion = {
            "Standard": HabitacionStandard,
            "Deluxe": HabitacionDeluxe,
            "Ejecutiva": HabitacionEjecutiva,
            "Suite": HabitacionSuite,
            "Presidencial": HabitacionPresidencial,
        }

        clase = tipos_habitacion.get(tipo, HabitacionStandard)

        return clase(numero, precio, estado, huesped, noches)
