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
