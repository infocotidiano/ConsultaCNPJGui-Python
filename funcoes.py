from tkinter import *
import json
#Validar se json 
def validar_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.decoder.JSONDecodeError:
        return False

def dlg_mensagem(mensagem):
    # Cria uma nova janela
    janela_erro = Tk()
    janela_erro.title("Atenção !")
    
    # Adiciona uma label com a mensagem de erro
    label_mensagem = Label(janela_erro, text=mensagem)
    label_mensagem.pack(padx=200, pady=50)

    # Função para fechar a janela de erro
    def fechar_janela():
        janela_erro.destroy()

    # Adiciona um botão "OK" para fechar a janela
    botao_ok = Button(janela_erro, text="OK", command=fechar_janela)
    botao_ok.pack(pady=10)

    # Define o foco inicial no botão "OK" para facilitar o uso com o teclado
    botao_ok.focus()

    # Mantém a janela aberta
    janela_erro.mainloop()
