varEtConst_text_pil = Image.open('images/text_varEtConst.png')
varEtConst_textR = (int(h*POURCENT_FCT_T*6.823), int(h*POURCENT_FCT_T))
varEtConst_text_img = ImageTk.PhotoImage(varEtConst_text_pil.resize(varEtConst_textR))
fonctionC.create_image(w*0.177, h*0.6644, image=varEtConst_text_img)

nomVarEtConstEntry = Text(fonctionC)
nomVarEtConstEntry.place(x=(w*0.3333), y=h*0.6389, width=int(w*0.1302), height=int(h*0.0601))
