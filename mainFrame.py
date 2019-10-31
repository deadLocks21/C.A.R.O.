#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *
from PIL import Image, ImageTk
import time
from generationFonction import *
from generationProcedure import *
from generationProgramme import *


def printLogTkinter(s):
    t = str(time.localtime()[2]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[0]) + " " + str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5])
    print(t + " [TK] " + s)


# Constantes
APPLICATION_NAME = "C.A.R.O."
POURCENT_BT = 0.035
POURCENT_BT_CHOIX = 0.08
POURCENT_BARRE = 0.8
POURCENT_FCT_T = 0.0787
CHEMIN_ENREGISTREMENT = "D:\\Users\\deadLocks21\\Desktop\\"

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

main_pil = Image.open('images/main.png')
main_resolution = (w, h)
main_img = ImageTk.PhotoImage(main_pil.resize(main_resolution))
main.create_image(w / 2, h / 2, image=main_img)

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
main.create_image(w / 4, h * 0.05, image=fonction_img)
procedureC.create_image(w / 4, h * 0.05, image=fonction_img)
programmeC.create_image(w / 4, h * 0.05, image=fonction_img)

# Bouton procedure
procedure_pil = Image.open('images/procedure.png')
procedureR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
procedure_img = ImageTk.PhotoImage(procedure_pil.resize(procedureR))
main.create_image(w / 2, h * 0.05, image=procedure_img)
fonctionC.create_image(w / 2, h * 0.05, image=procedure_img)
programmeC.create_image(w / 2, h * 0.05, image=procedure_img)

# Bouton programme
programme_pil = Image.open('images/programme.png')
programmeR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
programme_img = ImageTk.PhotoImage(programme_pil.resize(programmeR))
main.create_image((3 * w) / 4, h * 0.05, image=programme_img)
fonctionC.create_image((3 * w) / 4, h * 0.05, image=programme_img)
procedureC.create_image((3 * w) / 4, h * 0.05, image=programme_img)

# Création du bouton selectionné
fonctionS_pil = Image.open('images/fonctionSel.png')
fonctionSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
fonctionS_img = ImageTk.PhotoImage(fonctionS_pil.resize(fonctionSR))
fonctionC.create_image(w / 4, h * 0.05, image=fonctionS_img)

# Création du bouton selectionné
procedureS_pil = Image.open('images/procedureSel.png')
procedureSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
procedureS_img = ImageTk.PhotoImage(procedureS_pil.resize(procedureSR))
procedureC.create_image(w / 2, h * 0.05, image=procedureS_img)

# Création du bouton selectionné
programmeS_pil = Image.open('images/programmeSel.png')
programmeSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
programmeS_img = ImageTk.PhotoImage(programmeS_pil.resize(programmeSR))
programmeC.create_image((3 * w) / 4, h * 0.05, image=programmeS_img)

barreS_pil = Image.open('images/barreSep.png')
barreSR = (int(h * POURCENT_BARRE * 0.03), int(h * POURCENT_BARRE))
barreS_img = ImageTk.PhotoImage(barreS_pil.resize(barreSR))
fonctionC.create_image(w / 2, h / 2 + h * 0.05, image=barreS_img)
procedureC.create_image(w / 2, h / 2 + h * 0.05, image=barreS_img)
programmeC.create_image(w / 2, h / 2 + h * 0.05, image=barreS_img)


def reduireProg():
    root.state('iconic')


def fermerProg():
    root.quit()
    root.destroy()


def affCanvasFonction():
    procedureC.place_forget()
    programmeC.place_forget()
    main.place_forget()
    fonctionC.place(x=0, y=0, width=w, height=h)


def affCanvasProcedure():
    fonctionC.place_forget()
    programmeC.place_forget()
    main.place_forget()
    procedureC.place(x=0, y=0, width=w, height=h)


def affCanvasProgramme():
    fonctionC.place_forget()
    procedureC.place_forget()
    main.place_forget()
    programmeC.place(x=0, y=0, width=w, height=h)


