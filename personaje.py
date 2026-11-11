from dataclasses import dataclass

@dataclass
class Personaje:
    nombre: str
    vida: int
    ataque: int
    defensa: int
    nivel: int

personaje = Personaje(nombre="Aragorn", vida=-100, ataque=18, defensa=15, nivel=1)

print(f"Nombre: {personaje.nombre}, Vida: {personaje.vida}, Ataque: {personaje.ataque}, Defensa: {personaje.defensa}, Nivel: {personaje.nivel}")