from abc import ABC, abstractmethod
from typing import Dict, Any


class Habitacion(ABC):
    def __init__(
        self,
        numero: str,
        tipo: str,
        precio_noche: float,
        descripcion: str,
        estado: str = "disponible",
        huesped: str | None = None,
        noches: int = 0,
    ) -> None:
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.descripcion = descripcion
        self.estado = estado
        self.huesped = huesped
        self.noches = noches

    @abstractmethod
    def calcular_total(self) -> float:
        raise NotImplementedError

    def esta_disponible(self) -> bool:
        return self.estado == "disponible"

    def ocupar(self, nombre_huesped: str, cantidad_noches: int) -> None:
        if not self.esta_disponible():
            raise ValueError("La habitación ya está ocupada")

        if cantidad_noches <= 0:
            raise ValueError("Las noches deben ser mayores a 0")

        self.estado = "ocupada"
        self.huesped = nombre_huesped
        self.noches = cantidad_noches

    def liberar(self) -> None:
        self.estado = "disponible"
        self.huesped = None
        self.noches = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "numero": self.numero,
            "tipo": self.tipo,
            "precio_noche": self.precio_noche,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "huesped": self.huesped,
            "noches": self.noches,
        }

    def __str__(self) -> str:
        base = (
            f"[{self.numero}] {self.tipo.upper()} - ${self.precio_noche}/noche\n"
            f"      Info: {self.descripcion}\n"
            f"      Estado: {self.estado.upper()}"
        )

        if not self.esta_disponible() and self.huesped:
            base += f" (Huésped: {self.huesped})"

        return base + "\n"
