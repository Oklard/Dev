#2 - (Valor 2,5) - O cardápio da lanchonete da FAESA é dado abaixo. Faça um programa em Python que leia
#cada item comprado e a quantidade de cada item escolhido e calcule o valor da conta final.
#Pão de Queijo..........................R$ 3,00.
#Misto Quente........................ R$ 5,00.
#Coxinha..........................R$ 4,00.
#Mate...............R$3,00.
#Água............... R$2,00.
#Refrigerante...............R$4,00. 
paoDeQueijo = int(input('Insira a quantidade de pão(es) de queijo'))
mistoQuente = int(input('Insira a quantidade de misto(s) quente(s)'))
coxinha = int(input('Insira a quantidade de coxinhas'))
mate = int(input('Insira a quantidade de mate'))
agua = int(input('Insira a quantidade de água(s)'))
refrigerante = int(input('Insira a quantidade de refrigerante(s)'))
total = (paoDeQueijo*3)+(mistoQuente*5)+(coxinha*4)+(mate*3)+(agua*2)+(refrigerante*4)
print('foram comprados,',paoDeQueijo,'pão(es) de queijo,',mistoQuente,'misto(s) quente(s),',coxinha,'coxinha(s),',mate,'mate,',agua,'água(s),',refrigerante,'refrigerante(s),','A sua refeição custou,',total,'reais')
