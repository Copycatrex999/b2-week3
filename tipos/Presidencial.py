from .Habitacion import Habitacion


class HabitacionPresidencial(Habitacion):
    COSTO_EXTRA = 100.0
    DESCRIPCION = (
        "Penthouse completo con chef privado "
        "(Cargo extra de $100)."
    )

    def __init__(
        self,
        numero: str,
        precio_noche: float = 500.0,
        estado: str = "disponible",
        huesped: str | None = None,
        noches: int = 0,
    ) -> None:
        super().__init__(
            numero=numero,
            tipo="Presidencial",
            precio_noche=precio_noche,
            descripcion=self.DESCRIPCION,
            estado=estado,
            huesped=huesped,
            noches=noches,
        )

    def calcular_total(self) -> float:
        return (self.noches * self.precio_noche) + self.COSTO_EXTRA