def oeilDeMoscou(event):
    global quelMenu

    print(event.x, "x", event.y)

    if (w - fermerR[0] - reduireR[0]) < event.x < (w - fermerR[0]) and 0 < event.y < reduireR[1]:
        reduireProg()
        printLogTkinter("Réduction de la fenêtre.")

    if (w - fermerR[0]) < event.x < w and 0 < event.y < reduireR[1]:
        fermerProg()
        printLogTkinter("Fermeture de la fenêtre.")

    if (w / 4 - fonctionR[0] / 2 < event.x < w / 4 + fonctionR[0] / 2) and (h * 0.05) - (fonctionR[1] / 2) < event.y < (
            h * 0.05) + (fonctionR[1] / 2):
        affCanvasFonction()
        quelMenu = "fonction"
        printLogTkinter("Ouverture du menu Fonction.")

    if (w / 2 - procedureR[0] / 2 < event.x < w / 2 + procedureR[0] / 2) and (h * 0.05) - (
            procedureR[1] / 2) < event.y < (h * 0.05) + (procedureR[1] / 2):
        affCanvasProcedure()
        quelMenu = "procedure"
        printLogTkinter("Ouverture du menu Procédure.")

    if ((3 * w) / 4 - programmeR[0] / 2 < event.x < (3 * w) / 4 + programmeR[0] / 2) and (h * 0.05) - (
            programmeR[1] / 2) < event.y < (h * 0.05) + (programmeR[1] / 2):
        affCanvasProgramme()
        quelMenu = "programme"
        printLogTkinter("Ouverture du menu Programme.")

    if ((w * 0.75) - (int(h * POURCENT_FCT_T * 6.7765))/2 < event.x < w * 0.75 + (int(h * POURCENT_FCT_T * 6.7765)))/2 and (
            (h * 0.9421) - (int(h * POURCENT_FCT_T)) < event.y < (h * 0.9421) + (int(h * POURCENT_FCT_T))):
        if quelMenu == "fonction":
            nomF = str(nomFonctionEntry.get(1.0, 'end')).replace("\n", "")
            roleF = str(roleFonctionEntry.get(1.0, 'end')).replace("\n", "")
            paramEF = str(paramEFonctionEntry.get(1.0, 'end'))
            typeValRF = str(typeValRFonctionEntry.get(1.0, 'end')).replace("\n", "")
            varConst = str(varEtConstFonctionEntry.get(1.0, 'end'))
            jEF = str(jeuxEssaisFonctionEntry.get(1.0, 'end'))
            principeF = str(principeFonctionEntry.get(1.0, 'end')).replace("\n", "")
            vJEF = str(valJEFonctionEntry.get(1.0, 'end'))
            genFct(nomF, roleF, paramEF, typeValRF, varConst, jEF, principeF, vJEF, CHEMIN_ENREGISTREMENT)
            printLogTkinter("Enregistrement du fichier %s.html dans le repertoire %s." % (str(nomFonctionEntry.get(1.0, 'end')).replace("\n", ""), CHEMIN_ENREGISTREMENT))

        if quelMenu == "procedure":
            nom = str(nomProcedureEntry.get(1.0, 'end')).replace("\n", "")
            role = str(roleProcedureEntry.get(1.0, 'end')).replace("\n", "")
            paramE = str(paramEProcedureEntry.get(1.0, 'end'))
            PSES = str(PSESProcedureEntry.get(1.0, 'end'))
            varConst = str(varEtConstProcedureEntry.get(1.0, 'end'))
            jEF = str(jeuxEssaisProcedureEntry.get(1.0, 'end'))
            principe = str(principeProcedureEntry.get(1.0, 'end')).replace("\n", "")
            vJE = str(valJEProcedureEntry.get(1.0, 'end'))
            genProc(nom, role, paramE, PSES, varConst, jEF, principe, vJE, CHEMIN_ENREGISTREMENT)
            printLogTkinter("Enregistrement du fichier %s.html dans le repertoire %s." % (str(nomProcedureEntry.get(1.0, 'end')).replace("\n", ""), CHEMIN_ENREGISTREMENT))

        if quelMenu == "programme":
            nom = str(nomProgrammeEntry.get(1.0, 'end')).replace("\n", "")
            role = str(roleProgrammeEntry.get(1.0, 'end')).replace("\n", "")
            donnee = str(donneeProgrammeEntry.get(1.0, 'end'))
            res = str(resProgrammeEntry.get(1.0, 'end'))
            varConst = str(varEtConstProgrammeEntry.get(1.0, 'end'))
            jEF = str(jeuxEssaisProgrammeEntry.get(1.0, 'end'))
            principe = str(principeProgrammeEntry.get(1.0, 'end')).replace("\n", "")
            vJE = str(valJEProgrammeEntry.get(1.0, 'end'))
            genProg(nom, role, donnee, res, varConst, jEF, principe, vJE, CHEMIN_ENREGISTREMENT)
            printLogTkinter("Enregistrement du fichier %s.html dans le repertoire %s." % (str(nomProgrammeEntry.get(1.0, 'end')).replace("\n", ""), CHEMIN_ENREGISTREMENT))


