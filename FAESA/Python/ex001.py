nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3.0
if media >= 7.0:
    print('Parabéns você está aprovado(a) com a média {}'.format(media))
elif media>=3:
    print('Parabéns você está aprovado(a) com a média {}'.format(media))
else:
    print('Você está na prova final.{}'.format(media))
