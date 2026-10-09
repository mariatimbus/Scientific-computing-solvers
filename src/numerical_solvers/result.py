"""Rezultatul unei rulări de solver."""


from dataclasses import dataclass, field


@dataclass
class SolveResult:
    """Rezultatul unei rulări care s-a oprit cu succes.

    Atribute:
        root: Aproximația finală (float scalar sau vector numpy).
        iterations: Numărul de iterații (pași de actualizare) efectuate.
        residual: Reziduul final, |f(root)| (norma infinit la sisteme).
        history: Înregistrările pe fiecare iterație; câmpurile depind de metodă.
        reason: Motivul opririi.
    """

    root: object
    iterations: int
    residual: float
    history: list = field(default_factory=list)
    reason: str = ""

    def summary(self):
        return (
            f"root={self.root}  iterations={self.iterations}  "
            f"residual={self.residual:.3e}  reason={self.reason!r}"
        )
