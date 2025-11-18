import tkinter as tk
from tkinter import messagebox, ttk
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "tpiprog1@gmail.com"
EMAIL_PASS = "ikie czyo euld vuit"

def enviar_recordatorio(email_destino, nombre, fecha_turno):
    asunto = "Recordatorio de turno"
    mensaje = f"""
Hola {nombre},

Este es un recordatorio de tu turno programado.

Fecha del turno: {fecha_turno.strftime('%d/%m/%Y')}

Saludos.
"""

    msg = MIMEText(mensaje)
    msg["Subject"] = asunto
    msg["From"] = EMAIL_USER
    msg["To"] = email_destino

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, email_destino, msg.as_string())
        server.quit()
        return True, None
    except Exception as e:
        return False, str(e)

def agregar_turno():
    nombre = entry_nombre.get().strip()
    email = entry_email.get().strip()
    fecha = entry_fecha.get().strip()

    if not nombre or not email or not fecha:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    try:
        fecha_turno = datetime.strptime(fecha, "%d/%m/%Y")
    except:
        messagebox.showerror("Error", "Formato de fecha incorrecto. Use dd/mm/aaaa.")
        return

    with open("turnos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre};{email};{fecha}\n")

    messagebox.showinfo("Éxito", "Turno agregado correctamente.")

    entry_nombre.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)

    mostrar_turnos()

def mostrar_turnos():
    tree.delete(*tree.get_children())

    try:
        with open("turnos.txt", "r", encoding="utf-8") as archivo:
            turnos = archivo.readlines()
    except FileNotFoundError:
        return

    for t in turnos:
        nombre, email, fecha = t.strip().split(";")
        tree.insert("", tk.END, values=(nombre, email, fecha))

def eliminar_turno():
    seleccionado = tree.selection()

    if not seleccionado:
        messagebox.showerror("Error", "Seleccione un turno.")
        return

    item = seleccionado[0]
    nombre_sel, email_sel, fecha_sel = tree.item(item, "values")

    try:
        with open("turnos.txt", "r", encoding="utf-8") as archivo:
            turnos = archivo.readlines()
    except FileNotFoundError:
        return

    nuevos = []
    for t in turnos:
        nombre, email, fecha = t.strip().split(";")
        if nombre != nombre_sel or email != email_sel or fecha != fecha_sel:
            nuevos.append(t)

    with open("turnos.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(nuevos)

    messagebox.showinfo("Éxito", "Turno eliminado")
    mostrar_turnos()

def borrar_todos():
    confirm = messagebox.askyesno("Confirmar", "¿Seguro que quiere eliminar TODOS los turnos?")
    if confirm:
        with open("turnos.txt", "w", encoding="utf-8") as archivo:
            archivo.write("")
        mostrar_turnos()
        messagebox.showinfo("Éxito", "Se eliminaron todos los turnos.")

def enviar_recordatorio_seleccionado():
    seleccionado = tree.selection()

    if not seleccionado:
        messagebox.showerror("Error", "Seleccione un turno.")
        return

    item = seleccionado[0]
    nombre, email, fecha = tree.item(item, "values")

    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    except:
        messagebox.showerror("Error", "La fecha del turno es inválida.")
        return

    ok, err = enviar_recordatorio(email, nombre, fecha_dt)

    if ok:
        messagebox.showinfo("Éxito", f"Recordatorio enviado a {email}.")
    else:
        messagebox.showerror("Error", f"No se pudo enviar el correo:\n{err}")

def enviar_pendientes():
    hoy = datetime.now().date()

    try:
        with open("turnos.txt", "r", encoding="utf-8") as archivo:
            turnos = archivo.readlines()
    except FileNotFoundError:
        messagebox.showinfo("Info", "No hay turnos cargados.")
        return

    enviados = 0

    for t in turnos:
        nombre, email, fecha = t.strip().split(";")
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y").date()

        if fecha_dt - hoy == timedelta(days=1):
            enviar_recordatorio(email, nombre, datetime.strptime(fecha, "%d/%m/%Y"))
            enviados += 1

    if enviados > 0:
        messagebox.showinfo("Éxito", f"Se enviaron {enviados} recordatorios.")
    else:
        messagebox.showinfo("Info", "No hay recordatorios pendientes para enviar.")

ventana = tk.Tk()
ventana.title("Turnero Interactivo")
ventana.geometry("820x600")
ventana.resizable(False, False)

frame_carga = tk.LabelFrame(ventana, text="Registrar Turno", padx=10, pady=10)
frame_carga.pack(fill="x", padx=10, pady=10)

tk.Label(frame_carga, text="Nombre:").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(frame_carga, width=40)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_carga, text="Email:").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame_carga, width=40)
entry_email.grid(row=1, column=1)

tk.Label(frame_carga, text="Fecha (dd/mm/aaaa):").grid(row=2, column=0, sticky="w")
entry_fecha = tk.Entry(frame_carga, width=40)
entry_fecha.grid(row=2, column=1)

btn_agregar = tk.Button(frame_carga, text="Agregar turno", width=20, command=agregar_turno)
btn_agregar.grid(row=3, columnspan=2, pady=10)

frame_lista = tk.LabelFrame(ventana, text="Turnos Registrados", padx=10, pady=10)
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

columnas = ("Nombre", "Email", "Fecha")
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")
for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=250)
tree.pack(fill="both", expand=True)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_mostrar = tk.Button(frame_botones, text="Mostrar turnos", width=20, command=mostrar_turnos)
btn_mostrar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar seleccionado", width=20, command=eliminar_turno)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_borrar_todos = tk.Button(frame_botones, text="Borrar TODOS", width=20, command=borrar_todos)
btn_borrar_todos.grid(row=0, column=2, padx=5)

btn_enviar_seleccionado = tk.Button(frame_botones, text="Enviar recordatorio seleccionado", width=26, command=enviar_recordatorio_seleccionado)
btn_enviar_seleccionado.grid(row=1, column=0, columnspan=2, pady=6)

btn_pendientes = tk.Button(frame_botones, text="Enviar recordatorios pendientes", width=26, command=enviar_pendientes)
btn_pendientes.grid(row=1, column=2, pady=6)

ventana.mainloop()