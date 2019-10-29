barreS_pil = Image.open('images/barreS.png')
barreSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
barreS_img = ImageTk.PhotoImage(barreS_pil.resize(barreSR))
programmeC.create_image((3*w)/4, h*0.05, image=barreS_img)