import customtkinter as ctk
import requests
from PIL import Image, ImageTk


janela = ctk.CTk()
janela.geometry("400x600")
janela.title("SERASA v2 BLOX FRUIT")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

bg_image = ctk.CTkImage(Image.open("dias.png"), size=(400, 600))
bg_label = ctk.CTkLabel(janela, image=bg_image, text="")
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# - Função
def consultar():
    tipo = select.get()
    documento = "".join(filter(str.isdigit, entrada_dados.get())) # Garante só números
    
    if not documento:
        respostas.configure(text="Por favor, digite um número.")
        return

    respostas.configure(text="Conectando ao servidor...")
    janela.update_idletasks() # Força o texto a aparecer antes de travar na requisição

    try:
        if tipo == "CPF":
            # CPFHub usa x-api-key e a URL é /cpf/{documento}
            token = "89f2fcbe7ecadae218b8e3bb6928f9315c6e9b7165a195217c4846417e27a31b"
            url = f"https://api.cpfhub.io/cpf/{documento}"
            headers = {"x-api-key": token} # Nome correto do header para CPFHub
            response = requests.get(url, headers=headers, timeout=15)
        
        else: # CNPJxxx
            url = f"https://api.opencnpj.org/{documento}?dataset=receita"
            response = requests.get(url, timeout=15)

        # Verificação do Status
        if response.status_code == 200:
            data = response.json()
            if tipo == "CPF":
                    # Se o seu dicionário principal se chama 'resposta'
                     respostas.configure(text=f"Nome: {data['data'].get('name')}\nNascimento: {data['data'].get('birthDate')}")

            else:
                respostas.configure(text=f"Empresa: {data.get('razao_social')}\nStatus: {data.get('situacao_cadastral')}\n Inicio Atividade: {data.get('data_inicio_atividade')}")
        
        elif response.status_code == 403:
            respostas.configure(text="Erro 403: Token inválido ou bloqueado.")
        elif response.status_code == 404:
            respostas.configure(text="Documento não encontrado na base.")
        else:
            respostas.configure(text=f"Servidor retornou erro {response.status_code}")

    except requests.exceptions.SSLError:
        respostas.configure(text="Erro de SSL: Tente desativar seu antivírus/VPN.")
    except requests.exceptions.ConnectionError:
        respostas.configure(text="Falha na conexão: Verifique seu Wi-Fi ou Firewall.")
    except Exception as e:
        respostas.configure(text=f"Erro crítico: {type(e).__name__}")

# Elementos graficos
titulo = ctk.CTkLabel(janela, text="Consulta CPF/CNPJ", font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=20)

select = ctk.CTkComboBox(janela, values=["CPF", "CNPJ"])
select.pack(pady=10)

# Mudei o nome de 'dados' para 'entrada_dados' para não confundir
entrada_dados = ctk.CTkEntry(janela, placeholder_text="Digite o número do documento", width=250)
entrada_dados.pack(pady=20)

botao = ctk.CTkButton(janela, text="Consultar", corner_radius=10, command=consultar)
botao.pack(pady=20)

# Este label servirá para mostrar o resultado
respostas = ctk.CTkLabel(janela, text="", font=ctk.CTkFont(size=14), justify="left")
respostas.pack(pady=20)

janela.mainloop()
