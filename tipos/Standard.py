from .Habitacion import Habitacion


class HabitacionStandard(Habitacion):
    DESCRIPCION = "Habitación cómoda con cama matrimonial y TV por cable."

    def __init__(
        self,
        numero: str,
        precio_noche: float = 50.0,
        estado: str = "disponible",
        huesped: str | None = None,
        noches: int = 0,
    ) -> None:
        super().__init__(
            numero=numero,
            tipo="Standard",
            precio_noche=precio_noche,
            descripcion=self.DESCRIPCION,
            estado=estado,
            huesped=huesped,
            noches=noches,
        )

    def calcular_total(self) -> float:
        return self.noches * self.precio_noche
