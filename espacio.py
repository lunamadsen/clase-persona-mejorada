class Espacio:
 def __init__(self, nombre):
     self.nombre = nombre
     self.personas = []

 def agregar_persona(self, persona):
     if persona not in self.personas:
         self.personas.append(persona)

 def eliminar_persona(self, persona):
     if persona in self.personas:
         self.personas.remove(persona)
         print(f"{persona.nombre} salió del espacio {self.nombre}.")

 def mover_persona(self, persona, x, y):
     if persona in self.personas:
         persona.x = x
         persona.y = y
         print(f"{persona.nombre} se movió a ({x}, {y}).")

 def buscar_persona_por_nombre(self, nombre):
     for persona in self.personas:
         if persona.nombre == nombre:
             return persona
     return None