fonction_text_pil = Image.open('images/text_fonction.png')
fonction_textR = (int(h * POURCENT_FCT_T * 3.41), int(h * POURCENT_FCT_T))
fonction_text_img = ImageTk.PhotoImage(fonction_text_pil.resize(fonction_textR))
fonctionC.create_image(w * 0.1016, h * 0.191, image=fonction_text_img)

procedure_text_pil = Image.open('images/text_procedure.png')
procedure_textR = (int(h * POURCENT_FCT_T * 4.176), int(h * POURCENT_FCT_T))
procedure_text_img = ImageTk.PhotoImage(procedure_text_pil.resize(procedure_textR))
procedureC.create_image(w * 0.1185, h * 0.191, image=procedure_text_img)

programme_text_pil = Image.open('images/text_programme.png')
programme_textR = (int(h * POURCENT_FCT_T * 4.588), int(h * POURCENT_FCT_T))
programme_text_img = ImageTk.PhotoImage(programme_text_pil.resize(programme_textR))
programmeC.create_image(w * 0.1276, h * 0.191, image=programme_text_img)

role_text_pil = Image.open('images/text_role.png')
role_textR = (int(h * POURCENT_FCT_T * 1.88), int(h * POURCENT_FCT_T))
role_text_img = ImageTk.PhotoImage(role_text_pil.resize(role_textR))
fonctionC.create_image(w * 0.5833, h * 0.191, image=role_text_img)
procedureC.create_image(w * 0.5833, h * 0.191, image=role_text_img)
programmeC.create_image(w * 0.5833, h * 0.191, image=role_text_img)

nomFonctionEntry = Text(fonctionC)
nomFonctionEntry.place(x=(w * 0.1849), y=h * 0.1574, width=int(w * 0.296875), height=int(h * 0.065))
nomProcedureEntry = Text(procedureC)
nomProcedureEntry.place(x=(w * 0.21615), y=h * 0.1574, width=int(w * 0.265625), height=int(h * 0.065))
nomProgrammeEntry = Text(programmeC)
nomProgrammeEntry.place(x=(w * 0.2396), y=h * 0.1574, width=int(w * 0.24219), height=int(h * 0.065))

roleFonctionEntry = Text(fonctionC)
roleFonctionEntry.place(x=(w * 0.628), y=h * 0.1574, width=int(w * 0.3594), height=int(h * 0.065))
roleProcedureEntry = Text(procedureC)
roleProcedureEntry.place(x=(w * 0.628), y=h * 0.1574, width=int(w * 0.3594), height=int(h * 0.065))
roleProgrammeEntry = Text(programmeC)
roleProgrammeEntry.place(x=(w * 0.628), y=h * 0.1574, width=int(w * 0.3594), height=int(h * 0.065))

glossaire_text_pil = Image.open('images/text_glossaire.png')
glossaire_textR = (int(h * POURCENT_FCT_T * 3.294), int(h * POURCENT_FCT_T))
glossaire_text_img = ImageTk.PhotoImage(glossaire_text_pil.resize(glossaire_textR))
fonctionC.create_image(w / 4, h * 0.28, image=glossaire_text_img)
procedureC.create_image(w / 4, h * 0.28, image=glossaire_text_img)
programmeC.create_image(w / 4, h * 0.28, image=glossaire_text_img)

algorithme_text_pil = Image.open('images/text_algorithme.png')
algorithme_textR = (int(h * POURCENT_FCT_T * 3.294), int(h * POURCENT_FCT_T))
algorithme_text_img = ImageTk.PhotoImage(algorithme_text_pil.resize(algorithme_textR))
fonctionC.create_image(3 * w / 4, h * 0.28, image=algorithme_text_img)
procedureC.create_image(3 * w / 4, h * 0.28, image=algorithme_text_img)
programmeC.create_image(3 * w / 4, h * 0.28, image=algorithme_text_img)

