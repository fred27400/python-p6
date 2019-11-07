#coding:utf-8
import tkinter

def show_about():
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    lb = tkinter.Label(about_window, text="Ce script automatise l'administration de windows!!! \n\nCréateur : Mr Frédéric Seguin \n\nProjet 6 AIC Openclassrooms ")
    lb.pack()

# Création de la fenêtre + paramétrage
app = tkinter.Tk()
app.geometry("340x50")
app.title("Script Automatisation")

# Widgets...
mainmenu = tkinter.Menu(app)

# Premier menu
script_utilisateurs = tkinter.Menu(mainmenu, tearoff=0)		
script_utilisateurs.add_command(label="Option1")
script_utilisateurs.add_command(label="Option2")
script_utilisateurs.add_command(label="Option3")
script_utilisateurs.add_command(label="Option4")
script_utilisateurs.add_command(label="Option5")

# Deuxieme menu
gpo = tkinter.Menu(mainmenu, tearoff=0)
gpo.add_command(label="gpo1")
gpo.add_command(label="gpo2")
gpo.add_command(label="gpo3")
gpo.add_command(label="gpo4")
gpo.add_command(label="gpo5")
gpo.add_command(label="gpo6")

# Troisième menu
divers = tkinter.Menu(mainmenu, tearoff=0)
divers.add_command(label="divers1")
divers.add_command(label="divers2")

# quatrième menu
quitter = tkinter.Menu(mainmenu, tearoff=0)
quitter.add_command(label="quitter", command=app.quit)

# Cinquième menu
A_propos = tkinter.Menu(mainmenu, tearoff=0)
A_propos.add_command(label="A propos", command=show_about)

mainmenu.add_cascade(label="script_utilisateurs", menu=script_utilisateurs)
mainmenu.add_cascade(label="gpo", menu=gpo)
mainmenu.add_cascade(label="divers", menu=divers)
mainmenu.add_cascade(label="quitter", menu=quitter)
mainmenu.add_cascade(label="A propos", menu=A_propos)

# Boucle principale
app.config(menu=mainmenu)
app.mainloop()

  
