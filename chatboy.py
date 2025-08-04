def interagirPython():
    print("")
    area = str(input("Informe a área deseja da linguagem Python: Web, Jogos e Dados")).lower()

    if area == 'web':
        print("Você escolheu a área de Web com Python.")
      
    elif area == 'jogos':
        print("Você escolheu a área de Jogos com Python.")
    
    elif area == 'dados':
        print("Você escolheu a área de Dados com Python.")
     
    else:
        print("Área não reconhecida para Python.")


def interagirPHP():
    print("")
    area = str(input("Informe a área deseja da linguagem PHP: Web, Jogos e Dados: ")).lower()

    if area == 'web':
        print("Você escolheu a área de Web com PHP: ")
    
    elif area == 'jogos':
        print("Você escolheu a área de Jogos com PHP: ")
       
    elif area == 'dados':
        print("Você escolheu a área de Dados com PHP.")
    
    else:
        print("Área não reconhecida para PHP.")


def interagirJavaScript():
    print("")
    area = str(input("Informe a área deseja da linguagem JavaScript: Web, Jogos e Dados")).lower()

    if area == 'web':
        print("Você escolheu a área de Web com JavaScript.")
     
    elif area == 'jogos':
        print("Você escolheu a área de Jogos com JavaScript.")
      
    elif area == 'dados':
        print("Você escolheu a área de Dados com JavaScript.")
    
    else:
        print("Área não reconhecida para JavaScript.")


def interagirHTML():
    print("")
    area = str(input("Informe a área deseja da linguagem HTML: Web, Jogos e Dados")).lower()

    if area == 'web':
        print("Você escolheu a área de Web com HTML.")
       
    elif area == 'jogos':
        print("Você escolheu a área de Jogos com HTML.")
       
    elif area == 'dados':
        print("Você escolheu a área de Dados com HTML.")
       
    else:
        print("Área não reconhecida para HTML.")


def chatBot():
    print('Olá, seja bem vindo ao Chat Kjol')

    while True:
        linguagem = str(input("Qual linguagem deseja aprender? Te ajudo com: Python, JavaScript, PHP e HTML (ou digite 'Sair')")).lower()

        if linguagem == "sair":
            print("Encerrando atendimento...")
            break
        elif linguagem == "python":
            interagirPython()
        elif linguagem == "php":
            interagirPHP()
        elif linguagem == "javascript":
            interagirJavaScript()
        elif linguagem == "html":
            interagirHTML()
        else:
            print("Linguagem não reconhecida, tente novamente...\n")

chatBot()