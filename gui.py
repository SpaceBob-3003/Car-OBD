#HOAREAU Alann


# The graphic interface in this file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
import can
import obd
    
#Fonction pour quitter la fenetre

def quitter():
	print("Fermeture du programme...")
	if 'bus' in globals():  # Vérifier si le bus a été initialisé
		window.destroy()
		bus.shutdown()

#Fonction pour mettre a jour les informations

def mise_a_jour(bus):
	
	values = {
	"Vitesse": obd.vitesse(bus),
	"Load": obd.pourcent_load(bus),
	"RPM": obd.rpm(bus),
	"Papillon": obd.position_papillon(bus),
	"Refroidissement": obd.temp_refroidissement(bus),
	"Air": obd.temp_air(bus)
	}
	
	for key in values:
		canvas.itemconfig(text_ids[key], text=values[key])
	
	window.after(500, lambda: mise_a_jour(bus))

#creation des canvas

window = Tk()

window.geometry("800x480")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    73.0,
    fill="#363636",
    outline="")

canvas.create_rectangle(
    0.0,
    73.0,
    800.0,
    480.0,
    fill="#1A1A1A",
    outline="")

canvas.create_text(
    310.0,
    0.0,
    anchor="nw",
    text="car'OBD",
    fill="#FFFFFF",
    font=("Chenla", 40 * -1)
)

button_image = PhotoImage(file="button_1.png")

button_1 = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=quitter,
    relief="flat"
)
button_1.place(
    x=745.0,
    y=7.0,
    width=42.0,
    height=51.0
)

canvas.create_rectangle(
    53.0,
    132.0,
    341.0,
    212.0,
    fill="#363636",
    outline="")

canvas.create_text(
    278.0,
    159.0,
    anchor="nw",
    text="km/h",
    fill="#FFFFFF",
    font=("Chenla", 16 * -1)
)

canvas.create_text(
    65.0,
    132.0,
    anchor="nw",
    text="Vitesse",
    fill="#FFFFFF",
    font=("Chenla", 14 * -1)
)

canvas.create_rectangle(
    457.0,
    132.0,
    745.0,
    212.0,
    fill="#363636",
    outline="")

canvas.create_text(
    683.0,
    159.0,
    anchor="nw",
    text="t/min",
    fill="#FFFFFF",
    font=("Chenla", 16 * -1)
)

canvas.create_text(
    469.0,
    132.0,
    anchor="nw",
    text="RPM",
    fill="#FFFFFF",
    font=("Chenla", 14 * -1)
)

canvas.create_rectangle(
    53.0,
    240.0,
    341.0,
    320.0,
    fill="#363636",
    outline="")

canvas.create_text(
    278.0,
    267.0,
    anchor="nw",
    text="%",
    fill="#FFFFFF",
    font=("Chenla", 16 * -1)
)

canvas.create_text(
    65.0,
    240.0,
    anchor="nw",
    text="Load",
    fill="#FFFFFF",
    font=("Chenla", 14 * -1)
)

canvas.create_rectangle(
    457.0,
    240.0,
    745.0,
    320.0,
    fill="#363636",
    outline="")

canvas.create_text(
    683.0,
    267.0,
    anchor="nw",
    text="°C",
    fill="#FFFFFF",
    font=("Chenla", 16 * -1)
)

canvas.create_text(
    469.0,
    240.0,
    anchor="nw",
    text="Temp. liquide de refroidissement",
    fill="#FFFFFF",
    font=("Chenla", 14 * -1)
)

canvas.create_rectangle(
    53.0,
    348.0,
    341.0,
    428.0,
    fill="#363636",
    outline="")

canvas.create_text(
    278.0,
    375.0,
    anchor="nw",
    text="%",
    fill="#FFFFFF",
    font=("Chenla", 16 * -1)
)

canvas.create_text(
    65.0,
    348.0,
    anchor="nw",
    text="Position du Papillon",
    fill="#FFFFFF",
    font=("Chenla", 14 * -1)
)

canvas.create_rectangle(
    457.0,
    348.0,
    745.0,
    428.0,
    fill="#363636",
    outline="")

canvas.create_text(
    683.0,
    375.0,
    anchor="nw",
    text="°C",
    fill="#FFFFFF",
    font=("Chenla", 16 * -1)
)

canvas.create_text(
    469.0,
    348.0,
    anchor="nw",
    text="Temp. Air",
    fill="#FFFFFF",
    font=("Chenla", 14 * -1)
)

# Liste contenant tous les textes du canvas a modifier

text_ids = {
	"Vitesse": canvas.create_text(
		190.0,
		159.0,
		anchor="nw",
		text="0",
		fill="#FFFFFF",
		font=("Chenla", 16 * -1)
	),

	"Load": canvas.create_text(
		190.0,
		267.0,
		anchor="nw",
		text="0",
		fill="#FFFFFF",
		font=("Chenla", 16 * -1)
	),

	"RPM": canvas.create_text(
		601.0,
		159.0,
		anchor="nw",
		text="0",
		fill="#FFFFFF",
		font=("Chenla", 16 * -1)
	),

	"Papillon": canvas.create_text(
		190.0,
		375.0,
		anchor="nw",
		text="0",
		fill="#FFFFFF",
		font=("Chenla", 16 * -1)
	),

	"Refroidissement": canvas.create_text(
		601.0,
		267.0,
		anchor="nw",
		text="0",
		fill="#FFFFFF",
		font=("Chenla", 16 * -1)
	),

	"Air": canvas.create_text(
		601.0,
		375.0,
		anchor="nw",
		text="0",
		fill="#FFFFFF",
		font=("Chenla", 16 * -1)
	)
}

#Chargement du Logo

image = Image.open("logo.jpeg")
image = image.resize((60, 60))  # Ajuster à la taille du logo
photo = ImageTk.PhotoImage(image)

canvas.create_image(6, 7, anchor="nw", image=photo)

window.resizable(False, False)




#Programme Principal

obd.setup_can_interface()

bus = can.interface.Bus(channel='can0', bustype='socketcan')

mise_a_jour(bus)

window.mainloop()
