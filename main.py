import modele

systeme = modele.Systeme()

objet1 = modele.ObjetCeleste(230, [0, 0, 0], [0,0,0], systeme)
objet2 = modele.ObjetCeleste(250, [1, 0, 0], [0,0,0], systeme)

print("RUN")

for i in range(100):
    systeme.actualise()
    for objet in systeme.objets:
        print(f"OBJET{objet}: {objet.pos}")
