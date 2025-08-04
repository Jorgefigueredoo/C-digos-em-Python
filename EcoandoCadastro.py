def solicitar_input(msg, limite, obrigatorio=True, somente_digitos=False, validar_func=None):
    while True:
        valor = input(msg).strip()
        if obrigatorio and not valor:
            print("Este campo é obrigatório. Por favor, digite novamente.")
            continue
        if len(valor) > limite:
            print(f"Valor muito longo! Máximo de {limite} caracteres. Por favor, digite novamente.")
            continue
        if somente_digitos and not valor.isdigit():
            print("Digite apenas números. Tente novamente.")
            continue
        if validar_func and not validar_func(valor):
            print("Formato inválido. Tente novamente.")
            continue
        return valor

def validar_email(email):
    return "@" in email and "." in email

def cadastro_pessoa_fisica(dados_comuns):
    nome = solicitar_input(f"Informe o seu nome completo (máximo {LIMITE_NOME_PF} caracteres): ", LIMITE_NOME_PF)
    cpf = solicitar_input(f"Informe o seu CPF (apenas números, {LIMITE_CPF} dígitos): ", LIMITE_CPF, somente_digitos=True)

    dados = {
        "tipo": "Pessoa Física",
        "nome": nome,
        "cpf": cpf,
        **dados_comuns
    }
    cadastros.append(dados)
    imprimir_dados(dados)

def cadastro_empresa(dados_comuns):
    razao_social = solicitar_input(f"Informe a Razão Social da empresa (máximo {LIMITE_RAZAO_SOCIAL} caracteres): ", LIMITE_RAZAO_SOCIAL)
    cnpj = solicitar_input(f"Informe o CNPJ da empresa (apenas números, {LIMITE_CNPJ} dígitos): ", LIMITE_CNPJ, somente_digitos=True)

    dados = {
        "tipo": "Empresa",
        "razao_social": razao_social,
        "cnpj": cnpj,
        **dados_comuns
    }
    cadastros.append(dados)
    imprimir_dados(dados)

def imprimir_dados(dados):
    print("\n--- Cadastro Realizado com Sucesso! ---")
    print(f"Tipo de Cadastro: {dados['tipo']}")
    if dados["tipo"] == "Pessoa Física":
        print(f"Nome: {dados['nome']}")
        print(f"CPF: {dados['cpf']}")
    else:
        print(f"Razão Social: {dados['razao_social']}")
        print(f"CNPJ: {dados['cnpj']}")
    print(f"Email: {dados['email']}")
    print(f"Telefone: {dados['telefone']}")
    print(f"CEP: {dados['cep']}")
    print(f"Endereço: {dados['endereco']}")
    print(f"Tipo de Lixo: {dados['tipo_lixo']}")
    print("\n-------------------------------------\n")

print("Olá, tudo bem, como posso ajudar hoje?")


LIMITE_EMAIL = 100
LIMITE_TELEFONE = 11
LIMITE_CEP = 8
LIMITE_ENDERECO = 200
LIMITE_TIPO_LIXO = 50
LIMITE_NOME_PF = 50
LIMITE_CPF = 11
LIMITE_RAZAO_SOCIAL = 100
LIMITE_CNPJ = 14

cadastros = []

while True:
    acao_principal = input("\nDigite 'cadastro' para iniciar ou 'sair' para encerrar: ").lower()

    if acao_principal == "cadastro":
        while True:
            tipo_cadastro = input("Você deseja cadastrar como 'pessoa fisica' ou 'empresa'? ").lower()
            if tipo_cadastro in ["pessoa fisica", "empresa"]:
                break
            else:
                print("Opção inválida. Por favor, digite 'pessoa fisica' ou 'empresa'.")

        print(f"\n--- Iniciando cadastro de {'Pessoa Física' if tipo_cadastro == 'pessoa fisica' else 'Empresa'} ---")

       
        email = solicitar_input(f"Informe o seu email (máximo {LIMITE_EMAIL} caracteres): ", LIMITE_EMAIL, validar_func=validar_email)
        telefone = solicitar_input(f"Informe o seu telefone com DDD (apenas números, {LIMITE_TELEFONE} dígitos): ", LIMITE_TELEFONE, somente_digitos=True)
        cep = solicitar_input(f"Informe o seu CEP (apenas números, {LIMITE_CEP} dígitos): ", LIMITE_CEP, somente_digitos=True)
        endereco = input(f"Informe o seu endereço completo (máximo {LIMITE_ENDERECO} caracteres): ")[:LIMITE_ENDERECO].strip()
        tipo_lixo = input(f"Informe o tipo de lixo que mais irá descartar (ex: orgânico, reciclável; máximo {LIMITE_TIPO_LIXO} caracteres): ")[:LIMITE_TIPO_LIXO].strip().capitalize()

        dados_comuns = {
            "email": email,
            "telefone": telefone,
            "cep": cep,
            "endereco": endereco,
            "tipo_lixo": tipo_lixo
        }

        if tipo_cadastro == "pessoa fisica":
            cadastro_pessoa_fisica(dados_comuns)
        else:
            cadastro_empresa(dados_comuns)

        continuar = input("Deseja realizar outro cadastro? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando o sistema de cadastros. Até mais!")
            break

    elif acao_principal == "sair":
        print("Programa encerrado, até mais!!!")
        break

    else:
        print("Mensagem inválida... Tente novamente.")