paramEntree_text_pil = Image.open('images/text_paramEntree.png')
paramEntree_textR = (int(h * POURCENT_FCT_T * 7.941), int(h * POURCENT_FCT_T))
paramEntree_text_img = ImageTk.PhotoImage(paramEntree_text_pil.resize(paramEntree_textR))
fonctionC.create_image(w * 0.25, h * 0.3727, image=paramEntree_text_img)
procedureC.create_image(w * 0.25, h * 0.3727, image=paramEntree_text_img)

donnee_text_pil = Image.open('images/text_donnee.png')
donnee_textR = (int(h * POURCENT_FCT_T * 3.294), int(h * POURCENT_FCT_T))
donnee_text_img = ImageTk.PhotoImage(donnee_text_pil.resize(donnee_textR))
programmeC.create_image(w * 0.25, h * 0.3727, image=donnee_text_img)

paramEFonctionEntry = Text(fonctionC)
paramEFonctionEntry.place(x=(w * 0.026), y=h * 0.4167, width=int(w * 0.4375), height=int(h * 0.2037))
paramEProcedureEntry = Text(procedureC)
paramEProcedureEntry.place(x=(w * 0.026), y=h * 0.4167, width=int(w * 0.4375), height=int(h * 0.1204))
donneeProgrammeEntry = Text(programmeC)
donneeProgrammeEntry.place(x=(w * 0.026), y=h * 0.4167, width=int(w * 0.4375), height=int(h * 0.1204))

typeValR_text_pil = Image.open('images/text_typeValR.png')
typeValR_textR = (int(h * POURCENT_FCT_T * 6.823), int(h * POURCENT_FCT_T))
typeValR_text_img = ImageTk.PhotoImage(typeValR_text_pil.resize(typeValR_textR))
fonctionC.create_image(w * 0.177, h * 0.6644, image=typeValR_text_img)

PSES_text_pil = Image.open('images/text_PSES.png')
PSES_textR = (int(h * POURCENT_FCT_T * 9.53), int(h * POURCENT_FCT_T))
PSES_text_img = ImageTk.PhotoImage(PSES_text_pil.resize(PSES_textR))
procedureC.create_image(w * 0.25, h * 0.5949, image=PSES_text_img)

res_text_pil = Image.open('images/text_res.png')
res_textR = (int(h * POURCENT_FCT_T * 3.47), int(h * POURCENT_FCT_T))
res_text_img = ImageTk.PhotoImage(res_text_pil.resize(res_textR))
programmeC.create_image(w * 0.25, h * 0.5949, image=res_text_img)

typeValRFonctionEntry = Text(fonctionC)
typeValRFonctionEntry.place(x=(w * 0.3333), y=h * 0.6389, width=int(w * 0.1302), height=int(h * 0.0601))
PSESProcedureEntry = Text(procedureC)
PSESProcedureEntry.place(x=(w * 0.026), y=h * 0.6389, width=int(w * 0.4375), height=int(h * 0.1204))
resProgrammeEntry = Text(programmeC)
resProgrammeEntry.place(x=(w * 0.026), y=h * 0.6389, width=int(w * 0.4375), height=int(h * 0.1204))

varEtConst_text_pil = Image.open('images/text_varEtConst.png')
varEtConst_textR = (int(h * POURCENT_FCT_T * 8.529), int(h * POURCENT_FCT_T))
varEtConst_text_img = ImageTk.PhotoImage(varEtConst_text_pil.resize(varEtConst_textR))
fonctionC.create_image(w * 0.25, h * 0.7477, image=varEtConst_text_img)
procedureC.create_image(w * 0.25, h * 0.8171, image=varEtConst_text_img)
programmeC.create_image(w * 0.25, h * 0.8171, image=varEtConst_text_img)

varEtConstFonctionEntry = Text(fonctionC)
varEtConstFonctionEntry.place(x=(w * 0.026), y=h * 0.7917, width=int(w * 0.4375), height=int(h * 0.2))
varEtConstProcedureEntry = Text(procedureC)
varEtConstProcedureEntry.place(x=(w * 0.026), y=h * 0.8611, width=int(w * 0.4375), height=int(h * 0.1203))
varEtConstProgrammeEntry = Text(programmeC)
varEtConstProgrammeEntry.place(x=(w * 0.026), y=h * 0.8611, width=int(w * 0.4375), height=int(h * 0.1203))

