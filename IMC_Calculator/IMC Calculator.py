#  este projeto tem tem por finalidade calcular a quantidade de massa corporal do usuário,
#  detectando também se o usuário é menor ou maior de idade


nome = str(input('Qual é seu nome? '))
idade = int(input('Qual é sua idade? '))
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
maiorIdade = 18
imc = peso / (altura ** 2)

if idade >= maiorIdade:
    print(nome, 'tem', idade, 'anos de idade (maior de idade) e seu IMC é {:.1f}'.format(imc))
elif idade < maiorIdade:
    print(nome, 'tem', idade, 'anos de idade (menor de idade) e seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal.")
elif 18.5 <= imc < 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL.")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO.")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE!")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")