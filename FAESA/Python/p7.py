nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doencaInfectagiosa= input("Voce tem doenca infectagiosa? (SIM/NAO): ").upper()
if (idade >= 65) and (doencaInfectagiosa=="SIM"):
    print("O paciente " + nome + " sera direcionado para sala AMARELA - COM PRIORIDADE")    
elif (idade < 65) and (doencaInfectagiosa=="SIM"):
    print("O paciente " + nome + " sera direcionado para sala AMARELA - sem prioridade")    
elif (idade >= 65) and (doencaInfectagiosa=="NAO"):
        print("O paciente " + nome + " sera direcionado para sala BRANCA - COM PRIORIDADE") 
elif (idade < 65) and (doencaInfectagiosa=="NAO"):
        print("O paciente " + nome + " sera direcionado para sala BRANCA - sem prioridade") 
else:
    print("Responda a suspeita de doenca infectagiosa com SIM ou NAO")
