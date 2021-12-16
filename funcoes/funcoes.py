def verify_email(email):
    '''
    Verifica o email do cliente é valido
    :return:
    '''
    if email not in '@':
        return f'Porfavor, digite um email válido.'
    else email is '@'
        return f'Email correto'


ef email ():
    '''

    :return:
    '''
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