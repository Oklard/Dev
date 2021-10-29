#4 – (Valor 2,5) – Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa
#anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento
#de 1.5%. Faça um programa em Python que calcule e escreva o número de anos necessários para que a
#população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. Informe
#a quantidade de anos.
codigo = int(input('Funcionário insira o seu código:'))
número = int(input('Insira agora o seu número:'))
hora = int(input('Insira o número de horas trabalhadas'))
preçoPorHora = hora*10
excesso = (preçoPorHora-500)
if (hora<=50):
    excesso = 0
    print('Salário=',preçoPorHora,'reais')
else:  
    print('salário excedente',excesso,'salário total',500+(excesso*2)) 
   