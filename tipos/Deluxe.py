from .Habitacion import Habitacion


class HabitacionDeluxe(Habitacion):
    COSTO_EXTRA = 15.0
    DESCRIPCION = (
        "Cama King size, balcón con vista y minibar "
        "(Cargo extra de $15)."
    )

    def __init__(
        self,
        numero: str,
        precio_noche: float = 80.0,
        estado: str = "disponible",
        huesped: str | None = None,
        noches: int = 0,
    ) -> None:
        super().__init__(
            numero=numero,
            tipo="Deluxe",
            precio_noche=precio_noche,
            descripcion=self.DESCRIPCION,
            estado=estado,
            huesped=huesped,
            noches=noches,
        )

    def calcular_total(self) -> float:
        return (self.noches * self.precio_noche) + self.COSTO_EXTRA