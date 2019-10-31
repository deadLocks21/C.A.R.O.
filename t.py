main_pil = Image.open('images/main.png')
main_resolution = (w, h)
main_img = ImageTk.PhotoImage(main_pil.resize(main_resolution))
main.create_image(w / 2, h / 2, image=main_img)