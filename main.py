from espacio import Espacio
from persona import Persona
import utils

parque = Espacio("Parque")

ana = Persona("Ana", "2000-05-10", parque, 0, 0)
luis = Persona("Luis", "1998-03-22", parque, 3, 4)
maria = Persona("Maria", "2001-07-15", parque, 1, 1)

ana.hablar(luis, "Hola!")

cercanas = utils.obtener_personas_cercanas(ana, parque, 2)
print("Personas cercanas a Ana:", [p.nombre for p in cercanas])

mas_cercana = utils.calcular_persona_mas_cercana(ana, parque)
print("La persona más cercana a Ana es:", mas_cercana.nombre)

ana.hacer_amigo(luis)
ana.influir(luis)
ana.hacer_enemigo(maria)
ana.influir(maria)

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

G.add_node(ana.nombre)
G.add_node(luis.nombre)
G.add_node(maria.nombre)

G.add_edge(ana.nombre, luis.nombre)
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.show()