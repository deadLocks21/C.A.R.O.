role_text_pil = Image.open('images/text_role_text.png')
role_textR = (int(h*POURCENT_FCT_T*3.41), int(h*POURCENT_FCT_T))
role_text_img = ImageTk.PhotoImage(role_text_pil.resize(role_textR))
role_textC.create_image(w*0.1016, h*0.191, image=role_text_img)