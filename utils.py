import math

def obtener_personas_cercanas(persona, espacio, distancia):
 cercanas = []
 for otra in espacio.personas:
     if otra != persona:
      d = math.sqrt((persona.x - otra.x)**2 + (persona.y - otra.y)**2)
      if d <= distancia:
       cercanas.append(otra)
 return cercanas


def calcular_persona_mas_cercana(persona, espacio):
 min_dist = float("inf")
 mas_cercana = None

 for otra in espacio.personas:
  if otra != persona:
   d = math.sqrt((persona.x - otra.x)**2 + (persona.y - otra.y)**2)
   if d < min_dist:
    min_dist = d
    mas_cercana = otra

 return mas_cercana