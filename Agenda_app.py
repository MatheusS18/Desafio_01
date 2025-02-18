print("\n>>>>>> Bem vindo a Agenda <<<<<<\n")

contatos = []

def adicionar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)

    print("\nContato adicionado com sucesso!\n")


def visualizar_contato():
    print(list(contatos))



def editar_contato():
     if not contatos:
        print("\nNenhum contato na lista.\n")
        return

     nome_busca = input("Digite o nome do contato que deseja editar: ")

     for contato in contatos:
         if contato["nome"] == nome_busca:
            print(f"Editando contato: {contato['nome']}")
            contato["nome"] = input("Digite o novo nome: ") 
            contato["telefone"] = input("Digite o novo telefone: ")
            contato["email"] = input("Digite o novo email: ")

            print("\nContato atualizado com sucesso!\n")
            return
    
    

def marcar_desmarcar_favoritos():
    favoritos = input("Digite o nome do contato que quer favoritar/desfavoritar: ")

    for contato in contatos:  # Percorre a lista de contatos
        if contato["nome"] == favoritos:
            if "favorito" in contato and contato["favorito"] == "✓":
                contato["favorito"] = " "  # Desmarca dos favoritos
                print(f"Contato {contato['nome']} removido dos favoritos.")
            else:
                contato["favorito"] = "✓"  # Marca como favorito
                print(f"Contato {contato['nome']} adicionado aos favoritos.")
            return

    print("\nContato não encontrado.\n")  # Caso o nome não esteja na lista


def listar_favoritos():
    print("\nLista de Contatos Favoritos:")
    
    favoritos_encontrados = False  # Variável para verificar se há favoritos
    
    for contato in contatos:
        if "favorito" in contato and contato["favorito"] == "✓":
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            favoritos_encontrados = True

    if not favoritos_encontrados:
        print("Nenhum contato favorito encontrado.")

    print()  # Apenas para dar um espaço no terminal


def apagar_contato():
    nome_apagar = input("Digite o nome do contato que deseja apagar: ")

    for contato in contatos:
        if contato["nome"] == nome_apagar:
            contatos.remove(contato)  # Remove o contato da lista
            print(f"\nContato {nome_apagar} apagado com sucesso!\n")
            return  # Sai da função após remover

    print("\nContato não encontrado.\n")

while True:
    print (" 1. Adicionar contato")
    print (" 2. Visualizar contato")
    print (" 3. Editar contato")
    print (" 4. Marcar/Desmarcar contato nos favoritos")
    print (" 5. Lista de contatos favoritos")
    print (" 6. Apagar contato")


    menu = input("Digite o numero correspondete a sua escolha: ")

    if menu == "1":
        adicionar_contato()


    elif menu == "2":
        visualizar_contato()


    elif menu == "3":
        editar_contato()


    elif menu == "4":
        marcar_desmarcar_favoritos()


    elif menu == "5":
        listar_favoritos()


    elif menu == "6":
        apagar_contato()


        
        








