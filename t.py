fonctionS_pil = Image.open('images/fonctionSel.png')
fonctionSR = (int(h * POURCENT_BT_CHOIX * 4), int(h * POURCENT_BT_CHOIX))
fonctionS_img = ImageTk.PhotoImage(fonctionS_pil.resize(fonctionSR))
fonctionC.create_image(w/4, h*0.05, image=fonctionS_img)