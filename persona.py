from datetime import datetime
import math

class Persona:
 def __init__(self, nombre, fecha_nacimiento, espacio, x=0, y=0):
     self.nombre = nombre
     self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
     self.x = x
     self.y = y
     self.espacio = espacio
     self.amigos = []
     self.enemigos = []
     self.nivel_influencia = 1
     espacio.agregar_persona(self)

 def calcular_edad(self):
     hoy = datetime.now()
     edad = hoy.year - self.fecha_nacimiento.year
     if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
         edad -= 1
     return edad

 def hablar(self, otra_persona , mensaje):
     if self.espacio == otra_persona.espacio:
         print(f"{self.nombre} le dice a {otra_persona.nombre}: '{mensaje}'")
     else:
         print("No están en el mismo espacio.")

 def mover_hacia(self, otra_persona):
     if self.espacio == otra_persona.espacio:
         self.x = otra_persona.x
         self.y = otra_persona.y
         print(f"{self.nombre} se movió hacia {otra_persona.nombre}.")
     else:
         print("No están en el mismo espacio.")

 def salir_del_espacio(self, nuevo_espacio):
     self.espacio.eliminar_persona(self)
     nuevo_espacio.agregar_persona(self)
     self.espacio = nuevo_espacio

 def distancia_a(self, otra_persona):
     return math.sqrt((self.x - otra_persona.x) ** 2 + (self.y - otra_persona.y) **2 )

 def hacer_amigo(self, otra_persona):
    if otra_persona != self and otra_persona not in self.amigos:
     self.amigos.append(otra_persona)
     otra_persona.amigos.append(self)
     print(f"{self.nombre} y {otra_persona.nombre} ahora son amigos.")
 
 def hacer_enemigo(self, otra_persona):
    if otra_persona != self and otra_persona not in self.enemigos:
     self.enemigos.append(otra_persona)
     otra_persona.enemigos.append(self)

     if otra_persona in self.amigos:
      self.amigos.remove(otra_persona)
      otra_persona.amigos.remove(self)
      print(f"{self.nombre} y {otra_persona.nombre} ahora son enemigos.")

 def influir(self, otra_persona):
    if otra_persona in self.enemigos:
     print(f"{self.nombre} no puede influir en {otra_persona.nombre} porque son enemigos.")
     return
    if otra_persona in self.amigos and self.nivel_influencia >= 1:
     print(f"{self.nombre} influyó en la decisión de {otra_persona.nombre}.")
    else: print(f"{self.nombre} no logró influir en {otra_persona.nombre}.")

def __str__(self):
     return f"{self.nombre} ({self.x}, {self.y})"