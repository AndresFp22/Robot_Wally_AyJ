import tkinter as tk
from tkinter import ttk


prior_value = 0

def move_arm(value):
    
    print("Palanca:", value)

def move_forward():
    
    print("Mover hacia adelante")

def stop():
    
    print("Detener")

def agarrar():
    
    print("Garra cerrada")

def soltar():
    
    print("Garra Abierta")

def move_backward():
    
    print("Mover hacia atrás")

def turn_left():
    
    print("Girar a la izquierda")

def turn_right():
    
    print("Girar a la derecha")

def emergency_stop():
    print("El robot realizó una parada de emergencia")

def objectos_reciclables():
    print("Ha seleccionado recoger solo objetos reciclables")

def objetos_no_reciclables():
    print("Ha seleccionado recoger solo objetos no reciclables")

def start_robot():
    btn_forward.config(state=tk.NORMAL)
    btn_stop.config(state=tk.NORMAL)
    btn_backward.config(state=tk.NORMAL)
    btn_left.config(state=tk.NORMAL)
    btn_right.config(state=tk.NORMAL)
    btn_no_reciclables.config(state=tk.NORMAL)
    btn_reciclables.config(state=tk.NORMAL)
    btn_agarrar.config(state=tk.NORMAL)
    btn_soltar.config(state=tk.NORMAL)

def stop_robot():
    btn_forward.config(state=tk.DISABLED)
    btn_stop.config(state=tk.DISABLED)
    btn_backward.config(state=tk.DISABLED)
    btn_left.config(state=tk.DISABLED)
    btn_right.config(state=tk.DISABLED)
    btn_no_reciclables.config(state=tk.DISABLED)
    btn_reciclables.config(state=tk.DISABLED)
    btn_agarrar.config(state=tk.DISABLED)
    btn_soltar.config(state=tk.DISABLED)

# Crear la ventana principal
window = tk.Tk()
window.title("Robot Wally")
window.geometry("1000x1000")  # Tamaño establecido para la ventana

# Configurar la expansión vertical de los botones
window.grid_rowconfigure(0, weight=1)

# Crear un contenedor para los botones
button_frame = tk.Frame(window)
button_frame.pack(expand=True, padx=10, pady=10)

# Crear el botón de inicio y apagado
btn_start = tk.Button(window, text="Inicio", relief="raised", bg="green", fg="yellow", command=start_robot)
btn_start.pack(side=tk.LEFT, padx=10, pady=10)

btn_stopRobot = tk.Button(window, text="Apagado", relief="raised", bg="grey", fg="yellow", command=stop_robot)
btn_stopRobot.pack(side=tk.LEFT, padx=10, pady=10)

# Crear el notebook (pestañas)
notebook = ttk.Notebook(window)
notebook.pack(anchor=tk.NE, padx=10, pady=10)

# Crear la pestaña "Categoría"
tab_categoria = ttk.Frame(notebook)
notebook.add(tab_categoria, text="Categoría")

# Crear las opciones dentro de la pestaña "Categoría"
btn_reciclables = tk.Button(tab_categoria, text="Objetos reciclables", bg="yellow", fg="black", command=objectos_reciclables)
btn_reciclables.pack(padx=10, pady=10)

btn_no_reciclables = tk.Button(tab_categoria, text="Objetos no reciclables", bg="black", fg="white", command=objetos_no_reciclables)
btn_no_reciclables.pack(padx=10, pady=10)

# Crear los botones para controlar el robot
btn_forward = tk.Button(button_frame, text="Adelante", command=move_forward, state=tk.DISABLED)
btn_forward.grid(row=0, column=1, padx=10, pady=10)

btn_stop = tk.Button(button_frame, text="Stop", relief="raised", command=stop, state=tk.DISABLED)
btn_stop.grid(row=1, column=1, padx=10, pady=10)

btn_backward = tk.Button(button_frame, text="Atrás", relief="raised", command=move_backward, state=tk.DISABLED)
btn_backward.grid(row=2, column=1, padx=10, pady=10)

btn_left = tk.Button(button_frame, text="Izquierda", relief="raised", command=turn_left, state=tk.DISABLED)
btn_left.grid(row=1, column=0, padx=10, pady=10)

btn_right = tk.Button(button_frame, text="Derecha", relief="raised", command=turn_right, state=tk.DISABLED)
btn_right.grid(row=1, column=2, padx=10, pady=10)

btn_emergencyStop = tk.Button(window, text="EMERGENCY STOP", relief="raised", bg="red", fg="white", command=emergency_stop)
btn_emergencyStop.pack(pady=10)

# Crear los requerimientos al lado del botón "Derecha"
requirements_frame = tk.Frame(button_frame)
requirements_frame.grid(row=1, column=3, padx=10, pady=10)


# Crear la palanca
label_arm = tk.Label(requirements_frame, text="BRAZO")
label_arm.pack(pady=10)

scale_arm = tk.Scale(requirements_frame, from_=0, to=100, orient=tk.VERTICAL, command=move_arm)
scale_arm.pack(pady=10)

# Crear los botones Agarrar y Soltar
btn_agarrar = tk.Button(requirements_frame, text="Agarrar", relief="raised", command=lambda: print("Agarrar"))
btn_agarrar.pack(side=tk.LEFT, padx=5, pady=5)

btn_soltar = tk.Button(requirements_frame, text="Soltar", relief="raised", command=lambda: print("Soltar"))
btn_soltar.pack(side=tk.LEFT, padx=5, pady=5)

def check_tipping():
    global prior_value
    
    current_value = scale_arm.get()
    
    if prior_value > 90 and current_value <= 90:
        print("Peligro: El robot se puede volcar")
    elif prior_value <= 90 and current_value > 90:
        print("Peligro: El robot se puede volcar")
    
    prior_value = current_value
    
    window.after(100, check_tipping)

# Iniciar la comprobación de volcado
check_tipping()

# Ejecutar la ventana principal
window.mainloop()
