# Importer math, random et tkinter
import math
import random
from tkinter import *
import datetime

points = 0
reponses = 0
nombres_calcul = 3
chrono = 0

# Fonction qui génère un calcul mental aléatoire
def generate_calculation(length):
    signes = ["+", "-", "*"]
    nombres = [random.randint(1, 10) for i in range(length)]
    newSigns = [random.choice(signes) for i in range(length-1)]
    # Join chaque nombre de nombre par le signe correspondant de newSigns
    question = []
    for i in range(length):
        question.append(str(nombres[i]))
        if i < length-1: question.append(newSigns[i])
    fenetre.calcul = " ".join(question)
    return fenetre.calcul
def valider():
    global points
    global nombres_calcul
    global reponses

    entry = entry_answer.get()
    answer = eval(fenetre.calcul)
    if entry == str(answer):
        points += 1
        resultat_text.config(text="Bravo ! Vous avez {} points".format(points), fg="green")
        calcul_text.config(text=generate_calculation(nombres_calcul))
        reponses += 1
    else:
        points = 0
        resultat_text.config(text="Dommage ! C'était {} = {}... Vous avez {} points".format(fenetre.calcul, answer, points), fg="red")
        calcul_text.config(text=generate_calculation(nombres_calcul))
    # Effacer la valeur de l'entrée
    entry_answer.delete(0, END)
    return
def changer_nombre_calcul():
    global nombres_calcul
    global points
    global reponses
    global chrono
    points = 0
    nombres_calcul = int(entry_nombre_calcul.get())
    reponses = 0
    chrono = 0
    calcul_text.config(text=generate_calculation(nombres_calcul))
    return
def update_chrono():
    # Créer un boucle qui va éditer le chrono toutes les secondes et l'afficher sous la forme: "Chronomètre: 00:00:00"
    global chrono
    chrono += 1
    chrono_text.config(text="Chronomètre: {}".format(str(datetime.timedelta(seconds=chrono))))
    update_moyenne_reponses()
    fenetre.after(1000, update_chrono)
def update_moyenne_reponses():
    global chrono
    global reponses

    moyenne = reponses / chrono
    # Arrondir au centième
    moyenne = math.ceil(moyenne * 100) / 100
    moyenne_text.config(text="Moyenne de réponses par seconde: {} ({})".format(moyenne, reponses))

# Créer la fenêtre
fenetre = Tk()
fenetre.geometry("400x300")
fenetre.calcul_resultat = ""

# Créer un titre: "Bienvenu au jeu du calcul mental"
titre = Label(fenetre, text="Bienvenu au jeu du calcul mental")
titre.pack()

# Créer un chronomètre
chrono_text = Label(fenetre, text="Chronomètre: 0:00", fg="red")
chrono_text.pack()

# Créer une zone de moyenne de réponses par 10 minutes
moyenne_text = Label(fenetre, text="Moyenne de réponses par seconde: 0 (0)", fg="blue")
moyenne_text.pack()

# Créer un tableau avec le titre: "Calcul:" et le calcul généré avec la fonction generate_calculation
calcul = Label(fenetre, text="Calcul:")
calcul.pack()
calcul_text = Label(fenetre, text=generate_calculation(nombres_calcul))
calcul_text.pack() 

# Créer une zone de nombre
entry_answer = Entry(fenetre, width=10)
entry_answer.pack()

# Créer un boutton "Valider"
boutton_valider = Button(fenetre, text="Valider", command=valider)
boutton_valider.pack()

# Créer une zone de texte pour afficher les résultats
resultat = Label(fenetre, text="Résultat:")
resultat.pack()
resultat_text = Label(fenetre, text=fenetre.calcul_resultat)
resultat_text.pack()

# Créer un titre: Changer la longueur du calcul
titre_nombre_calcul = Label(fenetre, text="Changer la longueur du calcul: ")
titre_nombre_calcul.pack()
# Créer un input pour changer le nombre de calcul
entry_nombre_calcul = Entry(fenetre, width=10)
entry_nombre_calcul.pack()
# Créer le bouton pour changer le nombre de calcul
boutton_nombre_calcul = Button(fenetre, text="Changer", command=changer_nombre_calcul)
boutton_nombre_calcul.pack()

# Créer un boutton "Quitter"
boutton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
boutton_quitter.pack()

update_chrono()
# Lancer la boucle principale
fenetre.mainloop()