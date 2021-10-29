#3 - (Valor 2,5) - Faça um programa em Python que verifica se um determinado usuário (candidato a uma
#vaga) tem perfil para entrar em uma empresa. Para ser aprovado o usuário deve falar inglês e saber
#programar em Python. Se o candidato sabe programar em Python e não fala inglês deve ir para treinamento.
#Caso contrário o candidato está reprovado. Você deve perguntar para o usuário se ele sabe programar em
#Python e se fala em inglês. As seguintes mensagens devem ser exibidas conforme a resposta do candidato:
# A mensagem "Aprovado", se o usuário fala inglês e sabe programar em Python;
# A mensagem "Treinamento", se o usuário sabe programar em Python e não fala inglês;
 #A mensagem "Eliminado", se o candidato não sabe programar em Python. 
ingles = input('Você sabe falar inglês?')
programar = input('Você sabe programar em python?')
ingles = ingles.lower()
programar = programar.lower()
print(ingles,programar)
if (ingles=='sim' and programar=='sim'):
    print('Aprovado')
elif (programar=='sim' and ingles!='sim'):
    print('Treinamento')
else: 
    print('Eliminado')