import ctypes
import json
import os
import sys
from funcoes import dlg_mensagem
from funcoes import validar_json

# Obtem a pasta do projeto
diretorio_script = os.path.dirname(os.path.abspath(__file__))

#Constantes de Configuração
#DLL ACBrLibSAT utilizada neste projeto é 64 ST (Single Thread)
PATH_DLL                = os.path.abspath(os.path.join(diretorio_script,r"ACBrLib\x64\ACBrConsultaCNPJ64.dll"))
PATH_ACBRLIB            = os.path.abspath(os.path.join(diretorio_script, "ACBrLib.INI"))
PATH_LOG                = os.path.abspath(os.path.join(diretorio_script, "Log"))

#Cria a pasta log se nao existir
if not os.path.exists(PATH_LOG):
   os.makedirs(PATH_LOG) 

#Verifica se a dll está no path indicado
if not os.path.exists(PATH_DLL):
   dlg_mensagem(f"O arquivo '{PATH_DLL}' não existe.")
   sys.exit(1)
    
#função para definir o novo temanho da resposta
def define_bufferResposta(novo_tamanho):
    global tamanho_inicial, esTamanho, sResposta
    tamanho_inicial = novo_tamanho
    esTamanho = ctypes.c_ulong(tamanho_inicial)
    sResposta = ctypes.create_string_buffer(tamanho_inicial)
    return tamanho_inicial, esTamanho, sResposta 

# Carregar a DLL, ajustes os paths para seu ambiente.
acbr_lib = ctypes.CDLL(PATH_DLL)
resposta = acbr_lib.CNPJ_Inicializar(PATH_ACBRLIB.encode("utf-8"),"".encode("utf-8"))
if resposta != 0:
    dlg_mensagem(f'Resposta Inicializar | Erro Código:  {(resposta)}')
    sys.exit(1)

#configurando tipo de resposta retorno 
acbr_lib.CNPJ_ConfigGravarValor("Principal".encode("utf-8"), "TipoResposta".encode("utf-8"), str(2).encode("utf-8"))

#Configurando o log da Biblioteca
acbr_lib.CNPJ_ConfigGravarValor("Principal".encode("utf-8"), "LogNivel".encode("utf-8"), str(4).encode("utf-8"))
acbr_lib.CNPJ_ConfigGravarValor("Principal".encode("utf-8"), "LogPath".encode("utf-8"), PATH_LOG.encode("utf-8"))

#função para configurar o provedor de consulta
def configuraWS(LProvedor):
    LProvedoresDisponiveis = ['Nenhum','BrasilAPI','ReceitaWS','CNPJWS']
    LCodigoProvedor = LProvedoresDisponiveis.index(LProvedor)
    resultado = acbr_lib.CNPJ_ConfigGravarValor("ConsultaCNPJ".encode("utf-8"), "Provedor".encode("utf-8"), str(LCodigoProvedor).encode("utf-8"))
    if resultado != 0:
       dlg_mensagem(f"Erro configurando Provedor Codigo Erro:{(resultado)}")   
        
#função para executar a consulta CNPJ.
def consultaCNPJ(LCNPJ):
    if not LCNPJ:
        dlg_mensagem('ERRO',"O CNPJ é obrigatorio")
    else:
        define_bufferResposta(4096)
        resultado = acbr_lib.CNPJ_Consultar(LCNPJ.encode("utf-8"), sResposta, ctypes.byref(esTamanho))
        if resultado == 0:
            if validar_json(sResposta.value.decode("utf-8")):
                dados_json = json.loads(sResposta.value.decode("utf-8"))
                return dados_json
            else:
                dlg_mensagem('Erro ao ler resposta json, verifique o tamanho do buffer de resposta')
                return ''
                
        else:
            dlg_mensagem(f'CNPJ_Consultar |Erro código{(resultado)}"')          
            return ''