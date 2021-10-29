num1 = int(input('Insira o primeiro número'))
num2 = int(input('Insira o segundo número'))
num3 = int(input('Insira o terceiro número'))
print((num1*2)*(num2/2))
print((num1*3)+num2)
if (num1<num2 and num1<num3):
    print('O menor numéro é o primeiro ',num1,'e')
elif (num3>num2 and num2<num1):
    print('O menor número é o segundo e',num2,'e')
elif (num3<num1 and num3<num2):
    print('O menor número é o terceiro e',num3,'e')
if (num1>num2 and num1>num3):
    print('o maior número é o primeiro',num1)
elif (num2>num3 and num2>num1):
    print('o maior número é o segundo',num2)
elif(num3>num1 and num3>num2):
    print('o maior número é o terceiro',num3)