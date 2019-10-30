boutonGen_pil = Image.open('images/boutonGen.png')
boutonGenR = (int(h * POURCENT_BARRE * 0.03), int(h * POURCENT_BARRE))
boutonGen_img = ImageTk.PhotoImage(boutonGen_pil.resize(boutonGenR))
fonctionC.create_image(w/2, h/2+h*0.05, image=boutonGen_img)