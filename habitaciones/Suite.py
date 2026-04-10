from .Habitacion import Habitacion


class HabitacionSuite(Habitacion):
    PORCENTAJE_EXTRA = 0.10
    DESCRIPCION = "Jacuzzi y room service premium (Cargo extra del 10%)."

    def __init__(
        self,
        numero: str,
        precio_noche: float = 200.0,
        estado: str = "disponible",
        huesped: str | None = None,
        noches: int = 0,
    ) -> None:
        super().__init__(
            numero=numero,
            tipo="Suite",
            precio_noche=precio_noche,
            descripcion=self.DESCRIPCION,
            estado=estado,
            huesped=huesped,
            noches=noches,
        )

    def calcular_total(self) -> float:
        costo_base = self.noches * self.precio_noche
        return costo_base * (1 + self.PORCENTAJE_EXTRA)
