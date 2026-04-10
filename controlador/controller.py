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

from .data import Data

# ==========================================
# Controlador
# ==========================================


class Controlador:
    def __init__(self, archivo_json="tiposHabitaciones.json") -> None:
        self.archivo_json = archivo_json
        self.data = Data(archivo_json)
        self.data.cargar_datos()
        self.habitaciones = self.data.habitaciones

    # Métodos privados de validación
    def _leer_cadena(self, mensaje: str) -> str:
        """evita que se deje en blanco"""
        while True:
            texto: str = input(mensaje).strip()
            if texto:
                return texto
            print("Error: Este campo no puede estar vacío.")

    def _leer_entero(self, mensaje: str, minimo: int = 1) -> int:  # Añade -> int
        while True:
            try:
                entrada = input(mensaje).strip()  # Lee sin anotar tipo aún
                numero = int(entrada)  # Convierte
                if numero >= minimo:
                    return numero
                else:
                    print(f" Error: Debe ingresar un número mayor o igual a {minimo}.")
            except ValueError:
                print(" Error: Por favor, ingrese un número válido.")

    # Métodos públicos
    def mostrar_todas_las_habitaciones(self) -> None:
        print("\n=== TODAS LAS HABITACIONES ===")
        for habitacion in self.habitaciones.values():
            print(habitacion)
        print("==============================")

    def mostrar_habitaciones_disponibles(self) -> bool:
        print("\n=== HABITACIONES DISPONIBLES ===")
        hay_disponibles: bool = False
        for habitacion in self.habitaciones.values():
            if habitacion.esta_disponible():
                print(habitacion)
                hay_disponibles = True

        if not hay_disponibles:
            print("No hay habitaciones disponibles.")
        print("================================")
        return hay_disponibles

    def hacer_check_in(self) -> None:
        if not self.mostrar_habitaciones_disponibles():
            return

        # Bucle para asegurar que elija una habitación correcta
        num_hab: str
        while True:
            num_hab = (
                input("\nIngrese el número de la habitación (o 'X' para cancelar): ")
                .strip()
                .upper()
            )

            if num_hab == "X":
                print(" Operación cancelada. Regresando al menú.")
                return

            if num_hab in self.habitaciones:
                habitacion = self.habitaciones[num_hab]
                if habitacion.esta_disponible():
                    break  # Salimos del bucle si la habitación es válida y libre
                else:
                    print("La habitación ya está ocupada. Elija otra.")
            else:
                print(" Número de habitación incorrecto. Intente de nuevo.")

        # Recopilación de datos validada
        nombre: str = self._leer_cadena(
            "Ingrese el nombre del huésped: "
        ).title()  # .title() pone mayúsculas (Juan Perez)
        noches: int = self._leer_entero("Ingrese la cantidad de noches: ", minimo=1)

        habitacion.ocupar(nombre, noches)

        datos_a_guardar: Dict[str, Dict[str, Any]] = {
            numero: hab.to_dict() for numero, hab in self.habitaciones.items()
        }

        self.data.guardar_datos(datos_a_guardar)
        print(f"\n CHECK-IN EXITOSO: La habitación {num_hab} ahora está ocupada por {nombre}.")

    def hacer_check_out(self) -> None:
        num_hab: str
        habitacion: Optional[Habitacion] = None  # Inicia en None

        while True:
            num_hab = input("\nIngrese el número... (o 'X'): ").strip().upper()

            if num_hab == "X":
                return

            if num_hab in self.habitaciones:
                habitacion = self.habitaciones[num_hab]
                # SOLUCIÓN ERROR 203+: Verificar que NO sea None explícitamente
                if habitacion is not None and not habitacion.esta_disponible():
                    break
                else:
                    print(" La habitación está vacía...")
            else:
                print(" Número incorrecto...")

        # Aquí Mypy ya sabe que 'habitacion' no es None gracias al 'break' de arriba
        if habitacion is not None:
            total: float = habitacion.calcular_total()

            print("\n === RECIBO DE CHECK-OUT ===")
            print(f"Huésped:   {habitacion.huesped}")
            print(f"Habitación: {habitacion.numero} ({habitacion.tipo})")
            print(f"Estadía:   {habitacion.noches} noches a ${habitacion.precio_noche}")
            print(f"TOTAL A PAGAR: ${total:.2f}")

            habitacion.liberar()
            datos_a_guardar: Dict[str, Dict[str, Any]] = {
                numero: hab.to_dict() for numero, hab in self.habitaciones.items()
            }
            self.data.guardar_datos(datos_a_guardar)
        print(f" Check-out exitoso. Habitación {num_hab} liberada y datos actualizados.")
