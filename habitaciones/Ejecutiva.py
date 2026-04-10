from .Habitacion import Habitacion


class HabitacionEjecutiva(Habitacion):
    COSTO_EXTRA = 25.0
    DESCRIPCION = "Ideal para negocios. Escritorio y acceso al Lounge " "(Cargo extra de $25)."

    def __init__(
        self,
        numero: str,
        precio_noche: float = 120.0,
        estado: str = "disponible",
        huesped: str | None = None,
        noches: int = 0,
    ) -> None:
        super().__init__(
            numero=numero,
            tipo="Ejecutiva",
            precio_noche=precio_noche,
            descripcion=self.DESCRIPCION,
            estado=estado,
            huesped=huesped,
            noches=noches,
        )

    def calcular_total(self) -> float:
        return (self.noches * self.precio_noche) + self.COSTO_EXTRA
