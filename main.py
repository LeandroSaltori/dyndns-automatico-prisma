import pandas as pd
import openpyxl
import win32com.client as win32

# Ler Tabela DynDNS



#Criar Menu de Leitura de XML

# Verificar DDNS Vencidos

#Enviar Whatsapp ao inserir o numero


# Enviar um email com o relatório dos proximos a vencer
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'leandrosb@hotmail.com'
mail.Subject = 'Teste de envio de email'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Leandro</p>
'''
mail.Display()
#mail.Send()
