# program       ExemploLibCNPJ.py
# author        Daniel de Morais InfoCotidiano
# installation  Exemplo de uso da biblioteca do Projeto ACBr utilizando Python
#               Tela Gráfica de consulta.                
# date-written  19/07/2024

from tkinter import *
import customtkinter as ctk
from libACBr import configuraWS
from libACBr import consultaCNPJ
from datetime import datetime
from funcoes import dlg_mensagem



#Crando a janela principal
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
self = ctk.CTk()
self.title("Consulta CNPJ")   
self.geometry('700x500')

#funcao para tratar a data da esposta
def formataData(LDATA):   
    return datetime.strptime(LDATA, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y")

#funcao para limpar campos da tela
def limpaCampos():
        edt_razao.delete(0,'end')
        edt_situacao.delete(0,'end')
        edt_fantasia.delete(0,'end')
        edt_abertura.delete(0,'end')
        edt_endereco.delete(0,'end')
        edt_complemento.delete(0,'end')
        edt_bairro.delete(0,'end')
        edt_cidade.delete(0,'end')
        edt_estado.delete(0,'end')
        edt_cep.delete(0,'end')
        edt_CNAE1.delete("1.0",'end')
        
#funcao para limpar campos da tela
def tela_resposta(LCNPJ):
    LJson = consultaCNPJ(LCNPJ)
    if not LJson:
        dlg_mensagem('consulta invalida')
    else:    
        consulta = LJson.get('Consulta', {})
        edt_razao.insert(0,consulta.get('RazaoSocial', ''))
        edt_situacao.insert(0,consulta.get('Situacao', ''))
        edt_fantasia.insert(0,consulta.get('Fantasia', ''))
        edt_abertura.insert(0,formataData(consulta.get('Abertura', '')))
        edt_endereco.insert(0,consulta.get('Endereco', ''))
        edt_complemento.insert(0,consulta.get('Complemento', ''))
        edt_bairro.insert(0,consulta.get('Bairro', ''))
        edt_cidade.insert(0,consulta.get('Cidade', ''))
        edt_estado.insert(0,consulta.get('UF', ''))
        edt_cep.insert(0,consulta.get('CEP', ''))
        edt_CNAE1.insert("1.0",consulta.get('CNAE1', '')+'\n'+consulta.get('CNAE2', ''))
        
#quando clicar no botao consultar
def consultar():
    limpaCampos() #vamos limpar os campos da tela
    configuraWS(sl_provedor.get()) # vamos configurar o provedor de consulta
    if edt_cnpj.get():
        tela_resposta(edt_cnpj.get())
    else:
        dlg_mensagem('CNPJ Obrigatorio')    
             
lb_sistema = ctk.CTkLabel(self,text='ACBrLibCNPJ com Python',font=('Arial', 20, 'bold') ).place(x=10,y=15)

sl_provedor = ctk.CTkOptionMenu(self,values=['Nenhum','BrasilAPI','ReceitaWS','CNPJWS'],)
sl_provedor.pack(pady=0)
sl_provedor.place(x=50,y=80)
lb_cnpj = ctk.CTkLabel(self,text='CNPJ:').place(x=200,y=50)
edt_cnpj = ctk.CTkEntry(self,width=200,height=30,  placeholder_text='Digite o CNPJ')
edt_cnpj.pack(pady=0)
edt_cnpj.place(x=200,y=80)
lb_autor = ctk.CTkLabel(self,text='Criado por Daniel de Morais - InfoCotidiano').place(x=10,y=470)
lb_provedor = ctk.CTkLabel(self,text='Provedores').place(x=50,y=50)
btn_consulta = ctk.CTkButton(self,text="Consulta",command=consultar).place(x=450,y=80)
frmResposta = ctk.CTkFrame(self,width=670,height=350)
frmResposta.place(x=10,y=120)
lb_razao  = ctk.CTkLabel(frmResposta,text='Razão Social',bg_color='transparent').place(x=15,y=5)
edt_razao = ctk.CTkEntry(frmResposta,width=450,height=25)
edt_razao.pack(pady=0)
edt_razao.place(x=15,y=28)

lb_situacao = ctk.CTkLabel(frmResposta,text='Situação',bg_color='transparent').place(x=480,y=5)
edt_situacao = ctk.CTkEntry(frmResposta,width=120,height=25)
edt_situacao.pack(pady=0)
edt_situacao.place(x=480,y=28)

lb_fantasia  = ctk.CTkLabel(frmResposta,text='Fantasia',bg_color='transparent').place(x=15,y=55)
edt_fantasia = ctk.CTkEntry(frmResposta,width=450,height=25)
edt_fantasia.pack(pady=0)
edt_fantasia.place(x=15,y=75)


lb_abertura = ctk.CTkLabel(frmResposta,text='Abertura',bg_color='transparent').place(x=480,y=55)
edt_abertura = ctk.CTkEntry(frmResposta,width=120,height=25)
edt_abertura.pack(pady=0)
edt_abertura.place(x=480,y=75)

lb_endereco  = ctk.CTkLabel(frmResposta,text='Endereco',bg_color='transparent').place(x=15,y=100)
edt_endereco = ctk.CTkEntry(frmResposta,width=450,height=25)
edt_endereco.pack(pady=0)
edt_endereco.place(x=15,y=122)

lb_complemento = ctk.CTkLabel(frmResposta,text='Complemento',bg_color='transparent').place(x=480,y=100)
edt_complemento = ctk.CTkEntry(frmResposta,width=160,height=25)
edt_complemento.pack(pady=0)
edt_complemento.place(x=480,y=122)

lb_bairro  = ctk.CTkLabel(frmResposta,text='Bairro',bg_color='transparent').place(x=15,y=148)
edt_bairro = ctk.CTkEntry(frmResposta,width=250,height=25)
edt_bairro.pack(pady=0)
edt_bairro.place(x=15,y=170)

lb_cidade  = ctk.CTkLabel(frmResposta,text='cidade',bg_color='transparent').place(x=280,y=148)
edt_cidade = ctk.CTkEntry(frmResposta,width=290,height=25)
edt_cidade.pack(pady=0)
edt_cidade.place(x=280,y=170)

lb_estado  = ctk.CTkLabel(frmResposta,text='UF',bg_color='transparent').place(x=590,y=148)
edt_estado = ctk.CTkEntry(frmResposta,width=50,height=25)
edt_estado.pack(pady=0)
edt_estado.place(x=590,y=170)

lb_cep  = ctk.CTkLabel(frmResposta,text='CEP',bg_color='transparent').place(x=15,y=195)
edt_cep = ctk.CTkEntry(frmResposta,width=100,height=25)
edt_cep.pack(pady=0)
edt_cep.place(x=15,y=215)

edt_CNAE1 = ctk.CTkTextbox(frmResposta,width=600,height=100, activate_scrollbars=True)
edt_CNAE1.pack(pady=0)
edt_CNAE1.place(x=15,y=245)

   
self.mainloop()
