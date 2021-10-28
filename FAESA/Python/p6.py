nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doencaInfectagiosa= input("Voce tem doenca infectagiosa? (SIM/NAO): ").upper()
if (idade >= 65):
    print("O paciente " + nome + " possui atendimento prioritario") 
elif (doencaInfectagiosa == "SIM"):
    print("O paciente " + nome + " deve ir para uma sala reservada")
else:
    print("O paciente " + nome + " NAO possui atendimento prioritario e pode ir para recepcao")