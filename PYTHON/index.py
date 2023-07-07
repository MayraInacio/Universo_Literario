nota1 = float(input("Qual a nota que o aluno(a) tirou no bimestre? "))
nota2 = float(input("Qual a segunda nota adquirido pelo aluno(a) no segundo bimestre? "))
nota3 = float(input("Qual a nota que o aluno(a) tirou no TERCEIRO? "))
nota4 = float(input("Qual a segunda nota adquirido pelo aluno(a) no quarto bimestre? "))
media = (nota1 + nota2 + nota3 + nota4)/2
if media >= 7:
    situacao = "Aprovado(a), Parabéns!!"
    print("Com uma média de {:.2f}".format(media),",o aluno(a) está",situacao)
else:
    situacao = "REPROVADO"
    print("Com uma média de {:.2f}".format(media), ",o aluno(a) está",situacao)

recuperacao = (input("Você quer fazer recuperação? responda com sim ou nao"))
if recuperacao == "sim" and recuperacao == "nao":
    print("OK, você irá fazer a recuperação, aguarde um instante...")
else:
    print("OK, você não irá fazer a recuperação")