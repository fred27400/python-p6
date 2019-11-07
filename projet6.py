#coding:utf-8
import tkinter

# Création de la fenêtre + paramétrage
app = tkinter.tk()
app.geometry("640x480")
app.tittle("Création de Menu")

# Widgets...
mainmenu = tkinter.Menu(app)

# Premier menu
script_utilisateurs = tkinter.Menu(mainmenu)		
script_utilisateurs.add_command(label="Option1")
script_utilisateurs.add_command(label="Option2")
script_utilisateurs.add_command(label="Option3")
script_utilisateurs.add_command(label="Option4")
script_utilisateurs.add_command(label="Option5")

# Deuxieme menu
gpo = tkinter.Menu(mainmenu)
gpo.add_command(label="gpo1")
gpo.add_command(label="gpo2")
gpo.add_command(label="gpo3")
gpo.add_command(label="gpo4")
gpo.add_command(label="gpo5")
gpo.add_command(label="gpo6")

# Troisiéme menu
divers = tkinter.Menu(mainmenu)
divers.add_command(label="divers1")
divers.add_command(label="divers1")

# Menu en cascade
mainmenu.add_cascade(label="script_utilisateurs", menu=script_utilisateurs)
mainmenu.add_cascade(label="gpo", menu=gpo)
mainmenu.add_cascade(label="divers", menu=divers)


# Boucle principale
app.config(menu=mainmenu)
app.mainloop()

  
