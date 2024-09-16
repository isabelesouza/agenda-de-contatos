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

   