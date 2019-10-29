#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *
from PIL import Image, ImageTk

# Constantes
APPLICATION_NAME = "CAA-CreateAnAlgorithm"
POURCENT_BT = 0.035
POURCENT_BT_CHOIX = 0.08
POURCENT_BARRE = 0.8
POURCENT_FCT_T = 0.0787

# Variables
quelMenu = "main"


# Création de la fenêtre principale
root = Tk()


# Mise en plein écran et renommage de root
root.attributes("-fullscreen", 1)
root.title(APPLICATION_NAME)


# Largeur et hauteur de l'écran
w = root.winfo_screenwidth()
h = root.winfo_screenheight()


# Canvas contenant les éléments visuels de l'application
main = Canvas(root, highlightthickness=0)
fonctionC = Canvas(root, highlightthickness=0)
procedureC = Canvas(root, highlightthickness=0)
programmeC = Canvas(root, highlightthickness=0)


def affImage(nomI, x, y, width, height):
    image_pil = Image.open('images/%s.png' % nomI)
    imageR = (width, height)
    image_img = ImageTk.PhotoImage(image_pil.resize(imageR))
    fonctionC.create_image(x, y, image=image_img)


# Création du fond d'écran image
fond_pil = Image.open('images/fond.png')
fond_resolution = (w, h)
fond_img = ImageTk.PhotoImage(fond_pil.resize(fond_resolution))
fond = main.create_image(w / 2, h / 2, image=fond_img)
fonctionC.create_image(w / 2, h / 2, image=fond_img)
procedureC.create_image(w / 2, h / 2, image=fond_img)
programmeC.create_image(w / 2, h / 2, image=fond_img)


# Bouton fermer
fermer_pil = Image.open('images/fermer.png')
fermerR = (int(h * POURCENT_BT * 1.5), int(h * POURCENT_BT))
fermer_img = ImageTk.PhotoImage(fermer_pil.resize(fermerR))
main.create_image(w - (fermerR[0] / 2), 0 + (fermerR[1] / 2), image=fermer_img)
fonctionC.create_image(w - (fermerR[0] / 2), 0 + (fermerR[1] / 2), image=fermer_img)
procedureC.create_image(w - (fermerR[0] / 2), 0 + (fermerR[1] / 2), image=fermer_img)
programmeC.create_image(w - (fermerR[0] / 2), 0 + (fermerR[1] / 2), image=fermer_img)


# Bouton reduire
reduire_pil = Image.open('images/reduire.png')
reduireR = (int(h * POURCENT_BT * 1.5), int(h * POURCENT_BT))
reduire_img = ImageTk.PhotoImage(reduire_pil.resize(reduireR))
main.create_image(w - (reduireR[0] / 2) * 3, 0 + (reduireR[1] / 2), image=reduire_img)
fonctionC.create_image(w - (reduireR[0] / 2) * 3, 0 + (reduireR[1] / 2), image=reduire_img)
procedureC.create_image(w - (reduireR[0] / 2) * 3, 0 + (reduireR[1] / 2), image=reduire_img)
programmeC.create_image(w - (reduireR[0] / 2) * 3, 0 + (reduireR[1] / 2), image=reduire_img)


# Bouton fonction
fonction_pil = Image.open('images/fonction.png')
fonctionR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
fonction_img = ImageTk.PhotoImage(fonction_pil.resize(fonctionR))
main.create_image(w/4, h*0.05, image=fonction_img)
procedureC.create_image(w/4, h*0.05, image=fonction_img)
programmeC.create_image(w/4, h*0.05, image=fonction_img)


# Bouton procedure
procedure_pil = Image.open('images/procedure.png')
procedureR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
procedure_img = ImageTk.PhotoImage(procedure_pil.resize(procedureR))
main.create_image(w/2, h*0.05, image=procedure_img)
fonctionC.create_image(w/2, h*0.05, image=procedure_img)
programmeC.create_image(w/2, h*0.05, image=procedure_img)


# Bouton programme
programme_pil = Image.open('images/programme.png')
programmeR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
programme_img = ImageTk.PhotoImage(programme_pil.resize(programmeR))
main.create_image((3*w)/4, h*0.05, image=programme_img)
fonctionC.create_image((3*w)/4, h*0.05, image=programme_img)
procedureC.create_image((3*w)/4, h*0.05, image=programme_img)


