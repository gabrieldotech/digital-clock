import requests
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Relógio")

# lista de fusos horários disponíveis
timezones = {
    "São Paulo": "Sao_Paulo", 
    "New York": "New_York", 
    "Los Angeles": "Los_Angeles", 
    "Buenos Aires": "Buenos_Aires", 
    "Mexico City": "Mexico_City", 
    "Lima": "Lima"
}

# função para o horário atual de uma zona
def get_time(city):
    timezone = f"America/{timezones[city]}"  
    url = f"http://worldtimeapi.org/api/timezone/{timezone}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        datetime = data['datetime']
        time = datetime[11:19]  #
        return time
    else:
        return "Erro"

# atualizar o relógio
def watch():
    city = timezone_var.get()
    horario = get_time(city)
    label.config(text=horario)
    label.after(1000, watch)

# estilo da janela e da fonte
root.geometry("800x400")  
root.configure(bg="#1E1E1E")  

# estilo da label
label = Label(root, font=("DS-Digital", 100), background="#1E1E1E", foreground="#00FF04") 
label.pack(anchor="center", expand=True)

# dropdown para selecionar o fuso
timezone_var = StringVar(value=list(timezones.keys())[0])  

# estilo combobox
style = Style()
style.configure("TCombobox",
fieldbackground="#2B2B2B", 
background="#2B2B2B",      
foreground="#111",       
font=("Helvetica", 20),
arrowcolor="#FFFFFF")      

dropdown = Combobox(root, textvariable=timezone_var, values=list(timezones.keys()), font=("Helvetica", 20), style="TCombobox")
dropdown.pack(pady=20)

watch()

root.mainloop()
