import win32com.client as win32

# Enviar um email com o relatório
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