jeuxEssais_text_pil = Image.open('images/text_jeuxEssais.png')
jeuxEssais_textR = (int(h * POURCENT_FCT_T * 5.294), int(h * POURCENT_FCT_T))
jeuxEssais_text_img = ImageTk.PhotoImage(jeuxEssais_text_pil.resize(jeuxEssais_textR))
fonctionC.create_image(w * 0.75, h * 0.3727, image=jeuxEssais_text_img)
procedureC.create_image(w * 0.75, h * 0.3727, image=jeuxEssais_text_img)
programmeC.create_image(w * 0.75, h * 0.3727, image=jeuxEssais_text_img)

jeuxEssaisFonctionEntry = Text(fonctionC)
jeuxEssaisFonctionEntry.place(x=(w * 0.5417), y=h * 0.4167, width=int(w * 0.4167), height=int(h * 0.0926))
jeuxEssaisProcedureEntry = Text(procedureC)
jeuxEssaisProcedureEntry.place(x=(w * 0.5417), y=h * 0.4167, width=int(w * 0.4167), height=int(h * 0.0926))
jeuxEssaisProgrammeEntry = Text(programmeC)
jeuxEssaisProgrammeEntry.place(x=(w * 0.5417), y=h * 0.4167, width=int(w * 0.4167), height=int(h * 0.0926))

principe_text_pil = Image.open('images/text_principe.png')
principe_textR = (int(h * POURCENT_FCT_T * 3.177), int(h * POURCENT_FCT_T))
principe_text_img = ImageTk.PhotoImage(principe_text_pil.resize(principe_textR))
fonctionC.create_image(w * 0.75, h * 0.5579, image=principe_text_img)
procedureC.create_image(w * 0.75, h * 0.5579, image=principe_text_img)
programmeC.create_image(w * 0.75, h * 0.5579, image=principe_text_img)

principeFonctionEntry = Text(fonctionC)
principeFonctionEntry.place(x=(w * 0.5417), y=h * 0.6019, width=int(w * 0.4167), height=int(h * 0.0926))
principeProcedureEntry = Text(procedureC)
principeProcedureEntry.place(x=(w * 0.5417), y=h * 0.6019, width=int(w * 0.4167), height=int(h * 0.0926))
principeProgrammeEntry = Text(programmeC)
principeProgrammeEntry.place(x=(w * 0.5417), y=h * 0.6019, width=int(w * 0.4167), height=int(h * 0.0926))

valJE_text_pil = Image.open('images/text_valJE.png')
valJE_textR = (int(h * POURCENT_FCT_T * 10.294), int(h * POURCENT_FCT_T))
valJE_text_img = ImageTk.PhotoImage(valJE_text_pil.resize(valJE_textR))
fonctionC.create_image(w * 0.75, h * 0.743, image=valJE_text_img)
procedureC.create_image(w * 0.75, h * 0.743, image=valJE_text_img)
programmeC.create_image(w * 0.75, h * 0.743, image=valJE_text_img)

valJEFonctionEntry = Text(fonctionC)
valJEFonctionEntry.place(x=(w * 0.5417), y=h * 0.787, width=int(w * 0.4167), height=int(h * 0.0926))
valJEProcedureEntry = Text(procedureC)
valJEProcedureEntry.place(x=(w * 0.5417), y=h * 0.787, width=int(w * 0.4167), height=int(h * 0.0926))
valJEProgrammeEntry = Text(programmeC)
valJEProgrammeEntry.place(x=(w * 0.5417), y=h * 0.787, width=int(w * 0.4167), height=int(h * 0.0926))

boutonGen_pil = Image.open('images/boutonGen.png')
boutonGenR = (int(h * POURCENT_FCT_T * 6.7765), int(h * POURCENT_FCT_T))
boutonGen_img = ImageTk.PhotoImage(boutonGen_pil.resize(boutonGenR))
fonctionC.create_image(w * 0.75, h * 0.9421, image=boutonGen_img)
procedureC.create_image(w * 0.75, h * 0.9421, image=boutonGen_img)
programmeC.create_image(w * 0.75, h * 0.9421, image=boutonGen_img)

root.bind('<Button-1>', oeilDeMoscou)

# Affichage du main
main.place(x=0, y=0, width=w, height=h)

# Lancement de l'application
root.mainloop()

"""Je m'appelle C.A.R.O. et je suis un Créateur d'Algorithmes Relativement Original."""
