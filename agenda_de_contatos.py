# Aluna:Isabele Silva Souza Monteiro Matrícula: 2222868
# Closure para armazenar contatos
def agenda():
    contatos = []

    # Função para adicionar contatos
    def adicionar_contato(nome, telefone, email):
        contatos.append({
            'nome': nome,
            'telefone': telefone,
            'email': email
        })
        return f"Contato {nome} adicionado com sucesso!"

    # Função para remover contato
    def remover_contato(nome):
        nonlocal contatos
        contatos = [contato for contato in contatos if contato['nome'] != nome]
        return f"Contato {nome} removido com sucesso!" if any(contato['nome'] == nome for contato in contatos) else f"Contato {nome} não encontrado!"

    # Função para buscar contato
    def buscar_contato(nome):
        resultados = [contato for contato in contatos if contato['nome'] == nome]
        return resultados if resultados else f"Contato {nome} não encontrado!"

    # Função para listar todos os contatos usando list comprehension
    def listar_contatos():
        return [contato for contato in contatos] if contatos else "Nenhum contato encontrado!"

    return adicionar_contato, remover_contato, buscar_contato, listar_contatos

# Função lambda para formatar os contatos
formatar_contato = lambda contato: f"{contato['nome']} - {contato['telefone']} - {contato['email']}"

# Função de alta ordem que processa múltiplos contatos
def processar_contatos(operacao, lista_de_contatos):
    return [operacao(contato) for contato in lista_de_contatos]

# Inicializando a agenda
adicionar, remover, buscar, listar = agenda()

# Testando a adição de contatos
adicionar("Maria", "99999-9999", "maria@example.com")
adicionar("João", "88888-8888", "joao@example.com")
adicionar("Ana", "77777-7777", "ana@example.com")

# Testando a remoção de um contato
remover("Ana")

# Listando todos os contatos
todos_contatos = listar()

# Formatando os contatos para exibição
contatos_formatados = processar_contatos(formatar_contato, todos_contatos)

# Exibindo contatos formatados
for contato in contatos_formatados:
    print(contato)
