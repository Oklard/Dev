nota1 = input("Digite a nota 1 = ")
nota2 = input("Digite a nota 2 = ")
nota3 = input("Digite a nota 3 = ")
#atenção para conversao de str para Float.
soma = float(nota1) + float(nota2) + float(nota3)
media = soma / 3.0
#atencao para conversao de float para str 
print("A media é igual a " +str(media))