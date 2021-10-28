checagem1 = float(input('Digite a temperatura do paciente: '))
checagem2 = float(input('Digite quantos dias ele(a) apresenta tosse: '))
checagem3 = float(input('Digite a porcentagem da oxigenação sanguinea (sómente números): '))
if checagem1 > 39.0 and checagem2>3.0 and checagem3<70.0:
    print('Internação imediata')
else:
    print('Vai pra casa meu filho')
