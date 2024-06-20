import requests
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Relógio")

# Lista de fusos horários disponíveis na América sem o prefixo "America/"
# Nomes formatados para exibição (sem underscores)
timezones = {
    "São Paulo": "Sao_Paulo", 
    "New York": "New_York", 
    "Los Angeles": "Los_Angeles", 
    "Buenos Aires": "Buenos_Aires", 
    "Mexico City": "Mexico_City", 
    "Lima": "Lima"
}

# Função para obter o horário atual de uma zona específica
def get_time(city):
    timezone = f"America/{timezones[city]}"  # Mapeia para o nome esperado pela API
    url = f"http://worldtimeapi.org/api/timezone/{timezone}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        datetime = data['datetime']
        time = datetime[11:19]  # Extraindo apenas a parte de horas, minutos e segundos
        return time
    else:
        return "Erro"

# Definindo uma função para atualizar o relógio
def watch():
    city = timezone_var.get()
    horario = get_time(city)
    label.config(text=horario)
    label.after(1000, watch)

# Configurando o estilo da janela e da fonte
root.geometry("800x400")  # Tamanho da janela
root.configure(bg="#1E1E1E")  # Cor de fundo da janela (preto escuro)

# Criando uma label com estilo personalizado
label = Label(root, font=("DS-Digital", 100), background="#1E1E1E", foreground="#00FF04")  # Texto branco sobre fundo preto
label.pack(anchor="center", expand=True)

# Adicionando um dropdown para selecionar o fuso horário
timezone_var = StringVar(value=list(timezones.keys())[0])  # Fuso horário padrão

# Estilizando o Combobox
style = Style()
style.configure("TCombobox",
                fieldbackground="#2B2B2B",  # Fundo do campo de entrada do Combobox (cinza escuro)
                background="#2B2B2B",       # Fundo do menu suspenso do Combobox (cinza escuro)
                foreground="#111",       # Texto branco
                font=("Helvetica", 20),
                arrowcolor="#FFFFFF")       # Cor da seta (branca)

dropdown = Combobox(root, textvariable=timezone_var, values=list(timezones.keys()), font=("Helvetica", 20), style="TCombobox")
dropdown.pack(pady=20)

# Iniciando a função watch
watch()

# Mantendo a janela aberta
root.mainloop()
