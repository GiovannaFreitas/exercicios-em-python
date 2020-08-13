import sqlite3

conn = sqlite3.connect("informacoes_pacientes.db")
cursor = conn.cursor()

conn.execute("""CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    peso REAL NOT NULL,
    idade INTEGER NOT NULL,
    situacao TEXT NOT NULL,
    acompanhante TEXT NOT NULL
);
""")

print("BEM VINDE AO BANCO DE DADOS DOS PACIENTES\nDIGITE A OPÇÃO DESEJADA")
print("1 - Inserir\n2 - Deletar\n3 - Atualizar\n4 - Listar")
print("Para pacientes maior de idade, sinalizar no campo acompanhante")
opcao2 = int(input("OPÇÃO: "))
if opcao2 in [1, 2, 3, 4]:
    if opcao2 == 1:
        nome = input("Digite o nome: ").upper()
        peso = float(input("Digite o peso: "))
        idade = input("Digite a idade: ")
        situacao = input("Relate a situação do paciente: ")
        acompanhante = input("Nome do acompanhante: ")
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO pacientes(nome, peso, idade, situacao, acompanhante)
        VALUES('{nome}', {peso}, {idade}, '{situacao}', '{acompanhante}');""")
        conn.commit()
        print("Paciente cadastrado")
        conn.close()

    elif opcao2 == 2:

        id = int(input("Digite o ID do paciente: "))
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM pacientes WHERE id={id};")
        conn.commit()
        print("Paciente deletado")
        conn.close()


    elif opcao2 == 3:
        
        opcao1 = input("O que deseja atualizar? (NOME, PESO, IDADE ou SITUACAO) ").upper()
        id = int(input("Digite o ID do paciente: "))

        if opcao1 == "NOME":
            novo_nome = input("Novo nome: ")
            cursor = conn.cursor()
            cursor.execute(f"""UPDATE pacientes SET nome ='{novo_nome}' WHERE id={id};""")
            print("Nome atualizado")
            conn.commit()

        elif opcao1 == "PESO":
            novo_peso = float(input("Novo peso: "))
            cursor = conn.cursor()
            cursor.execute(f"""UPDATE pacientes SET peso ={novo_peso} WHERE id={id};""")
            print("Peso atualizado")
            conn.commit()

        elif opcao1 == "IDADE":
            nova_idade = int(input("Nova idade: "))
            cursor = conn.cursor()
            cursor.execute(f"""UPDATE pacientes SET idade ={nova_idade} WHERE id={id};""")
            print("Idade atualizada")
            conn.commit()


        elif opcao1 == "SITUACAO":
            atualizacao_caso = input("Atualização do paciente: ")
            cursor = conn.cursor()
            cursor.execute(f"""UPDATE pacientes SET atualizacao ='{atualizacao_caso}' WHERE id={id};""")
            print("Situação atualizada")
            conn.commit()

        else:
            print("Digite um campo válido e tente novamente.")

        conn.close()

    elif opcao2 == 4:

        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM pacientes;")
        pacientes = cursor.fetchall()

        if len(pacientes) > 0:
            print("PACIENTES INSERIDOS")
            for paciente in pacientes:
                print(f"ID: {paciente[0]}")
                print(f"NOME: {paciente[1]}")
                print(f"PESO: {paciente[2]}")
                print(f"IDADE: {paciente[3]}")
                print(f"SITUAÇÃO: {paciente[4]}")
                print(f"ACOMPANHANTE: {paciente[5]}")   
        else:
            print("Ainda não há pacientes cadastrados")
            
else:
    print("Opção inválida, tente novamente.")

conn.close()