# Création du bouton selectionné
fonctionS_pil = Image.open('images/fonctionSel.png')
fonctionSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
fonctionS_img = ImageTk.PhotoImage(fonctionS_pil.resize(fonctionSR))
fonctionC.create_image(w/4, h*0.05, image=fonctionS_img)


# Création du bouton selectionné
procedureS_pil = Image.open('images/procedureSel.png')
procedureSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
procedureS_img = ImageTk.PhotoImage(procedureS_pil.resize(procedureSR))
procedureC.create_image(w/2, h*0.05, image=procedureS_img)


# Création du bouton selectionné
programmeS_pil = Image.open('images/programmeSel.png')
programmeSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
programmeS_img = ImageTk.PhotoImage(programmeS_pil.resize(programmeSR))
programmeC.create_image((3*w)/4, h*0.05, image=programmeS_img)


barreS_pil = Image.open('images/barreSep.png')
barreSR = (int(h * POURCENT_BARRE * 0.03), int(h * POURCENT_BARRE))
barreS_img = ImageTk.PhotoImage(barreS_pil.resize(barreSR))
fonctionC.create_image(w/2, h/2+h*0.05, image=barreS_img)
procedureC.create_image(w/2, h/2+h*0.05, image=barreS_img)
programmeC.create_image(w/2, h/2+h*0.05, image=barreS_img)


def reduireProg():
    root.state('iconic')


def fermerProg():
    root.quit()


def affCanvasFonction():
    fonctionC.place(x=0, y=0, width=w, height=h)
    procedureC.place_forget()
    programmeC.place_forget()
    main.place_forget()


def affCanvasProcedure():
    fonctionC.place_forget()
    procedureC.place(x=0, y=0, width=w, height=h)
    programmeC.place_forget()
    main.place_forget()


def affCanvasProgramme():
    fonctionC.place_forget()
    procedureC.place_forget()
    programmeC.place(x=0, y=0, width=w, height=h)
    main.place_forget()


def oeilDeMoscou(event):
    print(event.x, "x", event.y)

    if (w - fermerR[0] - reduireR[0]) < event.x < (w - fermerR[0]) and 0 < event.y < reduireR[1]:
        reduireProg()

    if (w - fermerR[0]) < event.x < w and 0 < event.y < reduireR[1]:
        fermerProg()

    if (w/4 - fonctionR[0]/2 < event.x < w/4 + fonctionR[0]/2) and (h*0.05)-(fonctionR[1]/2) < event.y < (h*0.05)+(fonctionR[1]/2) :
        affCanvasFonction()
        quelMenu = "fonction"

    if (w/2 - procedureR[0]/2 < event.x < w/2 + procedureR[0]/2) and (h*0.05)-(procedureR[1]/2) < event.y < (h*0.05)+(procedureR[1]/2) :
        affCanvasProcedure()
        quelMenu = "procedure"

    if ((3*w)/4 - programmeR[0]/2 < event.x < (3*w)/4 + programmeR[0]/2) and (h*0.05)-(programmeR[1]/2) < event.y < (h*0.05)+(programmeR[1]/2) :
        affCanvasProgramme()
        quelMenu = "programme"


fonction_text_pil = Image.open('images/text_fonction.png')
fonction_textR = (int(h*POURCENT_FCT_T*3.41), int(h*POURCENT_FCT_T))
fonction_text_img = ImageTk.PhotoImage(fonction_text_pil.resize(fonction_textR))
fonctionC.create_image(w*0.1016, h*0.191, image=fonction_text_img)

role_text_pil = Image.open('images/text_role.png')
role_textR = (int(h*POURCENT_FCT_T*1.88), int(h*POURCENT_FCT_T))
role_text_img = ImageTk.PhotoImage(role_text_pil.resize(role_textR))
fonctionC.create_image(w*0.5833, h*0.191, image=role_text_img)

nomFonctionEntry = Text(fonctionC)
nomFonctionEntry.place(x=(w*0.1849), y=h*0.1574, width=int(w*0.296875), height=int(h*0.065))

roleFonctionEntry = Text(fonctionC)
roleFonctionEntry.place(x=(w*0.628), y=h*0.1574, width=int(w*0.3594), height=int(h*0.065))

root.bind('<Button-1>', oeilDeMoscou)

# Affichage du main
fonctionC.place(x=0, y=0, width=w, height=h)



# Lancement de l'application
root.mainloop()
